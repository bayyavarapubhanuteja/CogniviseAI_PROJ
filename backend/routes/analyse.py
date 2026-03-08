from fastapi import APIRouter
from pydantic import BaseModel
from services.ai_services import analyze_reasoning
from services.database_service import save_session
from datetime import date

router = APIRouter()

class AnalyzeRequest(BaseModel):
    topic: str
    first_attempt: str
    final_answer: str
    user_id: str = "user_001"

@router.post("/api/analyze")
def analyze(data: AnalyzeRequest):
    result = analyze_reasoning(data.topic, data.first_attempt, data.final_answer)

    # Auto-save session after every analysis
    save_session({
        "user_id":        data.user_id,
        "topic":          data.topic,
        "thinking_pattern": "Analytical",   # overwrite below if AI returns it
        "confusion_type": "General",
        "first_attempt":  50,
        "final_attempt":  75,
        "correct_answer": 100,
        "date":           str(date.today())
    })

    return {"analysis": result}
