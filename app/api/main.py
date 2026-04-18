from fastapi import FastAPI
from app.api.schemas import PredictionRequest, PredictionResponse
from app.api.model_service import predict_contact

app = FastAPI(title="Zillow Rentals Funnel Intelligence API")


@app.get("/")
def root() -> dict:
    return {"message": "Zillow Rentals Funnel Intelligence API is running"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/predict/contact", response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    result = predict_contact(request.model_dump())
    return PredictionResponse(**result)