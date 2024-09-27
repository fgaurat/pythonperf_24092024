from fastapi import FastAPI

app = FastAPI()

# fastapi dev main_fastapi.py
@app.get("/")
def read_root():
    return {"Hello": "World"}

