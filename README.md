# 🍲 Local Food Wastage Analytics & Management

## 📌 Overview
This project focuses on analyzing local food wastage data, testing hypotheses, and building predictive models to reduce wastage.  
It also includes a **Streamlit-based Food Wastage Management System** to connect providers (who donate food) with receivers (who need food).

The project has two parts:
1. **Data Analytics & Machine Learning (Colab Notebook)** → EDA, Hypothesis Testing, and Predictive Models  
2. **Streamlit App** → A management system to view, add, search, and analyze records

---

## 📂 Datasets
The project uses 4 CSV datasets:
- `providers_data.csv` → Details of food providers  
- `receivers_data.csv` → Details of food receivers  
- `food_listings_data.csv` → Food donation listings  
- `claims_data.csv` → Claim details of receivers  

---

## ⚙️ Tech Stack
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)  
- **Jupyter/Google Colab** (for EDA & ML models)  
- **Streamlit** (for interactive web app)  
- **SQLite** (for database management)  
- **GitHub** (for version control & project hosting)  

---

## 🔍 Features
### 📊 Data Analysis & ML
- End-to-end **EDA** with visualizations  
- **3 Hypotheses tested**  
- Built **classification models** to predict claim success  
- Compared models: Logistic Regression, Random Forest, Gradient Boosting  
- Final chosen model: **Gradient Boosting** (best accuracy & recall)  

### 🌐 Streamlit App
- **View Data** → Explore providers, receivers, food listings, and claims  
- **Add Record** → Add new food donation records  
- **Search** → Find food listings by city  
- **Analysis** → Bar chart visualization of food type distribution  

---

## 🚀 Setup Instructions

### 🔹 1. Clone Repo
```bash
git clone https://github.com/your-username/food-wastage-management.git
cd food-wastage-management
