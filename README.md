<<<<<<< HEAD
=======
# 🏡 End-to-End House Price Prediction ML Project

Welcome to the **House Price Prediction** project — a complete **End-to-End ML pipeline** built using Python, Docker, FastAPI, MLflow and AWS ECS. This project demonstrates how to take a machine learning model from training to deployment in production! 🚀

## 📌 Project Highlights

- ✅ **Data Preprocessing & Feature Engineering**
- 📊 **Model Training & Evaluation**
- 🧪 **MLflow Experiment Tracking**
- ⚙️ **FastAPI Model Serving**
- 🐳 **Dockerized App**
- 🔁 **CI/CD with GitHub Actions**
- ☁️ **Deployed on AWS ECS (Fargate/EC2)**


## 🔧 Tech Stack

| Layer              | Tool/Framework     |
|--------------------|--------------------|
| Programming        | Python 🐍         |
| Web Framework      | FastAPI ⚡        |
| Experiment Tracking| MLflow 📊         |
| Containerization   | Docker 🐳         |
| CI/CD              | GitHub Actions 🔁 |
| Deployment         | AWS ECS ☁️        |


## 📂 Project FIle Structure

```
📦 End-to-end-ML-Project/
├── app/
│   ├── main.py
│   ├── test_main.py
│   └── saved_models/
│       └── house_price_model.pkl
│       └── imputer.pkl
│       └── scaler.pkl
├── data/
│   └── housing.csv
├── ml/
│   ├── pipeline.py
│   ├── train.py
│   └── evaluate.py
├── Dockerfile
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci-cd.yaml
├── mlflow/
│   └── tracking_uri.txt
└── README.md

```

## 🛠️ Setup & Execution Guide

### 🧠 1. Train the Model

```bash
# Option 1: Direct run
set PYTHONPATH=.
python ml/train.py

# Option 2: Run as module
python -m ml.train
```


### ⚡ 2. Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

📍 API Live at: `http://127.0.0.1:8000`



### 📊 3. Track Experiments with MLflow

```bash
mlflow ui --backend-store-uri file:./mlflow
```

📍 MLflow UI: `http://127.0.0.1:5000`



### 🧪 4. Run Unit Tests

```bash
set PYTHONPATH=.
pytest app/test_main.py
```

**Test Cases Covered:**

- `POST /predict`: Single prediction  
- `POST /batch_predict`: Batch prediction  


## 📬 API Endpoints (via FastAPI)

| Method | Endpoint           | Description                         |
|--------|--------------------|-------------------------------------|
| POST   | `/predict`         | Predict house price for single row |
| POST   | `/batch_predict`   | Predict prices for multiple rows   |
| GET    | `/docs`            | Swagger UI to test API             |

---

## 📦 Sample Requests

### 🔹 `/predict`

```json
{
  "features": [-122.23, 37.88, 41, 880, 129, 322, 126, 8.3252]
}
```

### 🔹 `/batch_predict`

```json
{
  "batch_features": [
    [-122.23, 37.88, 41, 880, 129, 322, 126, 8.3252],
    [-122.22, 37.86, 21, 7099, 1106, 2401, 1138, 8.3014]
  ]
}
```


### 🐳 5. Build & Run Docker Image

```bash
docker build -t house-price-app .
docker run -p 8000:80 house-price-app
```

📍 App available at: `http://localhost:8000`



## 🔁 CI/CD Pipeline (GitHub Actions → AWS ECS)

📁 `.github/workflows/ci-cd.yaml` automates:

- Code checkout
- Python setup
- Install dependencies
- Run tests
- Build Docker image
- Deploy to AWS ECS

### 🔐 Required GitHub Secrets

| Secret Name              | Description                      |
|--------------------------|----------------------------------|
| `AWS_ACCESS_KEY_ID`      | Your AWS access key              |
| `AWS_SECRET_ACCESS_KEY`  | Your AWS secret key              |
| `AWS_REGION`             | AWS region (e.g., `us-east-1`)  |
| `ECS_CLUSTER`            | Name of your ECS cluster         |
| `ECS_SERVICE`            | ECS service name                 |
| `ECS_TASK_DEFINITION`    | ECS task definition name         |
| `CONTAINER_NAME`         | Docker container name            |

📌 **Trigger:** Push to `main` branch → deploys to ECS automatically ✅





>>>>>>> 80bdae55ecfaf16741a9dd9c5c38219a4dee99b6

