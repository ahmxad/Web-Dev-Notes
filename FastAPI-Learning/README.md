## Starting with SQLModel
### Template code:

```py
from fastapi import FastAPI
from sqlmodel import Field, SQLModel, create_engine
from typing import ClassVar # importing this prefents type errors (specifically used in Table Model)
from contextlib import asynccontextmanager

class Hero(SQLModel, table=True): # table=True means it will create a table named "Hero"
    __tablename__: ClassVar[str] = "heroes" # But here we specified the name of the table
    __table_args__ = {"schema": "sqlmodel"}
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

# Database URL
DATABASE_URL = "postgresql://postgres:password@localhost:5432/db"
engine = create_engine(DATABASE_URL, echo=True) # echo=True means it will print the sql query in the terminal

@asynccontextmanager # Runs only once
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)
```