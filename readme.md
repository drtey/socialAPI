# socialAPI

REST API developed with [Python](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com) & [PostgreSQL](https://www.postgresql.org/)
where you can register users, create and vote posts

Model Validation, JWT Authentication, ORM, Unit testing, password hashing, etc

Stack: SQLAlchemy, psycopg2, OAuth2, bcrypt, pydantic, JWT, FastAPI...

### Run project
```
$ uvicorn app.main:app --reload
```

## Build

### Install dependencies
```
$ pip install -r requirements.txt
```

### Create virtual environment
```
$ python3 -m venv <name_of_environment>
$ source <name_of_environment>/bin/activate
```

### PostgreSQL
```
$ sudo apt install postgresql postgresql-contrib
$ sudo service postgresql start
$ sudo -u postgres psql
postgres=# CREATE DATABASE <name_of_db>;
```
To change default pass for "postgres" DB user (NOT UNIX User):
```
postgres=# \password postgres
```

### Documentation 
http://127.0.0.1:8000//docs & http://127.0.0.1:8000//redoc 


