from typing import List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel

from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
    

while True:

    try: 
        conn = psycopg2.connect(host='localhost', port=3306, database='postgres', 
                                user='postgres', password='trucktor3', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting from database failed")
        print("Error: ", error)
        time.sleep(2)
        
app.include_router(post.router)      
app.include_router(user.router)      
app.include_router(auth.router)      
        

#Mensaje de inicio
@app.get("/")
async def root():
    mensaje = f"Bienvenido, esto es una API que simula una red social realizada con Fast API y Swagger por lo que si va a /docs o /redoc puedes comprobar la documentación."
    return {mensaje}



    