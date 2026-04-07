from fastapi import FastAPI

app = FastAPI(title="Zillow Rentals Funnel Intelligence API")


@app.get("/")
def root() -> dict:
    return {"message": "Zillow Rentals Funnel Intelligence API is running"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}