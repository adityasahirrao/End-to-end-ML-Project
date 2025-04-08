from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from typing import List

app = FastAPI(
    title="House Price Prediction API",
    description="Predict house prices using a pre-trained ML model. Supports single and batch inputs.",
    version="1.0"
)

model = joblib.load("app/saved_models/house_price_model.pkl")
imputer = joblib.load("app/saved_models/imputer.pkl")
scaler = joblib.load("app/saved_models/scaler.pkl")

class HouseFeatures(BaseModel):
    features: List[float]

class HouseFeaturesBatch(BaseModel):
    batch_features: List[List[float]]

@app.get("/")
def read_root():
    return {"message": "Welcome to the House Price Prediction API : latest"}


@app.get("/health")
def health_check():
    """Health check endpoint for load balancer"""
    return {"status": "ok"}

@app.post("/predict")
def predict(data: HouseFeatures):
    raw = np.array(data.features).reshape(1, -1)
    raw_imputed = imputer.transform(raw)
    raw_scaled = scaler.transform(raw_imputed)
    prediction = model.predict(raw_scaled)
    return {"prediction": prediction[0]}

@app.post("/predict_batch")
def predict_batch(data: HouseFeaturesBatch):
    raw = np.array(data.batch_features)
    raw_imputed = imputer.transform(raw)
    raw_scaled = scaler.transform(raw_imputed)
    prediction = model.predict(raw_scaled)
    return {"predictions": prediction.tolist()}
