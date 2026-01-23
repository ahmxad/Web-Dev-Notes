from fastapi import FastAPI, HTTPException
from sqlmodel import Field, SQLModel, create_engine, Session, select
from typing import ClassVar, List, Optional
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

# TABLE
class Book(SQLModel, table=True):
    __tablename__: ClassVar[str] = "books"
    __table_args__ = {"schema": "sqlmodel"}
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    year: int | None = None

# How the get request will look
class ReadBook(SQLModel):
    name: str
    year: int | None

# How the patch request will look
class UpdateBook(SQLModel):
    name: Optional[str] = None
    year: Optional[int] = None

DATABASE_URL = "postgresql://postgres:abc12345@localhost:5432/sqlmodeldb"
engine = create_engine(DATABASE_URL, echo=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Solid Js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GET
@app.get('/books', response_model=List[ReadBook])
def getting():
    with Session(engine) as session:
        books = session.exec(select(Book)).all()
        return books
    
# POST
@app.post('/books', response_model=ReadBook)
def create_book(book:Book):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return book
    
# PATCH
@app.patch("/books/{id}", response_model=ReadBook)
def update_book(id: int, book_update: UpdateBook):
    with Session(engine) as session:
        book = session.get(Book, id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        # Update only the fields provided
        if book_update.name is not None:
            book.name = book_update.name
        if book_update.year is not None:
            book.year = book_update.year

        session.add(book)
        session.commit()
        session.refresh(book)
        return book

# DELETE
@app.delete('/books/{id}')
def delete_book(id: int):
    with Session(engine) as session:
        book = session.get(Book, id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        session.delete(book)
        session.commit()
    return {"Message": "Book deleted successfully"}