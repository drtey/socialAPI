from sqlalchemy import Column
from .database import Base

class Post(Base):
    __tablename__ = "posts"
    
    id = 