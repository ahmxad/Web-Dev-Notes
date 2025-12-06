from fastapi import FastAPI

app = FastAPI(title="My fastapi app")

@app.get("/")
def read_root():
    return {"message": "Hello World"}
