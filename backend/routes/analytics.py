from fastapi import APIRouter
from services.analytics_service import analytics_summary

router = APIRouter()

@router.get("/api/analytics/dashboard")
def analytics_dashboard():
    return analytics_summary()
