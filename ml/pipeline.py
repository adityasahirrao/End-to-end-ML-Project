from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    print("pipeline.py --> preprocess_data")
    df = df.dropna(subset=["median_house_value"])
    num_df = df.select_dtypes(include=['int64', 'float64']).drop("median_house_value", axis=1)
    y = df["median_house_value"]

    imputer = SimpleImputer(strategy="median")
    X_imputed = imputer.fit_transform(num_df)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test, imputer, scaler