import joblib
import numpy as np
import pandas as pd
import xgboost as xgb

rf_model = joblib.load("rf_model.pkl")
lr_model = joblib.load("lr_model.pkl")
meta_model = joblib.load("meta_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

booster = xgb.Booster()
booster.load_model("booster_only.json")

NUMERIC_COLUMNS = [
    "age",
    "website_visits",
    "time_spent_on_website",
    "page_views_per_visit"
]


def preprocess_input(user_input):
    df = pd.DataFrame([user_input])

    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[feature_columns].copy()
    df[NUMERIC_COLUMNS] = scaler.transform(df[NUMERIC_COLUMNS])

    return df


def base_model_probabilities(df):
    rf_prob = rf_model.predict_proba(df)[:, 1][0]

    dmatrix = xgb.DMatrix(df)
    xgb_prob = float(booster.predict(dmatrix)[0])

    lr_prob = lr_model.predict_proba(df)[:, 1][0]

    return np.array([[rf_prob, xgb_prob, lr_prob]])


def load_models():
    return {
        "rf": rf_model,
        "lr": lr_model,
        "meta": meta_model,
        "booster": booster,
        "scaler": scaler,
        "feature_columns": feature_columns
    }


def predict_lead(user_input):
    df = preprocess_input(user_input)

    meta_features = base_model_probabilities(df)

    probability = float(
        meta_model.predict_proba(meta_features)[0][1]
    )

    prediction = int(probability >= 0.40)

    confidence = round(
        max(probability, 1 - probability) * 100,
        2
    )

    return {
        "prediction": prediction,
        "probability": round(probability * 100, 2),
        "confidence": confidence,
        "label": "Converted" if prediction == 1 else "Not Converted"
    }


if __name__ == "__main__":
    sample = {
        "age": 30,
        "website_visits": 5,
        "time_spent_on_website": 450,
        "page_views_per_visit": 4,
        "current_occupation_Student": 0,
        "current_occupation_Unemployed": 0,
        "first_interaction_Website": 1,
        "profile_completed_Low": 0,
        "profile_completed_Medium": 1,
        "last_activity_Phone Activity": 0,
        "last_activity_Website Activity": 1,
        "print_media_type1_Yes": 0,
        "print_media_type2_Yes": 0,
        "digital_media_Yes": 1,
        "educational_channels_Yes": 0,
        "referral_Yes": 0
    }

    print(predict_lead(sample))