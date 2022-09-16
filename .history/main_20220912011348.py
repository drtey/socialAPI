from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Python API"}

@app.post("cpost")
def cpost(payload: dict = Body(...)):
    print(payload)
    return {"message": "Bye world"}