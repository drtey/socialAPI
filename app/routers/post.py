from unicodedata import name
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

#Obtener listado de posts
@router.get("/", response_model=List[schemas.Post])
async def get_posts(db: Session = Depends(get_db)):
    
    posts= db.query(models.Post).all()
    return posts


#Ruta obtener post por ID
@router.get("/{id}", response_model=List[schemas.Post])
def get_post(id:int, db: Session = Depends(get_db)):
    
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return post


#Ruta creación de post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), get_current_user: int ):
    
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post


#Ruta borrar post por ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def borrar_post(id: int, db: Session = Depends(get_db)):
    
    post = db.query(models.Post).filter(models.Post.id == id)
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
    
    post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NOT_CONTENT)


#Ruta editar post por ID
@router.put("/{id}", response_model=schemas.Post)
def editar_post(id: int, editado_post: schemas.Post, db: Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
        
    post_query.update(editado_post.dict(), synchronize_session=False)
    
    db.commit()

    return {"data": post_query.first()}