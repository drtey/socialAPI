from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:trucktor3@127.0.0.1/localhost/postgres'

engine = create_engine(SQLALCHEMY_DATABASE_URL)