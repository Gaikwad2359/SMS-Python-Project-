from fastapi import APIRouter, HTTPException, Depends
import subprocess
from app.routes.auth import oauth2_scheme

router = APIRouter()

@router.post("/start_session")
async def start_session(country_operator_id: str, token: str = Depends(oauth2_scheme)):
    try:
        subprocess.Popen(['screen', '-dm', 'python3', f'{country_operator_id}.py'])
        return {"status": "Session started"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/stop_session")
async def stop_session(country_operator_id: str, token: str = Depends(oauth2_scheme)):
    try:
        subprocess.run(['screen', '-X', '-S', f"{country_operator_id}", 'quit'])
        return {"status": "Session stopped"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
