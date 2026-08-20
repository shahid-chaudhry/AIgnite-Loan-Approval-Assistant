<p align="center">
  <img src="assets/aignite_logo_compact_wbg.png" alt="AIgnite Logo" width="400">
</p>

<h1 align="center">AIgnite — AI Loan Approval Assistant</h1>

<p align="center">
  <strong>Smart Credit Risk Prediction powered by Machine Learning</strong>
</p>

---

## 📌 Project Overview
# 🏦 AIgnite — AI Loan Approval Assistant

### Smart Credit Risk Prediction powered by Machine Learning

AIgnite AI Loan Approval Assistant is a machine learning application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant, loan, and credit-related information.

The project combines a trained machine learning model with an interactive **Streamlit** interface to provide real-time loan approval predictions and confidence probabilities.

---

## 📌 Project Overview

Loan approval decisions depend on several factors such as income, employment experience, credit score, loan amount, loan purpose, and previous loan history.

This project demonstrates how machine learning can be used to analyze these factors and assist in making faster, data-driven loan approval decisions.

The trained model is integrated into a user-friendly Streamlit web application where users can enter applicant information and instantly receive a prediction.

---

🌐 Live Demo

🚀 Try the application:

https://aignite-loan-approval-assistant.streamlit.app/

---

## 🎯 Objective

The main objectives of this project are:

- Build a machine learning model for loan approval prediction.
- Perform data preprocessing and feature transformation.
- Convert categorical features into machine-readable values.
- Standardize numerical features using `StandardScaler`.
- Train and evaluate a classification model.
- Save the trained model and scaler for deployment.
- Build an interactive Streamlit application.
- Display prediction probabilities to the user.
- Create a professional AI-powered user interface.

---

## 🤖 Machine Learning Model

The project uses:

**Logistic Regression**

Logistic Regression is a supervised machine learning classification algorithm suitable for predicting binary outcomes.

In this project:

```text
0 → Loan Rejected
1 → Loan Approved

The trained model is saved as:

loan_model.pkl

The fitted scaler is saved as:

scaler.pkl

📊 Dataset

The dataset contains 45,000 loan application records and includes applicant, financial, loan, and credit information.

Features
Feature	Description
person_age	Applicant age
person_gender	Applicant gender
person_education	Education level
person_income	Annual income
person_emp_exp	Employment experience
person_home_ownership	Home ownership status
loan_amnt	Requested loan amount
loan_intent	Purpose of the loan
loan_int_rate	Loan interest rate
loan_percent_income	Loan amount as percentage of income
cb_person_cred_hist_length	Credit history length
credit_score	Applicant credit score
previous_loan_defaults_on_file	Previous loan default information
loan_status	Target variable
🔄 Data Preprocessing

Several preprocessing operations were performed before model training.

Education Mapping

Education levels were converted into numerical values:

education_map = {
    'High School': 0,
    'Associate': 1,
    'Bachelor': 2,
    'Master': 3,
    'Doctorate': 4
}
Gender Mapping

Gender was converted into numerical values:

gender_map = {
    'female': 0,
    'male': 1
}
Categorical Encoding

Categorical variables such as home ownership and loan intent were converted using one-hot encoding.

Feature Scaling

Numerical features were standardized using:

StandardScaler()

The fitted scaler was saved and reused during prediction so that new application data receives the same preprocessing as the training data.

🧪 Model Training

The dataset was divided into training and testing sets using:

train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

This resulted in:

80% → Training data
20% → Testing data

The stratify=y parameter was used to maintain the class distribution between the training and testing datasets.

📈 Model Prediction

The application generates two outputs:

Prediction
Loan Approved

or

Loan Rejected
Probability

The model also provides the probability associated with each class.

For example:

Approved: 60.49%
Rejected: 39.51%

This provides additional insight into the model's prediction rather than displaying only the final class.

🖥️ Streamlit Application

The machine learning model has been integrated into a professional Streamlit interface.

The application includes:

👤 Applicant Information
💰 Loan Information
💳 Credit Information
🏠 Home Ownership
📋 Loan Purpose
🤖 AI-powered prediction
📊 Prediction confidence
🎨 AIgnite branding
📱 Responsive layout
🎯 Professional UI styling
🏗️ Project Structure
Loan_Approval_Prediction_System/
│
├── app.py
├── loan_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
└── assets/
    ├── aignitelogo.png
    └── aignite_logo_compact.png
⚙️ Technologies Used
Programming Language
Python
Machine Learning
Scikit-learn
Logistic Regression
StandardScaler
Data Processing
Pandas
NumPy
Web Application
Streamlit
Development Environment
VS Code
Google Colab
Version Control
Git
GitHub
🚀 Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Navigate into the project directory:

cd Loan_Approval_Prediction_System

Install the required dependencies:

pip install -r requirements.txt
▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

Usually:

http://localhost:8501
🔐 Important Note

The application uses the saved machine learning artifacts:

loan_model.pkl
scaler.pkl

The same preprocessing pipeline used during model training must be maintained when making predictions on new data.

Feature order and feature transformations must remain consistent between training and deployment.

📸 Application Preview

Add screenshots of your application here after uploading them to the repository.

Example:

![AIgnite Loan Approval Assistant](screenshots/app.png)
🧠 What I Learned

This project helped me practice and understand:

Data cleaning
Exploratory data analysis
Feature engineering
Categorical encoding
Feature scaling
Train-test splitting
Logistic Regression
Model prediction
Prediction probabilities
Model persistence using Pickle
Streamlit application development
CSS customization in Streamlit
UI/UX design
Git and GitHub
Machine learning deployment workflow
🔮 Future Improvements

Possible future improvements include:

Model comparison with Random Forest, XGBoost, and other classifiers.
Hyperparameter tuning.
Cross-validation.
Explainable AI using SHAP.
More detailed risk analysis.
Model performance dashboard.
Database integration.
User authentication.
Cloud deployment.
Automated model retraining.
Loan risk scoring.
👨‍💻 Developer
Shahid Mahmood Chaudhry

Machine Learning & AI Enthusiast

This project was developed as part of my journey toward becoming an AI Engineer, combining machine learning with practical application development.

🏷️ Project

AIgnite — AI Loan Approval Assistant

Smart Credit Risk Prediction powered by Machine Learning

📄 License

This project is intended for educational and portfolio purposes.
