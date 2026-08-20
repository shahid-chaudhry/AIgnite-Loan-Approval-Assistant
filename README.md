<p align="center">
  <img src="assets/aignite_logo_compact_wbg.png" alt="AIgnite Logo" width="400">
</p>

<h1 align="center">AIgnite — AI Loan Approval Assistant</h1>

<p align="center">
  <strong>Smart Credit Risk Prediction powered by Machine Learning</strong>
</p>

---

# 🤖 AIgnite Loan Approval Assistant

A machine learning web application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on an applicant's financial, employment, loan, and credit information.

Built using **Python, Scikit-learn, and Streamlit**.

---

## 🌐 Live Demo

🚀 **Try the application:**

https://aignite-loan-approval-assistant.streamlit.app/

---

## 📌 Project Overview

Loan approval is an important decision-making process for banks and financial institutions. Manually evaluating loan applications can be time-consuming and may involve multiple factors.

This project uses **Machine Learning** to analyze applicant information and predict the loan approval status.

The deployed application provides a simple interface where users can enter applicant, loan, and credit details and receive:

* ✅ Loan approval prediction
* 📊 Prediction confidence
* 💡 Automated recommendation
* 🌐 Easy-to-use web interface

---

## 🎯 Problem Statement

The goal of this project is to build a machine learning model that can predict whether a loan application will be approved or rejected based on historical applicant data.

The model analyzes factors such as:

* Applicant age
* Gender
* Education
* Income
* Employment experience
* Home ownership
* Loan amount
* Loan intent
* Interest rate
* Loan percentage of income
* Credit history length
* Credit score
* Previous loan defaults

---

## 📂 Dataset

The dataset contains **45,000 loan application records** and **14 columns**.

### Target Variable

```text
loan_status
```

The target represents the predicted loan outcome.

### Data Quality

* Total Records: **45,000**
* Total Columns: **14**
* Missing Values: **0**
* Duplicate Records: **0**

---

## ⚙️ Data Preprocessing

The following preprocessing steps were performed:

1. Checked for missing values.
2. Checked for duplicate records.
3. Encoded categorical variables.
4. Prepared independent features and the target variable.
5. Split the dataset into training and testing sets.
6. Applied feature scaling using `StandardScaler`.

---

## 🧠 Machine Learning Model

The project uses:

### Logistic Regression

Logistic Regression is a supervised machine learning algorithm commonly used for classification problems.

The model predicts one of two possible outcomes:

```text
0 → Rejected
1 → Approved
```

The trained model and scaler were saved using Pickle:

```text
model.pkl
scaler.pkl
```

---

## 📈 Model Performance

The Logistic Regression model achieved an overall accuracy of:

# 🎯 89.94%

### Classification Report

| Class | Precision | Recall | F1-Score | Support |
| ----- | --------: | -----: | -------: | ------: |
| 0     |      0.93 |   0.94 |     0.94 |    7000 |
| 1     |      0.79 |   0.75 |     0.77 |    2000 |

### Overall Metrics

| Metric                 |      Score |
| ---------------------- | ---------: |
| Accuracy               | **89.94%** |
| Macro Avg Precision    |       0.86 |
| Macro Avg Recall       |       0.85 |
| Macro Avg F1-Score     |       0.85 |
| Weighted Avg Precision |       0.90 |
| Weighted Avg Recall    |       0.90 |
| Weighted Avg F1-Score  |       0.90 |

### Confusion Matrix

```text
[[6599  401]
 [ 504 1496]]
```

---

## 💻 Web Application

The machine learning model is deployed as an interactive web application using **Streamlit**.

The application is organized into three main sections:

### 👤 Applicant Information

Users can provide details such as:

* Age
* Gender
* Education
* Income
* Employment experience
* Home ownership

### 💰 Loan Information

Users can enter:

* Loan amount
* Loan intent
* Interest rate
* Loan percentage of income

### 🏦 Credit Information

Users can provide:

* Credit score
* Credit history length
* Previous loan defaults

After entering the information, the application generates a prediction along with a confidence score and recommendation.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

---

## 📁 Project Structure

```text
AIgnite-Loan-Approval-Assistant/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── favicon.png
└── README.md
```

---

## 🚀 Run Locally

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Folder

```bash
cd AIgnite-Loan-Approval-Assistant
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

---

## 📦 Requirements

```text
streamlit
pandas
numpy
scikit-learn
```

---

## ✨ Key Features

* 🤖 Machine Learning-powered predictions
* 📊 Prediction confidence score
* 💡 Automated loan recommendation
* 🖥️ Clean and interactive Streamlit interface
* 📱 Responsive design
* 🌐 Deployed online using Streamlit Cloud
* 🎯 89.94% model accuracy

---

## 🔮 Future Improvements

Possible future improvements include:

* Experimenting with Random Forest and XGBoost.
* Adding more model evaluation visualizations.
* Adding feature importance analysis.
* Improving class imbalance handling.
* Creating a database to store prediction history.
* Adding user authentication.

---

## 👨‍💻 Developed By

**Shahid Mahmood Chaudhry**

AI & Machine Learning Enthusiast | Python Developer

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub!

---

### 🚀 AIgnite

**Artificial Intelligence • Machine Learning • Data Science • Web Applications**

*Turning Data into Decisions.*
