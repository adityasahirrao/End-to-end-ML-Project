import pandas as pd
from ml.pipeline import preprocess_data
from mlflow import sklearn as mlflow_sklearn
import mlflow
import joblib
import os
from sklearn.linear_model import LinearRegression
from ml.evaluate import evaluate_model  # ✅ Add this at the top

def load_data(path="data/housing.csv"):
    print("file train.py --> load_data")
    """Load dataset from CSV."""
    return pd.read_csv(path)

def select_model():
    print("file train.py --> select_model")
    """Select regression model."""
    return LinearRegression()

def save_model(model, imputer, scaler):
    print("file train.py --> save_model")
    """Save model and preprocessing objects."""
    os.makedirs("app/saved_models", exist_ok=True)
    joblib.dump(model, "app/saved_models/house_price_model.pkl")
    joblib.dump(imputer, "app/saved_models/imputer.pkl")
    joblib.dump(scaler, "app/saved_models/scaler.pkl")

def train_model():
    print("file train.py --> train_model")
    df = load_data()
    X_train, X_test, y_train, y_test, imputer, scaler = preprocess_data(df)

    model = select_model()
    model.fit(X_train, y_train)

    # ✅ Evaluate model
    rmse, r2 = evaluate_model(model, X_test, y_test)

    mlflow.set_tracking_uri("file:./mlflow")
    mlflow.set_experiment("HousePricePrediction")

    with mlflow.start_run():
        mlflow_sklearn.log_model(model, "model")
        mlflow.log_params(model.get_params())
        
        # ✅ Log evaluation metrics
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2_score", r2)

    save_model(model, imputer, scaler)

if __name__ == "__main__":
    train_model()