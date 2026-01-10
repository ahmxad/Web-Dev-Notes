from fastapi import FastAPI
from sqlmodel import SQLModel, Field

app = FastAPI()

class Hero(SQLModel):
    name: str

@app.post("/")
async def create_hero(hero: Hero):
    return hero
