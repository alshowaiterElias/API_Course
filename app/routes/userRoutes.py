from fastapi import Depends,  Response, status, HTTPException, APIRouter
from .. import models, schemas, utils
from ..db import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Creating a User


@router.get('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    user.password = utils.hash(user.password)

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# Getting a User


@router.get('/{id}', response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def create_user(id: int, db: Session = Depends(get_db)):

    Query = db.query(models.User).filter(models.User.id == id)
    if Query.first() == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    Query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
