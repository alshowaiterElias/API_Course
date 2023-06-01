from fastapi import FastAPI
from . import models
from .db import engine
from .routes import userRoutes, postRoutes, Auth, Votes
from .config import setting
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(postRoutes.router)
app.include_router(userRoutes.router)
app.include_router(Auth.router)
app.include_router(Votes.router)


@app.get("/")
def root():
    return {"detail": "connected to application"}
