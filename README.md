<h1 align="center">🏠 Bangalore House Price Prediction</h1>

<p align="center">
An end-to-end Machine Learning project that predicts house prices in Bangalore using Linear Regression and Streamlit.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit">
  <img src="https://img.shields.io/badge/License-MIT-green">
  <img src="https://img.shields.io/badge/Status-Completed-success">
</p>


A Machine Learning web application that predicts the estimated price of houses in Bangalore based on property details such as location, area type, total square feet, number of bedrooms, bathrooms, and balconies.

The application is built using **Python**, **Scikit-learn**, and **Streamlit**, providing users with a simple and interactive interface for real-time house price prediction.

---

## 📖 Overview

This project uses a **Linear Regression** model trained on the Bengaluru House Price Dataset. The dataset underwent extensive preprocessing, feature engineering, and outlier removal to improve prediction accuracy.

The trained model is deployed as a **Streamlit web application**, allowing users to enter house details and instantly receive a predicted house price.

---

## ✨ Features

- 🏠 Predict Bangalore house prices instantly
- 📍 Location-based price estimation
- 📊 Interactive Streamlit web interface
- 🧹 Data cleaning and preprocessing
- ⚙️ Feature engineering (`sqft_per_bhk`)
- 📌 One-Hot Encoding for categorical variables
- 📈 Linear Regression model
- 💾 Model saved using Pickle
- 🚀 Real-time predictions

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Web Framework | Streamlit |
| Model Serialization | Pickle |
| Data Storage | JSON |
| Development | Jupyter Notebook |

---

## 📊 Machine Learning Pipeline

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Missing Value Handling
      │
      ▼
Feature Engineering
      │
      ▼
Outlier Removal
      │
      ▼
One-Hot Encoding
      │
      ▼
Train-Test Split
      │
      ▼
Linear Regression Model
      │
      ▼
Model Evaluation
      │
      ▼
Model Serialization (.pkl)
      │
      ▼
Streamlit Deployment
```

---

## 📈 Model Performance

| Metric | Value |
|---------|-------|
| Algorithm | Linear Regression |
| R² Score | **0.856** |
| Cross Validation Score | **0.858** |

---

## 📁 Project Structure

```text
Bangalore-House-Price-Prediction/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── data/
│   └── Bengaluru_House_Data.csv
│
├── models/
│   ├── bangalore_house_price_model.pkl
│   └── columns.json
│
└── notebooks/
    └── Bangalore_House_Price_Prediction.ipynb
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/AnkushSharma5/bangalore-house-price-prediction.git
```

### Navigate to the project directory

```bash
cd bangalore-house-price-prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

or

```bash
py -m streamlit run app.py
```

---

## 💻 How to Use

1. Enter the Total Square Feet.
2. Select the Number of BHK.
3. Select the Number of Bathrooms.
4. Select the Number of Balconies.
5. Choose the Area Type.
6. Select the Location.
7. Click **Predict Price**.
8. View the estimated house price.

---

## 📸 Application Screenshots

### Home Page

> *(Add a screenshot of your Streamlit home page here.)*

### Prediction Result

> *(Add a screenshot showing the predicted price.)*

---

## 📌 Future Improvements

- Implement advanced regression models such as XGBoost and Random Forest.
- Add price trend visualization using interactive charts.
- Integrate Google Maps for location-based analysis.
- Include additional property features for improved accuracy.
- Deploy using Docker and cloud platforms.

---

## 👨‍💻 Author

**Ankush Sharma**

- 🎓 Information Science & Engineering Student
- 💻 Passionate about Machine Learning, Data Science, and Software Development

**GitHub:** https://github.com/AnkushSharma5

**LinkedIn:** *(Add your LinkedIn profile here)*

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
