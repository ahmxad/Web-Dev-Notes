basic fastapi app starting steps

- mkdir folder_name
- cd folder_name
- uv init .
- uv add fastapi
- .venv\Scripts\activate | source .venv/bin/activate
- "uv sync" for syncing the packages in .toml file
- path to interpreter: /home/ahmad/project folder/.venv/bin/python (in ubuntu)
- uv add uvicorn
- uv add pydantic
- run app by typing uvicorn main:app --reload (main is the file name, app is the app = FastAPI())