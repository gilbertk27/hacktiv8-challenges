from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def handler():
    return {"Hello": "World"}