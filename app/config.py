from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_Hostname: str
    DB_Password: str
    DB_Port: str
    DB_Name: str
    DB_Username: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"


setting = Settings()
