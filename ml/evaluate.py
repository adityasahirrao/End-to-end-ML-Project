from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

def evaluate_model(model, X_test, y_test):
    print("evaluate.py --> evaluate_model")
    predictions = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)
    print(f"RMSE: {rmse}")
    print(f"R2 Score: {r2}")

    # ✅ Plot Predicted vs Actual
    plt.figure(figsize=(8,6))
    plt.scatter(y_test, predictions, alpha=0.5, color="blue")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Predicted vs Actual House Prices")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("ml/evaluation_plot.png")  # ✅ Save plot image
    plt.close()

    return rmse, r2
