import streamlit as st
import pickle
import json
import numpy as np

# ----------------------------
# Load Model
# ----------------------------
with open("models/bangalore_house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# ----------------------------
# Load Feature Columns
# ----------------------------
with open("models/columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

# ----------------------------
# Extract Locations
# ----------------------------
locations = []

for col in data_columns:
    if col.startswith("location_"):
        locations.append(col.replace("location_", ""))

locations.sort()

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("About")

st.sidebar.info(
    """
    ## Bangalore House Price Prediction

    Predict the price of houses in Bangalore using a Machine Learning model.

    **Model Used:**
    - Linear Regression

    **Technologies:**
    - Python
    - Streamlit
    - Scikit-learn
    - Pandas
    - NumPy
    """
)

# ----------------------------
# Main Title
# ----------------------------
st.title("🏠 Bangalore House Price Prediction")

st.markdown(
    """
    Predict the estimated price of a house in Bangalore using a trained
    Machine Learning model.

    Enter the property details below and click **Predict Price**.
    """
)

# ----------------------------
# Input Layout
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    total_sqft = st.number_input(
        "Total Square Feet",
        min_value=300.0,
        max_value=10000.0,
        value=1200.0
    )

    bath = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=20,
        value=2
    )

    area_type = st.selectbox(
        "Area Type",
        (
            "Built-up Area",
            "Carpet Area",
            "Plot Area",
            "Super built-up Area"
        )
    )

with col2:
    bhk = st.number_input(
        "BHK",
        min_value=1,
        max_value=20,
        value=2
    )

    balcony = st.number_input(
        "Balconies",
        min_value=0,
        max_value=10,
        value=1
    )

    location = st.selectbox(
        "Location",
        locations
    )

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict Price"):

    # Input Validation
    if bhk > total_sqft / 150:
        st.error("Please enter a realistic combination of Total Sqft and BHK.")
    else:

        sqft_per_bhk = total_sqft / bhk

        x = np.zeros(len(data_columns))

        # Numerical Features
        x[0] = total_sqft
        x[1] = bath
        x[2] = balcony
        x[3] = bhk
        x[4] = sqft_per_bhk

        # Area Type Encoding
        if area_type == "Carpet Area":
            x[data_columns.index("area_type_Carpet  Area")] = 1

        elif area_type == "Plot Area":
            x[data_columns.index("area_type_Plot  Area")] = 1

        elif area_type == "Super built-up Area":
            x[data_columns.index("area_type_Super built-up  Area")] = 1

        # Built-up Area is the reference category
        # so no need to set any column.

        # Location Encoding
        location_column = "location_" + location

        if location_column in data_columns:
            x[data_columns.index(location_column)] = 1

        prediction = model.predict([x])[0]

        st.success("Prediction Successful!")

        st.subheader("🏠 Estimated House Price")

        st.metric(
            label="Predicted Price",
            value=f"₹ {prediction:.2f} Lakhs"
        )

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Developed by Ankush Sharma | Bangalore House Price Prediction")