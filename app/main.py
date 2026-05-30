from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(
    title="My FastAPI App",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"status": "healthy", "platform": "Klade"}


app.include_router(api_router)

