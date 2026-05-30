from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "FastAPI running on Klade!"}


@router.get("/health")
def health():
    return {"status": "ok"}
