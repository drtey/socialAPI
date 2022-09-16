from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id" : 1}, {
"title": "favorite foods", "content": "I like pizza" , "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
async def root():
    return {"message": "Python API"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def cpost(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)
    #print(post.dict())
    return {"data": post_dict}
# title str, content str, category, Bool published

@app.get("/posts/{id}")
def get_post(id):
    print(type(id))
    post = find_post(int(id))
    print(post)
    return {"post_detail": post}