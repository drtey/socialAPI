from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Python API"}

@app.post("cpost")
def create post(payload: dict = Body(...)):
    