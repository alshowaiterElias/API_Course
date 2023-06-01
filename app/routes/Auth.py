from typing import List
from fastapi import Depends,  Response, status, HTTPException, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import models, schemas, utils, OAuth2
from ..db import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=["Authentication"])


@router.get('/login', response_model=schemas.Token)
def login(userCred: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == userCred.username).first()

    if user == None:
        raise HTTPException(status.HTTP_403_FORBIDDEN,
                            detail=f"Invalied credentials")

    if not utils.verify(userCred.password, user.password):
        raise HTTPException(status.HTTP_403_FORBIDDEN,
                            detail=f"Invalied credentials")

    access_token = OAuth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
