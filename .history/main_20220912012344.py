from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/")
async def root():
    return {"message": "Python API"}

@app.post("/cpost")
def cpost(post: Post):
    print(post)
    return {"message": f"title: {payload['title']} content: {payload['content']}"}
# title str, content str, category, Bool published