import os
import subprocess
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.authRoute import router as auth_router
from routes.repoRoute import router as repo_router
from routes.org import router as org
from routes.allRepos import router as arepo_router
from routes.scheduleRoute import router as schedule_router
from routes.chatRoute import router as chat_router

load_dotenv()

app = FastAPI()

allowed_origin = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix = "/auth")
app.include_router(repo_router, prefix = "/repo")
app.include_router(org, prefix = "/org")
app.include_router(arepo_router, prefix = "/repo")
app.include_router(schedule_router, prefix = "/schedule")
app.include_router(chat_router, prefix = "/api")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)