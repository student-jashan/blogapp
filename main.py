from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title: str
    content: str
    # user_id: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: PostBase, db: db_dependency):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
def get_post(post_id: int, db: db_dependency):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@app.put("/posts/{post_id}", status_code=status.HTTP_200_OK)
def update_post(post_id: int, post: PostBase, db: db_dependency):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()

    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    db_post.title = post.title
    db_post.content = post.content

    db.commit()
    db.refresh(db_post)

    return db_post


@app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
def delete_post(post_id: int, db: db_dependency):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()

    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(db_post)
    db.commit()

    return {"message": "Post deleted successfully"}