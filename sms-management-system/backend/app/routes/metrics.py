from fastapi import APIRouter, Depends
from app.services.monitoring import get_sms_metrics
from app.routes.auth import oauth2_scheme

router = APIRouter()

@router.get("/metrics")
async def get_metrics(token: str = Depends(oauth2_scheme)):
    return get_sms_metrics()
