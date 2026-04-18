from pydantic import BaseModel


class PredictionRequest(BaseModel):
    device_type: str
    traffic_source: str
    room_type: str
    city: str
    price_log: float
    demand_score: float
    availability_ratio: float
    click: int
    detail_view: int
    save: int


class PredictionResponse(BaseModel):
    contact_probability: float
    predicted_contact: int
    threshold_used: float