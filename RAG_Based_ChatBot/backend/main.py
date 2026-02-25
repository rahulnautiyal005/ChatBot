from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.rag.pipeline import rag_pipeline

app = FastAPI(
    title="UK Global Talent Visa RAG API",
    version="1.0.0"
)

# Allow frontend connection (important later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------- Request Schema --------
class ChatRequest(BaseModel):
    message: str


# -------- Health Check --------
@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "UK Global Talent Visa RAG API"
    }


# -------- Chat Endpoint --------
@app.post("/chat")
def chat(request: ChatRequest):
    response = rag_pipeline(request.message)

    return {
        "question": request.message,
        "answer": response
    }