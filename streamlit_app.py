# YOu can run locally using the command : streamlit run streamlit_app.py
# Also, replace the BACKEND_URL with your aws public url.

import streamlit as st
import pandas as pd
import requests
from io import StringIO
from PIL import Image

# Set page config
st.set_page_config(
    page_title="🏡 House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load and display logo
logo = Image.open("logo.png") if "logo.png" in locals() or "logo.png" in globals() else None
if logo:
    st.sidebar.image(logo, use_column_width=True)

# Sidebar options
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to", ["Single Prediction", "Batch Prediction"])

# Dark mode toggle using custom CSS
if st.sidebar.checkbox("🌙 Enable Dark Mode"):
    dark_css = """
    <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stApp {
            background-color: #0e1117;
        }
    </style>
    """
    st.markdown(dark_css, unsafe_allow_html=True)

st.title("🏡 House Price Prediction")

BACKEND_URL = "http://<Public-url>"
HEADERS = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income']

if page == "Single Prediction":
    st.subheader("🔍 Predict House Price (Single Input)")

    input_data = []
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        input_data.append(st.slider("📍 Longitude", -125.0, -113.0, -120.0))
        input_data.append(st.slider("🌍 Latitude", 32.0, 42.0, 36.0))

    with col2:
        input_data.append(st.slider("🏠 Housing Median Age", 1, 52, 25))
        input_data.append(st.slider("🏘️ Total Rooms", 1, 50000, 2000))

    with col3:
        input_data.append(st.slider("🛏️ Total Bedrooms", 1, 10000, 500))
        input_data.append(st.slider("👨‍👩‍👧‍👦 Population", 1, 50000, 1000))

    with col4:
        input_data.append(st.slider("🏡 Households", 1, 10000, 800))
        input_data.append(st.slider("💰 Median Income", 0.0, 15.0, 4.0))

    if st.button("Predict Price"):
        with st.spinner("⏳ Predicting price..."):
            try:
                response = requests.post(f"{BACKEND_URL}/predict", json={"features": input_data})
                if response.status_code == 200:
                    prediction = response.json()["prediction"]
                    st.success("🎯 Prediction Complete")
                    st.markdown(f"### 💸 **Estimated Price: ${prediction:,.2f}**")
                else:
                    st.error("Prediction failed. Try again later.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

elif page == "Batch Prediction":
    st.subheader("📁 Batch Prediction via CSV")
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file, header=None)
            df.columns = HEADERS
            st.write("🔍 Preview of Input Data:")
            st.dataframe(df.head())

            if st.button("Predict Batch Prices"):
                with st.spinner("⏳ Predicting for batch..."):
                    response = requests.post(f"{BACKEND_URL}/predict_batch", json={"batch_features": df.values.tolist()})
                    if response.status_code == 200:
                        predictions = response.json()["predictions"]
                        result_df = df.copy()
                        result_df["Predicted Price"] = predictions
                        st.success("🎯 Batch Prediction Complete")
                        st.dataframe(result_df)
                    else:
                        st.error("Batch prediction failed.")

        except Exception as e:
            st.error(f"Error reading file: {e}")

# Footer
st.markdown("---")
st.markdown("📦 Powered by **FastAPI + Docker + ECS + Streamlit** 🚀")
st.markdown("🔗 [View Source Code on GitHub](https://github.com/adityasahirrao/End-to-end-ML-Project)")
