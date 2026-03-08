from dotenv import load_dotenv
load_dotenv()  # ← THIS must be BEFORE everything else

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from routes import analyze, questions, analytics

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze.router)
app.include_router(questions.router)
app.include_router(analytics.router)

@app.get("/")
def home():
    return {"message": "Cognivise backend running"}

@app.get("/app")
def serve_frontend():
    return FileResponse("frontend/cognivise.html")
