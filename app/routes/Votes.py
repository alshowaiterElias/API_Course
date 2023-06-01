from fastapi import Depends,  Response, status, HTTPException, APIRouter
from .. import models, schemas, OAuth2
from ..db import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=["Votes"]
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user=Depends(OAuth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post Does not exist")

    Query = db.query(models.Vote).filter(models.Vote.post_id ==
                                         vote.post_id, models.Vote.user_id == current_user.id)

    if (vote.dir == 1):
        if (Query.first()):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Already voted")
        vote_to_add = models.Vote(
            post_id=vote.post_id, user_id=current_user.id)
        db.add(vote_to_add)
        db.commit()
        return {"message": "added vote"}
    else:
        if not Query.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Does not Exist")
        Query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Deleted vote"}
