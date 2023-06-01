from typing import List, Optional
from fastapi import Depends,  Response, status, HTTPException, APIRouter
from .. import models, schemas, OAuth2
from ..db import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

# Get All Posts


@router.get('/', response_model=List[schemas.PostWithVote])
def get_posts(db: Session = Depends(get_db),
              current_user: int = Depends(OAuth2.get_current_user),
              limit: int = 30,
              skip: int = 0,
              search: Optional[str] = ""):

    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
        models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return posts

# Get Single Post


@router.get('/{id}', response_model=schemas.PostWithVote)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(OAuth2.get_current_user)):

    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if post == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    return post

# Create Post


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(OAuth2.get_current_user)):

    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

# Update Post


@router.put('/{id}', status_code=status.HTTP_205_RESET_CONTENT, response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(OAuth2.get_current_user)):

    postQuery = db.query(models.Post).filter(models.Post.id == id)

    if postQuery.first() == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    if post.first().owner_id != current_user.id:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            detail=f"NOT ALLOWED")
    postQuery.update(post.dict(), synchronize_session=False)
    db.commit()
    return postQuery.first()

# Delete Post


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(OAuth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    if post.first().owner_id != current_user.id:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            detail=f"NOT ALLOWED")
    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
