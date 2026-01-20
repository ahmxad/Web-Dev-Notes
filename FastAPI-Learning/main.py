from fastapi import FastAPI, HTTPException
from sqlmodel import Field, SQLModel, create_engine, Session, select
from typing import ClassVar, List
from contextlib import asynccontextmanager

class Book(SQLModel, table=True):
    __tablename__: ClassVar[str] = "books"
    __table_args__ = {"schema": "sqlmodel"}
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = None

class ReadBook(SQLModel):
    name: str

DATABASE_URL = "postgresql://postgres:abc12345@localhost:5432/sqlmodeldb"
engine = create_engine(DATABASE_URL, echo=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)
# Code above omitted 👆

@app.get('/', response_model=List[ReadBook])
def getting():
    with Session(engine) as session:
        books = session.exec(select(Book)).all()
        return books
    
@app.post('/')
def create_book(book:Book):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return book
    
@app.delete('/{id}')
def delete_book(id:int):
    with Session(engine) as session:
        book = session.get(Book, id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(book)
    session.commit()
    return {"Message": "Book deleted successfully"}