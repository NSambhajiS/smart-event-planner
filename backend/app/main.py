from fastapi import FastAPI
from database import db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Smart Event Planner API is running"}