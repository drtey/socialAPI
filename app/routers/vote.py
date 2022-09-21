from unicodedata import name
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/votes",
    tags=['Votes']
)

#Ruta anadir votos
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Vote)
def gen_vote(vote: schemas.Vote, db: Session = Depends(get_db)):

    new_vote = models.Vote(**vote.dict())
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)


#Ruta coger todos los votos
@router.get("/{id}", response_model=List[schemas.Vote])
def count_votes(id: int, vote: schemas.Vote, db: Session = Depends(get_db)):

    vote_query = db.query(models.Votes).filter(models.Votes.id == id)

    if id == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"vote with id: {id} does not exist")
        
    return {"data": vote_query.all()}
    