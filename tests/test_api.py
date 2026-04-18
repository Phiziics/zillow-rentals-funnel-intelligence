from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict_contact():
    payload = {
        "device_type": "mobile",
        "traffic_source": "organic",
        "room_type": "Entire home/apt",
        "city": "Manhattan",
        "price": 150.0,
        "demand_score": 1.43,
        "availability_365": 90,
        "click": 1,
        "detail_view": 1,
        "save": 0
    }

    response = client.post("/predict/contact", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert "contact_probability" in body
    assert "predicted_contact" in body
    assert "threshold_used" in body