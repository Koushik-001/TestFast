from fastapi import FastAPI
from routes.blog import root

app = FastAPI()

app.include_router(root)