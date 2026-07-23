<h1 align="center">🏠 Bangalore House Price Prediction</h1>

<p align="center">
An end-to-end Machine Learning web application that predicts house prices in Bangalore using Linear Regression and Streamlit.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-green">
  <img src="https://img.shields.io/badge/Status-Completed-success">
</p>

---

## 📖 Overview

This project predicts the price of residential properties in Bangalore based on property details such as location, area type, total square feet, number of bedrooms, bathrooms, and balconies.

The model was trained using the **Bengaluru House Price Dataset** and deployed as an interactive web application using **Streamlit**.

---

## ✨ Features

- 🏠 Real-time house price prediction
- 📍 Location-based prediction
- 📊 Interactive Streamlit interface
- 🧹 Data cleaning & preprocessing
- ⚙️ Feature engineering (`sqft_per_bhk`)
- 📌 One-Hot Encoding
- 📈 Linear Regression model
- 💾 Model serialization using Pickle
- 🚀 Fast and responsive predictions

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Web Framework | Streamlit |
| Model Storage | Pickle |
| File Handling | JSON |
| Development | Jupyter Notebook |

---

## 📊 Machine Learning Workflow

```text
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
Streamlit Web Application
```

---

## 📈 Model Performance

| Metric | Score |
|--------|------:|
| Algorithm | Linear Regression |
| R² Score | **0.856** |
| Cross Validation Score | **0.858** |

---

## 📸 Application Screenshots

<p align="center">
  <img src="assets/input-form.png" alt="Input Form" width="48%">
  <img src="assets/prediction-result.png" alt="Prediction Result" width="48%">
</p>

---

## 📁 Project Structure

```text
Bangalore-House-Price-Prediction/
│
├── assets/
│   ├── input-form.png
│   └── prediction-result.png
│
├── data/
│   └── Bengaluru_House_Data.csv
│
├── models/
│   ├── bangalore_house_price_model.pkl
│   └── columns.json
│
├── notebooks/
│   └── Bangalore_House_Price_Prediction.ipynb
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/AnkushSharma5/Bangalore-House-Price-Prediction.git
```

Navigate to the project

```bash
cd Bangalore-House-Price-Prediction
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

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
3. Enter the Number of Bathrooms.
4. Enter the Number of Balconies.
5. Select the Area Type.
6. Select the Property Location.
7. Click **Predict Price**.
8. View the estimated house price instantly.

---

## 🔮 Future Improvements

- Implement advanced regression models (Random Forest, XGBoost)
- Hyperparameter tuning
- Interactive price trend visualizations
- Google Maps integration
- Support for additional property features
- Cloud deployment using Docker

---

## 👨‍💻 Author

**Ankush Sharma**

🎓 Information Science & Engineering Student

💻 Passionate about Machine Learning, Data Science, and Software Development

- GitHub: https://github.com/AnkushSharma5
- LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
