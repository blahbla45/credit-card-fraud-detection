# 💳 Credit Card Fraud Detection System

## 📌 Overview
This project is about detecting fraudulent credit card transactions using Machine Learning. The idea is to classify whether a transaction is normal or fraud based on past transaction data. It also handles the issue of imbalanced data and uses a Random Forest model for prediction.

---

## ⚙️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib, Seaborn  
- Flask (basic deployment)

---

## 📊 Dataset
The dataset used is the Kaggle Credit Card Fraud dataset.

🔗 Dataset link: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data

- Features are mostly PCA transformed (V1–V28)  
- `Amount` feature is also included  
- Target column:  
  - `0` → Normal transaction  
  - `1` → Fraud transaction  

---

## 🧠 Project Details
This project focuses on detecting fraudulent credit card transactions using Machine Learning techniques. It includes data preprocessing, handling imbalanced data, and training a Random Forest classifier for prediction.

---

## 📈 Results
- Model performs well on detecting fraud cases  
- Confusion matrix and classification report used for evaluation  
- Focus was more on recall since fraud detection is important  

---

## 🚀 How to run the project

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run data preprocessing & model training
Open Jupyter Notebook:

```bash
jupyter notebook
```

Then run in order:
- dataprocessing.ipynb
- randomforest.ipynb

This will:
- preprocess the data
- train Random Forest model
- save the trained model file

### 3. Run Flask app
```bash
python appflask.py
```
