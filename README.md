# Zillow Rentals Funnel Intelligence

## Introduction
This project is an end-to-end product data science and machine learning system inspired by Zillow's rental marketplace use case. The goal is to analyze renter behavior across the shopping funnel and predict which listing impressions or sessions are most likely to lead to a contact event.

## Problem
Rental platforms need to understand where users drop off in the funnel and which factors increase the probability of deeper engagement such as saving a listing or contacting a landlord or agent.

## Project Goal
Build a system that tracks and analyzes the renter funnel:

search → impression → click → detail_view → save → contact

and predicts contact likelihood using listing and session-level features.

## Project Structure
- `config/` environment configs
- `data/` raw, preprocessed, features, predictions
- `entrypoint/` train and inference entry scripts
- `notebooks/` EDA, experimentation, modeling, recommendations
- `src/` pipelines, analytics, modeling
- `app/api/` FastAPI backend
- `app/streamlit/` dashboard app
- `tests/` unit tests
- `docker/` containerization files
- `environment/` environment configs
- `artifacts/` metadata and model outputs

## Planned Stack
- Python
- pandas
- scikit-learn
- FastAPI
- Streamlit
- Jupyter

## Status
Project setup in progress.