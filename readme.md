# socialAPI

REST API developed with [Python](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com) & [PostgreSQL](https://www.postgresql.org/)
where you can register as user, publicate posts and vote posts

Model validation, login with JWT, ORM, unit testings, hashing passwords

Stack: SQLAlchemy, psycopg2, OAuth2, bcrypt, pydantic, JWT, fastapi

## DISCLAIMER: This was made using WSL2 integration

### Install dependencies
```
$ pip install -r requirements.txt
```

### Create virtual environment
```
$ py -3 -m venv <name_of_environment>
$ source <name_of_environment>/bin/activate
```

### PostgreSQL
Install and run postgresql service

```
$ sudo apt install postgresql postgresql-contrib
$ sudo service postgresql start
$ sudo su postgres
```
```
postgres@desktop~/socialAPI$ psql postgres
postgres=# \password postgres
```
Password should be 'postgres' to match the original config files,
if you want to use a different one you can configure it inside main.py and database.py  

### Run project
```
$ uvicorn app.main:app --reload
```

### Documentation 
http://127.0.0.1:8000//docs & http://127.0.0.1:8000//redoc 


