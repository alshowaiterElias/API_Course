from jose import JWTError, jwt
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(pwd, hashed_pwd):
    return pwd_context.verify(pwd, hashed_pwd)
