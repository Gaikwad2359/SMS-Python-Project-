from fastapi import FastAPI
from backend.app import auth, sms_control, metrics, country_operator  

app = FastAPI()

# Include routers for different functionalities
app.include_router(auth.router)
app.include_router(sms_control.router)
app.include_router(metrics.router)
app.include_router(country_operator.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the SMS Management System"}
