import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page configuration
st.set_page_config(
    page_title="AIgnite | AI Loan Approval Assistant",
    page_icon="assets/aignite_logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

    /* ==============================
       COLOR VARIABLES
       ============================== */

    :root {
        --primary-blue: #0B5ED7;
        --dark-blue: #123B73;
        --aignite-blue: #1261D6;
        --hover-blue: #084298;
        --light-blue: #EAF3FF;
        --border-blue: #D6E5F5;
        --text-dark: #252B3A;
    }


    /* ==============================
       MAIN PAGE
       ============================== */

    .stApp {
        background-color: #FFFFFF;
        color: var(--text-dark);
    }


    /* ==============================
       MAIN CONTENT WIDTH
       ============================== */

    .block-container {
        max-width: 1200px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }


    /* ==============================
       MAIN HEADINGS
       ============================== */

    h1 {
        color: var(--dark-blue) !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
    }

    h2, h3 {
        color: var(--dark-blue) !important;
    }


    /* ==============================
       SECTION HEADINGS
       ============================== */

    .section-title {
        color: var(--primary-blue);
        font-size: 1.25rem;
        font-weight: 650;
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
    }


    /* ==============================
       CAPTION / SUBTITLE
       ============================== */

    .subtitle {
        color: #6B7280;
        font-size: 0.95rem;
        margin-top: -10px;
        margin-bottom: 20px;
    }


    /* ==============================
       INPUT LABELS
       ============================== */

    label {
        color: #374151 !important;
        font-weight: 500 !important;
    }


    /* ==============================
       INPUT BOXES
       ============================== */

    div[data-baseweb="input"] {
        border-radius: 8px;
    }

    div[data-baseweb="select"] {
        border-radius: 8px;
    }


    /* ==============================
       DIVIDERS
       ============================== */

    hr {
        border: none;
        border-top: 1px solid #DCE3EA;
        margin: 1.5rem 0;
    }


    /* ==============================
       PREDICTION BUTTON
       ============================== */

    div.stButton > button {
        background-color: var(--primary-blue) !important;
        color: white !important;

        border: none !important;
        border-radius: 8px !important;

        padding: 0.65rem 1.6rem !important;

        font-size: 1rem !important;
        font-weight: 600 !important;

        transition: all 0.2s ease-in-out;
    }


    /* Button hover */

    div.stButton > button:hover {
        background-color: var(--hover-blue) !important;
        color: white !important;

        border: none !important;

        transform: translateY(-1px);
        box-shadow: 0 4px 10px rgba(11, 94, 215, 0.20);
    }


    /* Button active */

    div.stButton > button:active {
        background-color: var(--hover-blue) !important;
        color: white !important;
    }


    /* ==============================
       SUCCESS MESSAGE
       ============================== */

    div[data-testid="stAlert"] {
        border-radius: 10px;
    }


    /* ============================================================
   SIDEBAR
   ============================================================ */

[data-testid="stSidebar"] {
    background-color: #f8fafc;
    border-right: 1px solid #e5e7eb;
}


/* Sidebar content */

[data-testid="stSidebar"] > div:first-child {
    padding-top: 25px;
    padding-left: 20px;
    padding-right: 20px;
}


/* Sidebar logo */

[data-testid="stSidebar"] img {
    display: block;
    margin: 0 auto;
    max-width: 150px;
}


/* Divider */

.sidebar-divider {
    height: 1px;
    background-color: #dbe2ea;
    margin: 22px 0;
}


/* Section heading */

.sidebar-section-title {
    color: #174ea6;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 12px;
}


/* Navigation item */

.sidebar-item {
    color: #374151;
    font-size: 13px;
    margin-bottom: 8px;
}


/* Developer name */

.sidebar-developer {
    color: #374151;
    font-size: 13px;
    line-height: 1.6;
}


/* Version information */

.sidebar-info {
    color: #6b7280;
    font-size: 12px;
    margin-bottom: 12px;
}


/* Sidebar text hover */

.sidebar-item:hover {
    color: #174ea6;
}

    /* ==============================
       CARDS
       ============================== */

    .info-card {
        background-color: #F8FBFF;
        border: 1px solid var(--border-blue);
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-bottom: 1rem;
    }
.app-subtitle {
    color: var(--aignite-blue) !important;
    font-size: 18px;
    font-weight: 700;
    text-align: center;
    margin-top: -10px;
    margin-bottom: 25px;
}    

</style>
""", unsafe_allow_html=True)

# ==================================================
# LOAD MODEL AND SCALER
# ==================================================

scaler = joblib.load("scaler.pkl")
model = joblib.load("loan_model.pkl")

# --------------------------------------------------
# AIgnite HEADER
# --------------------------------------------------

logo_col1, logo_col2, logo_col3 = st.columns([1, 2, 1])

with logo_col2:
    st.image(
        "assets/aignite_logo_compact_wbg.png",
        width=300
    )

st.markdown(
    """
    <div class="app-subtitle">
        Smart Credit Risk Prediction powered by Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)
# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    # AIgnite Logo
    st.image(
        "assets/aignite_logo_compact_tbgr.png",
        width=150
    )

    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # Navigation
    st.markdown(
        """
        <div class='sidebar-section-title'>AI Loan Approval Assistant</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sidebar-item'>Machine Learning Project</div>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # Developer Information
    st.markdown(
        "<div class='sidebar-section-title'>👨‍💻 Developer</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sidebar-developer'>"
        "Shahid Mahmood Chaudhry"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # Version Information
    st.markdown(
        "<div class='sidebar-info'>Version 1.0</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sidebar-info'>Updated August 2026</div>",
        unsafe_allow_html=True
    )

# =====================================================
# APPLICANT INFORMATION
# =====================================================

with st.container(border=True):
    st.subheader("👤 Applicant Information")

    col1, col2 = st.columns(2)
    # Person Age
    with col1:
        person_age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=25
        )
    # Person Gender    
    with col2:
        gender_options = {'Male': 'male', 'Female': 'female'}
        person_gender = st.selectbox("Gender", list(gender_options.keys()))
        person_gender = gender_options[person_gender]
        gender_map = {'male': 1, 'female': 0}
        person_gender = gender_map[person_gender]
            
    col1, col2 = st.columns(2)
    # Person Education
    with col1:
        education_options = {
        "High School": "High School",
        "Associate": "Associate",
        "Bachelor": "Bachelor",
        "Master": "Master",
        "Doctorate": "Doctorate"
        }
        education = st.selectbox(
        "Education",
        list(education_options.keys())
        )
        education = education_options[education]
        # Custom Encoding
        education_map = {
        "High School": 0,
        "Associate": 1,
        "Bachelor": 2,
        "Master": 3,
        "Doctorate": 4
        }
        person_education = education_map[education]

    with col2:
        # Person Income
        person_income = st.number_input(
        'Annual Income',
        min_value = 0.0,
        value = 50000.0,
        step = 1000.0
        )

    col1,col2 = st.columns(2)
    # Person Employment Experience
    with col1:
        person_emp_exp = st.number_input(
        'Employment Experience (Years)',
        min_value = 0,
        max_value = 80,
        value = 2)

    # Home ownership     
    with col2:
        home_options = {
        "Rent": "RENT",
        "Own": "OWN",
        "Mortgage": "MORTGAGE",
        "Other": "OTHER"
        }
        home_ownership = st.selectbox(
        "Home Ownership",
        list(home_options.keys())
        )
        # Convert UI value to dataset value
        home_ownership = home_options[home_ownership]
        # Manual One-Hot Encoding
        home_mortgage = 0
        home_other = 0
        home_own = 0
        home_rent = 0
        if home_ownership == "MORTGAGE":
            home_mortgage = 1

        elif home_ownership == "OTHER":
            home_other = 1

        elif home_ownership == "OWN":
            home_own = 1

        elif home_ownership == "RENT":
            home_rent = 1
st.write(" ")
st.write(" ")
# =====================================================
# LOAN INFORMATION
# =====================================================

with st.container(border=True):
    st.subheader("💰 Loan Information")
    col1, col2 = st.columns(2)        
    # Loan amount       
    with col1:
        loan_amnt = st.number_input(
        "Loan Amount",
        min_value=0.0, 
        value=10000.0,
        step = 1000.0)
    #loan_int_rate    
    with col2:
        loan_int_rate = st.number_input(
        'Interest Rate (%)',
        min_value = 0.0,
        max_value = 100.0,
        value = 10.0,
        step = 0.1
        )

    col1, col2 = st.columns(2)
    # Loan percent income
    with col1:
        loan_percent_income = st.number_input(
            "Loan Percentage of Income (Example: 0.20 = 20%)",
            min_value=0.0,
            max_value=1.0,
            value=0.20,
            step = 0.01,
            format = "%.2f"
        )
    # Loan Intent    
    with col2:        
        loan_intent_options = {
            "Debt Consolidation": "DEBTCONSOLIDATION",
            "Education": "EDUCATION",
            "Home Improvement": "HOMEIMPROVEMENT",
            "Medical": "MEDICAL",
            "Personal": "PERSONAL",
            "Venture": "VENTURE"
        }
        loan_intent = st.selectbox("Loan Purpose", list(loan_intent_options.keys()))
        loan_intent = loan_intent_options[loan_intent]
        loan_debt = 0
        loan_education = 0
        loan_home = 0
        loan_medical = 0
        loan_personal = 0
        loan_venture = 0
        if loan_intent == "DEBTCONSOLIDATION":
            loan_debt = 1
        elif loan_intent == "EDUCATION":
            loan_education = 1
        elif loan_intent == "HOMEIMPROVEMENT":
            loan_home = 1
        elif loan_intent == "MEDICAL":
            loan_medical = 1
        elif loan_intent == "PERSONAL":
            loan_personal = 1
        elif loan_intent == "VENTURE":
            loan_venture = 1

st.write(" ")
st.write(" ")            
# ==========================================
# 📊 CREDIT INFORMATION
# ==========================================

with st.container(border=True):
    st.subheader("📊 Credit Information")
    col1, col2 = st.columns(2)
    #Credit Score
    with col1:
        credit_score = st.number_input(
        'Credit Score',
        min_value = 300,
        max_value = 850,
        value = 650,
        step = 1
        )
    # Person Credit History Length    
    with col2:
        cb_person_cred_hist_length = st.number_input(
        'Credit History Length (Years)',
        min_value = 0.0,
        value = 5.0,
        step = 0.5
        )
    col1, col2 = st.columns(2)    
    # Previous loan defaults on file (binary encoding)
    with col1:
        default_options = {
        "Yes": "Yes",
        "No": "No"
        }
        previous_default = st.selectbox(
        "Previous Loan Default",
        list(default_options.keys())
        )
        previous_default = default_options[previous_default]
        default_map = {
        "Yes": 1,
        "No": 0
        }
        previous_loan_defaults_on_file = default_map[previous_default]

st.write(" ")
st.write(" ")        
# =====================================
# Prediction Button
# =====================================
with st.container(border=True):
        
    st.subheader("🤖 AI Prediction")
    if st.button(
        "🔍 Predict Loan Approval",
        use_container_width= True):

        # Create NumPy Array
        input_data = np.array([[
            person_age,
            person_gender,
            person_education,
            person_income,
            person_emp_exp,
            loan_amnt,
            loan_int_rate,
            loan_percent_income,
            cb_person_cred_hist_length,
            credit_score,
            previous_loan_defaults_on_file,
            home_mortgage,
            home_other,
            home_own,
            home_rent,
            loan_debt,
            loan_education,
            loan_home,
            loan_medical,
            loan_personal,
            loan_venture
        ]])

        # Show Input Data
        print("========== INPUT DATA ==========")
        print(input_data)

        # Scale Input
        input_data_scaled = scaler.transform(input_data)

        print("========== SCALED DATA ==========")
        print(input_data_scaled)

        # Make Prediction
        prediction = model.predict(input_data_scaled)

        print("========== PREDICTION ==========")
        print(prediction)

        # Prediction Probability
        probability = model.predict_proba(input_data_scaled)
        print("========== PROBABILITY ==========")
        print("Probability:", probability)
        
        confidence = probability[0][prediction[0]]

        # Display Result
        if prediction[0] == 1:

            confidence = probability[0][1]

            st.success("✅ Loan Approved!")

        else:

            confidence = probability[0][0]

            st.error("❌ Loan Rejected.")

        st.metric(
            label = "Prediction Confidence",
            value = f"{confidence:.2%}")
        if prediction[0] == 1:
            st.info(
                "💡 Recommendation: The applicant meets the approval criteria."
            )
        else:
            st.warning(
                "💡 Recommendation: Review income, credit score, or previous loan default before applying again."
            )    