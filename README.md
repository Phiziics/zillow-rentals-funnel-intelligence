# Zillow Rentals Funnel Intelligence

## Overview
This project builds an end-to-end machine learning system to predict whether a user session will result in a contact action for a rental listing. It simulates a real-world product funnel and delivers a production-ready solution with a trained model, API, and interactive UI.

---

## Business Problem
Rental platforms need to understand which listings and user sessions are most likely to convert into contact events.

This helps:
- Prioritize listings
- Optimize ranking and personalization
- Improve conversion rates

The goal is to predict **contact** using listing features, user context, and engagement signals.

---

## Dataset
This project uses a real rental listings dataset combined with simulated user interaction events to create a realistic funnel:

- impression  
- click  
- detail_view  
- save  
- contact  

Key features include:
- device type  
- traffic source  
- room type  
- city  
- price  
- demand score  
- availability  

---

## Project Architecture

**Data Layer**
- Raw listing data and simulated event funnel

**Model Layer**
- Feature engineering  
- Model training and evaluation  
- Threshold optimization  

**API Layer**
- FastAPI service for real-time predictions  

**UI Layer**
- Streamlit dashboard for interactive input and predictions  

**Deployment Layer**
- Dockerized services for reproducible execution  

---

## Feature Engineering

Key engineered features:

- Log-transformed price  
- Log-transformed demand score  
- Room type and city interaction  
- Relative price within city  
- Availability ratio  
- Listing attractiveness score  

These features improved model performance beyond baseline models.

---

## Model Development

Models evaluated:

- Logistic Regression  
- Random Forest  
- Gradient Boosting  
- Hist Gradient Boosting  
- Extra Trees  

**Final selected model:**
random_forest_engineered


**Key performance:**
- High recall  
- Strong PR AUC  
- Stable performance across metrics  

---

## Threshold Decision

Threshold tuning was performed to optimize model behavior.

Comparison:
- Default threshold: `0.50`
- Tuned threshold: `0.35`

**Result:**
- `0.35` gave only a marginal F1 improvement  
- `0.50` selected for production due to stability and simplicity  

---

## API

**Endpoint:**
POST /predict/contact


**Input:**
- device_type  
- traffic_source  
- room_type  
- city  
- price  
- demand_score  
- availability_365  
- click  
- detail_view  
- save  

**Output:**
- contact probability  
- predicted contact  
- threshold used  

---

## Streamlit App

Interactive UI to:
- Enter listing and session details  
- Call the API  
- Display predictions  

---

## Run Locally

Start API:

```bash
uvicorn app.api.main:app --reload

Start Streamlit:
streamlit run app/streamlit/app.py

docker compose -f docker/docker-compose.yml up --build