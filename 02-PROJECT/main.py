from fastapi import FastAPI
from sqlmodel import Field, SQLModel, create_engine, Session, select
from typing import ClassVar, List
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

class Client(SQLModel, table=True):
    __tablename__: ClassVar[str] = "clients"
    __table_args__ = {"schema": "sqlmodel"}
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    text: str | None

class ReadClient(SQLModel):
    name: str
    text: str | None

class CreateClient(SQLModel):
    name: str
    text: str | None = None


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

@app.get("/clients", response_model=List[ReadClient])
def get_clients():
    with Session(engine) as session:
        clients = session.exec(select(Client)).all()
        return clients
    
@app.post("/clients", response_model=ReadClient)
def create_client(client: CreateClient):
    with Session(engine) as session:
        db_client = Client.model_validate(client)
        session.add(db_client)
        session.commit()
        session.refresh(db_client)
        return client