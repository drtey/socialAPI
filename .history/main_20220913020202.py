from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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


@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}


@app.get("/posts/{id}")
def get_post(id:int, response: Response):
    post = find_post(id)
    if not post: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post_detail": post}
