# 📌 Customer Churn Prediction – ML Project

A Machine Learning project to **predict whether a customer is likely to churn (leave a service)** based on demographic, account, and service usage behavior.  
Built using **Python, Scikit-Learn, SMOTE, Random Forest, and Streamlit** with live deployment.


## 🎯 Project Objective
Telecom companies lose huge revenue when customers leave.  
The goal of this project is to:

✔️ Predict whether a customer will churn  
✔️ Identify key churn indicators  
✔️ Support business teams in retention planning  
✔️ Provide an interactive web app to test predictions  

---

## 🧠 Business Problem
Churn Prediction helps answer:
- Which customers are likely to leave?
- Who needs retention offers?
- What patterns indicate customer dissatisfaction?

This dataset is **rule-driven**, meaning churn is strongly influenced by business decisions such as contract type, tenure, support availability, and Internet service type.  
Because these features are highly informative, the model achieves **near-perfect performance**.

---

## 📂 Dataset Overview
The dataset includes:

| Feature | Description |
|--------|------------|
| Age | Customer age |
| Gender | Male / Female |
| Tenure | Subscription length in months |
| MonthlyCharges | Customer billing amount |
| ContractType | Month-to-month / One-year / Two-year |
| InternetService | DSL / Fiber / None |
| TechSupport | Yes / No |
| TotalCharges | Total amount billed |
| Churn | Target (Yes / No) |

---

## 🧪 Model Approach

### 🧹 Data Pre-Processing
✔️ Handle missing values  
✔️ Convert categorical → numeric (One-Hot Encoding)  
✔️ Convert Yes/No → 1/0  
✔️ Remove duplicates  
✔️ Train–Test Split with Stratification  
✔️ SMOTE applied to fix class imbalance  

---

### 🤖 Models Trained
| Model | Status |
|------|--------|
| Logistic Regression | Trained |
| K-Nearest Neighbors | Trained |
| Support Vector Machine | Trained |
| Random Forest | **Selected Best Model** |
| Gradient Boosting | Trained |

---

## 🏆 Final Model Performance
Since churn behavior in this dataset is strongly rule-based:

- ✔️ **Accuracy:** 100%
- ✔️ **Precision:** 100%
- ✔️ **Recall:** 100%
- ✔️ **F1-Score:** 100%
- ✔️ **ROC-AUC:** 1.0

📌 Explanation:  
This dataset contains very strong business signals. Features such as **month-to-month contracts, lack of tech support, and low tenure** almost perfectly indicate churn behavior.  
So the model learns these rules accurately instead of guessing.

---

## 🧾 Key Insights
📌 Month-to-Month customers churn the most  
📌 Customers without Tech Support churn heavily  
📌 Short-tenure customers churn more  
📌 Internet Service Type impacts churn  

---

## 🏗️ Tech Stack
- **Python**
- **Pandas | NumPy**
- **Scikit-Learn**
- **Imbalanced-Learn (SMOTE)**
- **Matplotlib | Seaborn**
- **Joblib**
- **Streamlit (Deployment)**

---

## 🖥️ Streamlit Web App
The app allows users to:

✔️ Enter customer details  
✔️ Predict churn probability  
✔️ Get instant decision feedback  
✔️ Useful for real-time demonstration  

---

## 📦 Project Structure
```
project/
 ├── app.py
 ├── best_model.pkl
 ├── scaler.pkl
 ├── requirements.txt
 └── notebook.ipynb
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repo
```bash
git clone https://github.com/yourname/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run App
```bash
streamlit run app.py
```

---

## 🌍 Deployment
Deployed using **Streamlit Cloud**

Steps:
1️⃣ Push project to GitHub  
2️⃣ Go to Streamlit Cloud  
3️⃣ Select repo → Choose `app.py` → Deploy  

---

## 🧑‍💻 Author
**ABDUL RAKHEEB**  
🎓 B.Tech CSE | Data Science & Machine Learning Enthusiast  
📍 India  

---

## ⭐ Show Support
If you like this project:

✔️ Star the repository ⭐  
✔️ Share with friends  
✔️ Connect for collaboration 😊

