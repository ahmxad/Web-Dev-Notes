from fastapi import FastAPI
from sqlmodel import Field, SQLModel, create_engine, Session
from typing import ClassVar
from contextlib import asynccontextmanager

class Hero(SQLModel, table=True):
    __tablename__: ClassVar[str] = "heroes"
    __table_args__ = {"schema": "sqlmodel"}
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

DATABASE_URL = "postgresql://postgres:abc12345@localhost:5432/sqlmodeldb"
engine = create_engine(DATABASE_URL, echo=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)