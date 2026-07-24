import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
import plotly.express as px
import plotly.graph_objects as go


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Bangalore House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main{
    background-color:#F8FAFC;
}

.block-container{
    padding-top:2rem;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.08);
}

.stButton>button{
    width:100%;
    height:50px;
    border:none;
    border-radius:10px;
    background:#2563EB;
    color:white;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1E40AF;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    padding:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,.08);
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# LOAD MODEL
# =====================================================

with open("models/bangalore_house_price_model.pkl","rb") as f:
    model = pickle.load(f)


# =====================================================
# LOAD COLUMNS
# =====================================================

with open("models/columns.json","r") as f:
    data_columns = json.load(f)["data_columns"]


# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv(
    "data/Bengaluru_House_Data.csv"
)


# =====================================================
# DATA CLEANING
# =====================================================

def convert_sqft_to_num(x):

    try:
        return float(x)

    except:

        try:

            values = str(x).split("-")

            if len(values) == 2:

                return (
                    float(values[0])
                    +
                    float(values[1])
                ) / 2

            return None

        except:

            return None



df["total_sqft"] = df["total_sqft"].apply(
    convert_sqft_to_num
)


df["price"] = pd.to_numeric(
    df["price"],
    errors="coerce"
)


df["bath"] = pd.to_numeric(
    df["bath"],
    errors="coerce"
)


df["balcony"] = pd.to_numeric(
    df["balcony"],
    errors="coerce"
)


# Create BHK column

df["bhk"] = (
    df["size"]
    .str.extract("(\d+)")
)


df["bhk"] = pd.to_numeric(
    df["bhk"],
    errors="coerce"
)


df = df.dropna(
    subset=[
        "total_sqft",
        "price",
        "bhk"
    ]
)


# =====================================================
# LOCATION LIST
# =====================================================

locations = []

for col in data_columns:

    if col.startswith("location_"):

        locations.append(
            col.replace("location_","")
        )


locations = sorted(locations)


# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#2563EB,#1D4ED8,#0EA5E9);
padding:30px;
border-radius:15px;
text-align:center;
margin-bottom:20px;">

<h1 style="color:white;">
🏠 Bangalore House Price Prediction Dashboard
</h1>

<p style="color:white;font-size:18px;">
Predict Bangalore House Prices using Machine Learning
</p>

</div>
""", unsafe_allow_html=True)


# =====================================================
# KPI CARDS
# =====================================================

total_houses = len(df)

total_locations = df["location"].nunique()

average_price = round(
    df["price"].mean(),
    2
)

average_sqft = round(
    df["total_sqft"].mean(),
    2
)


k1,k2,k3,k4 = st.columns(4)


with k1:
    st.metric(
        "🏘 Houses",
        total_houses
    )


with k2:
    st.metric(
        "📍 Locations",
        total_locations
    )


with k3:
    st.metric(
        "💰 Avg Price",
        f"₹ {average_price} L"
    )


with k4:
    st.metric(
        "📐 Avg Sqft",
        average_sqft
    )


st.markdown("---")
# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.header("🏠 Property Details")


total_sqft = st.sidebar.number_input(
    "Total Square Feet",
    min_value=300.0,
    max_value=10000.0,
    value=1200.0
)


bhk = st.sidebar.number_input(
    "BHK",
    min_value=1,
    max_value=20,
    value=2
)


bath = st.sidebar.number_input(
    "Bathrooms",
    min_value=1,
    max_value=20,
    value=2
)


balcony = st.sidebar.number_input(
    "Balconies",
    min_value=0,
    max_value=10,
    value=1
)


area_type = st.sidebar.selectbox(
    "Area Type",
    (
        "Built-up Area",
        "Carpet Area",
        "Plot Area",
        "Super built-up Area"
    )
)


location = st.sidebar.selectbox(
    "Location",
    locations
)


predict_btn = st.sidebar.button(
    "🔮 Predict Price"
)


st.sidebar.markdown("---")


st.sidebar.info(
"""
### ℹ About

This application predicts Bangalore house prices using a Machine Learning model.

**Tech Stack**

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Plotly
"""
)


# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3 = st.tabs(
[
    "🏠 Prediction",
    "📊 Dataset Insights",
    "ℹ About Project"
]
)


# =====================================================
# PREDICTION TAB
# =====================================================

with tab1:


    left_col, right_col = st.columns([2,1])


    with left_col:

        st.subheader(
            "🏡 Predict House Price"
        )

        st.write(
            "Enter the property details from the sidebar and click Predict Price."
        )


    with right_col:

        st.info(
            f"""
            **Selected Location**

            📍 {location}
            """
        )


    st.markdown("---")


    if predict_btn:


        sqft_per_bhk = total_sqft / bhk


        x = np.zeros(
            len(data_columns)
        )


        # Numerical Features

        x[0] = total_sqft
        x[1] = bath
        x[2] = balcony
        x[3] = bhk
        x[4] = sqft_per_bhk



        # Area Type Encoding

        if area_type == "Carpet Area":

            if "area_type_Carpet  Area" in data_columns:

                x[
                    data_columns.index(
                        "area_type_Carpet  Area"
                    )
                ] = 1


        elif area_type == "Plot Area":

            if "area_type_Plot  Area" in data_columns:

                x[
                    data_columns.index(
                        "area_type_Plot  Area"
                    )
                ] = 1


        elif area_type == "Super built-up Area":

            if "area_type_Super built-up  Area" in data_columns:

                x[
                    data_columns.index(
                        "area_type_Super built-up  Area"
                    )
                ] = 1



        # Location Encoding

        location_column = (
            "location_" + location
        )


        if location_column in data_columns:

            x[
                data_columns.index(
                    location_column
                )
            ] = 1



        prediction = model.predict(
            [x]
        )[0]


        st.success(
            "Prediction Successful ✅"
        )


        st.markdown("---")


        c1,c2 = st.columns(
            [1.3,1]
        )


        with c1:

            st.markdown(
                "## 💰 Estimated House Price"
            )


            st.metric(
                "Predicted Price",
                f"₹ {prediction:.2f} Lakhs"
            )


            if prediction < 50:

                st.success(
                    "🟢 Budget Friendly Property"
                )

            elif prediction < 100:

                st.warning(
                    "🟡 Mid Range Property"
                )

            else:

                st.error(
                    "🔴 Premium Property"
                )


        with c2:


            st.markdown(
                "## 📋 Property Summary"
            )


            st.write(
                f"**📍 Location :** {location}"
            )

            st.write(
                f"**🏠 Area Type :** {area_type}"
            )

            st.write(
                f"**📐 Total Sqft :** {total_sqft}"
            )

            st.write(
                f"**🛏 BHK :** {bhk}"
            )

            st.write(
                f"**🚿 Bathrooms :** {bath}"
            )

            st.write(
                f"**🌇 Balconies :** {balcony}"
            )


        st.markdown("---")


        st.subheader(
            "📊 Location Statistics"
        )


        location_df = df[
            df["location"] == location
        ]


        if len(location_df) > 0:


            l1,l2,l3 = st.columns(3)


            with l1:

                st.metric(
                    "Average Price",
                    f"₹ {location_df['price'].mean():.2f} L"
                )


            with l2:

                st.metric(
                    "Average Sqft",
                    round(
                        location_df["total_sqft"].mean(),
                        0
                    )
                )


            with l3:

                st.metric(
                    "Average BHK",
                    round(
                        location_df["bhk"].mean(),
                        1
                    )
                )


        st.markdown("---")


        st.subheader(
            "🏘 Similar Properties"
        )


        similar = df[
            (df["location"] == location)
            &
            (abs(df["bhk"] - bhk) <= 1)
        ]


        if len(similar) > 0:


            st.dataframe(

                similar[
                    [
                        "location",
                        "total_sqft",
                        "bhk",
                        "bath",
                        "price"
                    ]
                ].head(10),

                use_container_width=True

            )


        else:

            st.info(
                "No similar properties found."
            )
            # =====================================================
# DATASET INSIGHTS
# =====================================================

with tab2:

    st.subheader(
        "📊 Dataset Insights"
    )


    c1,c2 = st.columns(2)


    # -----------------------------
    # Price Distribution
    # -----------------------------

    with c1:


        fig = px.histogram(
            df,
            x="price",
            nbins=40,
            title="House Price Distribution"
        )


        fig.update_layout(
            template="plotly_white",
            xaxis_title="Price (Lakhs)",
            yaxis_title="Number of Houses"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )



    # -----------------------------
    # Scatter Plot
    # -----------------------------

    with c2:


        scatter_df = df[
            [
                "total_sqft",
                "price",
                "bhk",
                "bath",
                "location"
            ]
        ].dropna()



        scatter_df = scatter_df[
            (scatter_df["total_sqft"] < 6000)
            &
            (scatter_df["price"] < 500)
        ]



        fig2 = px.scatter(

            scatter_df,

            x="total_sqft",

            y="price",

            color="bhk",

            size="bath",

            hover_name="location",

            title="Square Feet vs Price"

        )


        fig2.update_layout(

            template="plotly_white",

            xaxis_title="Square Feet",

            yaxis_title="Price (Lakhs)"

        )


        st.plotly_chart(

            fig2,

            use_container_width=True

        )



    st.markdown("---")



    c3,c4 = st.columns(2)



    # -----------------------------
    # Area Type Distribution
    # -----------------------------

    with c3:


        area_df = (
            df["area_type"]
            .value_counts()
            .reset_index()
        )


        area_df.columns = [
            "Area Type",
            "Count"
        ]



        fig3 = px.pie(

            area_df,

            values="Count",

            names="Area Type",

            hole=0.45,

            title="Area Type Distribution"

        )


        st.plotly_chart(

            fig3,

            use_container_width=True

        )



    # -----------------------------
    # Top Locations
    # -----------------------------

    with c4:


        top_locations = (

            df["location"]
            .value_counts()
            .head(10)
            .reset_index()

        )


        top_locations.columns = [

            "Location",

            "Properties"

        ]



        fig4 = px.bar(

            top_locations,

            x="Properties",

            y="Location",

            orientation="h",

            title="Top 10 Locations"

        )


        fig4.update_layout(

            template="plotly_white"

        )


        st.plotly_chart(

            fig4,

            use_container_width=True

        )



    st.markdown("---")



    st.subheader(
        "📋 Dataset Preview"
    )


    st.dataframe(

        df.head(20),

        use_container_width=True

    )



    st.markdown("---")



    st.subheader(
        "📈 Dataset Statistics"
    )



    s1,s2,s3,s4 = st.columns(4)



    with s1:

        st.metric(
            "Rows",
            df.shape[0]
        )


    with s2:

        st.metric(
            "Columns",
            df.shape[1]
        )


    with s3:

        st.metric(
            "Missing Values",
            int(
                df.isnull().sum().sum()
            )
        )


    with s4:

        st.metric(
            "Unique Locations",
            df["location"].nunique()
        )



# =====================================================
# ABOUT TAB
# =====================================================

with tab3:


    st.subheader(
        "ℹ About Project"
    )


    st.markdown(
"""
### 🏠 Bangalore House Price Prediction

This project predicts Bangalore residential property prices using Machine Learning.

---

### 🚀 Technologies Used

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Plotly

---

### 🤖 Machine Learning Model

- Linear Regression

---

### 📊 Features Used

- Total Square Feet
- BHK
- Bathrooms
- Balconies
- Area Type
- Location
- Sqft per BHK

---

### 👨‍💻 Developed By

**Ankush Sharma**
Computer Science & Engineering

Nitte Meenakshi Institute of Technology

Bangalore
"""
)



# =====================================================
# FOOTER
# =====================================================

st.markdown("---")


st.markdown(
"""
<div style="text-align:center;color:gray;">

Made with ❤️ using

<b>Python • Streamlit • Scikit-Learn • Plotly</b>

<br><br>

© 2026 Ankush Sharma

</div>
""",
unsafe_allow_html=True
)