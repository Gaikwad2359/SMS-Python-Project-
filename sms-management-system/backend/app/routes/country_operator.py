from fastapi import APIRouter, HTTPException, Depends
from app.services.sms_service import add_country_operator, remove_country_operator, update_country_operator
from app.routes.auth import oauth2_scheme

router = APIRouter()

@router.post("/add_pair")
async def add_pair(country: str, operator: str, high_priority: bool = False, token: str = Depends(oauth2_scheme)):
    add_country_operator(country, operator, high_priority)
    return {"status": "Country-operator pair added"}

@router.delete("/remove_pair")
async def remove_pair(pair_id: str, token: str = Depends(oauth2_scheme)):
    remove_country_operator(pair_id)
    return {"status": "Country-operator pair removed"}

@router.put("/update_pair")
async def update_pair(pair_id: str, success_rate: float, token: str = Depends(oauth2_scheme)):
    update_country_operator(pair_id, success_rate)
    return {"status": "Country-operator pair updated"}
