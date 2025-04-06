import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
#------------------------------------------------------------------

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prediction():
    print("test_main.py --> test_prediction")
    response = client.post("/predict", json={"features": [-122.23, 37.88, 41, 880, 129, 322, 126, 8.3252]})  # Actual Output : 452600
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_batch_prediction():
    print("test_main.py --> test_batch_prediction")
    batch_data = {
        "batch_features": [
            [-122.23, 37.88, 41, 880, 129, 322, 126, 8.3252],       # Actual Output : 452600
            [-122.22, 37.86, 21, 7099, 1106, 2401, 1138, 8.3014]  # Actual Output : 358500
        ]
    }
    response = client.post("/predict_batch", json=batch_data)
    assert response.status_code == 200
    assert "predictions" in response.json()
    assert isinstance(response.json()["predictions"], list)
