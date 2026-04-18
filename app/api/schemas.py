from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    device_type: str = Field(
        ...,
        json_schema_extra={"example": "mobile"}
    )
    traffic_source: str = Field(
        ...,
        json_schema_extra={"example": "organic"}
    )
    room_type: str = Field(
        ...,
        json_schema_extra={"example": "Entire home/apt"}
    )
    city: str = Field(
        ...,
        json_schema_extra={"example": "Manhattan"}
    )
    price: float = Field(
        ...,
        gt=0,
        json_schema_extra={"example": 150.0}
    )
    demand_score: float = Field(
        ...,
        ge=0,
        json_schema_extra={"example": 1.43}
    )
    availability_365: int = Field(
        ...,
        ge=0,
        le=365,
        json_schema_extra={"example": 90}
    )
    click: int = Field(
        ...,
        ge=0,
        le=1,
        json_schema_extra={"example": 1}
    )
    detail_view: int = Field(
        ...,
        ge=0,
        le=1,
        json_schema_extra={"example": 1}
    )
    save: int = Field(
        ...,
        ge=0,
        le=1,
        json_schema_extra={"example": 0}
    )


class PredictionResponse(BaseModel):
    contact_probability: float
    predicted_contact: int
    threshold_used: float