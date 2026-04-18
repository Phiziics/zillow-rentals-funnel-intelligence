import json
import joblib
import numpy as np
import pandas as pd


MODEL_PATH = "artifacts/final_model.joblib"
CITY_MAP_PATH = "artifacts/city_median_price_log_map.json"
THRESHOLD = 0.50

model = joblib.load(MODEL_PATH)

with open(CITY_MAP_PATH, "r") as f:
    city_median_price_log_map = json.load(f)


def build_features(input_df: pd.DataFrame) -> pd.DataFrame:
    input_df = input_df.copy()

    input_df["demand_score_log"] = np.log1p(input_df["demand_score"])

    input_df["room_city"] = (
        input_df["room_type"].astype(str) + "_" + input_df["city"].astype(str)
    )

    input_df["city_median_price_log"] = input_df["city"].map(city_median_price_log_map)

    global_median_price_log = float(np.median(list(city_median_price_log_map.values())))
    input_df["city_median_price_log"] = input_df["city_median_price_log"].fillna(global_median_price_log)

    input_df["price_log_diff_from_city"] = (
        input_df["price_log"] - input_df["city_median_price_log"]
    )

    input_df["relative_price_bucket"] = pd.cut(
        input_df["price_log_diff_from_city"],
        bins=[-10, -0.25, 0.25, 10],
        labels=["below_city", "near_city", "above_city"]
    )

    input_df["relative_price_bucket"] = input_df["relative_price_bucket"].astype(str)

    input_df["listing_attractiveness_score"] = (
        0.4 * input_df["demand_score_log"]
        + 0.3 * (1 / (1 + np.exp(input_df["price_log_diff_from_city"])))
        + 0.3 * input_df["availability_ratio"]
    )

    final_columns = [
        "device_type",
        "traffic_source",
        "room_type",
        "city",
        "price_log",
        "demand_score",
        "availability_ratio",
        "click",
        "detail_view",
        "save",
        "demand_score_log",
        "room_city",
        "city_median_price_log",
        "price_log_diff_from_city",
        "relative_price_bucket",
        "listing_attractiveness_score"
    ]

    return input_df[final_columns]


def predict_contact(data: dict) -> dict:
    input_df = pd.DataFrame([data])
    feature_df = build_features(input_df)

    probability = model.predict_proba(feature_df)[:, 1][0]
    prediction = int(probability >= THRESHOLD)

    return {
        "contact_probability": float(probability),
        "predicted_contact": prediction,
        "threshold_used": THRESHOLD
    }