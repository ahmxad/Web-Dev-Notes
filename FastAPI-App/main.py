from fastapi import FastAPI
from sqlalchemy import create_engine, text
from pydantic import BaseModel

app = FastAPI()

DATABASE_URL = "postgresql://postgres:abc12345@localhost:5432/demo_db"
engine = create_engine(DATABASE_URL)

# -------- Schema (request body) --------
class UserCreate(BaseModel):
    email: str
    password: str


# -------- GET: sab users laao --------
@app.get("/users")
def get_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id, email FROM users")) # you can also retrive password 😹
        rows = result.fetchall()

    return [dict(row._mapping) for row in rows]


# -------- POST: naya user banao --------
@app.post("/users")
def create_user(user: UserCreate):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO users (email, password)
                VALUES (:email, :password)
            """),
            {
                "email": user.email,
                "password": user.password
            }
        )
        conn.commit()

    return {"status": "user created"}
