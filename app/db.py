import time
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import setting
sql_alchemy_db_url = f"postgresql://{setting.DB_Username}:{setting.DB_Password}@{setting.DB_Hostname}:{setting.DB_Port}/{setting.DB_Name}"

engine = create_engine(sql_alchemy_db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while (True):
#     try:
#         conn = psycopg2.connect(host='localhost', database='API_Course',
#                                 user='postgres', password="Alshowaiter12", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("connected sucessfully")
#         break
#     except Exception as error:
#         print("connection failed")
#         print(error)
#         time.sleep(5)
