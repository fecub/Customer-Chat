from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.api.controller import create_api
from core.startup_main import startup_main

startup_main()

app = FastAPI()
api = create_api()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows ALL domains (restrict in production!)
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE etc.
    allow_headers=["*"],  # Allows all Header
)

app.mount("/api", api)


@app.get("/health")
def health():
    return {"success": True}
