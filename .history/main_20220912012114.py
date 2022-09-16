from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Python API"}

@app.post("/cpost")
def cpost(payload: dict = Body(...)):
    print(payload)
    return {"message": f"title: {payload['title']} content: {payload['content']}"}
# title str, content str