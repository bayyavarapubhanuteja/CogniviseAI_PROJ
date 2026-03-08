from fastapi import APIRouter
from services.ai_services import generate_questions

router = APIRouter()

@router.get("/api/questions")
def questions(topic: str, difficulty: str, qtype: str = "open"):
    result = generate_questions(topic, difficulty, qtype)
    return {"questions": result}
