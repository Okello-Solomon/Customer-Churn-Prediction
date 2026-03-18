import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ✅ FULL DARK THEME (MERGED)
st.markdown("""
    <style>
    /* ===== MAIN APP ===== */
    .stApp {
        background-color: #0e1117;
        color: white;
    }

    /* ===== SIDEBAR ===== */
    section[data-testid="stSidebar"] {
        background-color: #0e1117;
    }

    /* ===== TEXT ===== */
    h1, h2, h3, h4, h5, h6, p, label, span {
        color: white !important;
    }

    /* ===== SELECTBOX (closed) ===== */
    div[data-baseweb="select"] > div {
        background-color: #1e222b !important;
        color: white !important;
        border-radius: 8px;
    }

    /* ===== DROPDOWN MENU ===== */
    div[role="listbox"] {
        background-color: #1e222b !important;
        color: white !important;
    }

    div[role="option"] {
        background-color: #1e222b !important;
        color: white !important;
    }

    div[role="option"]:hover {
        background-color: #2a2f3a !important;
    }

    div[aria-selected="true"] {
        background-color: #1f77b4 !important;
        color: white !important;
    }

    /* ===== SLIDERS ===== */
    .stSlider div {
        color: white !important;
    }

    /* ===== BUTTONS ===== */
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 8px;
    }

    /* ===== METRICS ===== */
    [data-testid="stMetricValue"] {
        color: white;
    }

    /* ===== PROGRESS BAR ===== */
    .stProgress > div > div > div > div {
        background-color: #1f77b4;
    }

    /* ===== HEADER / TOOLBAR ===== */
    header[data-testid="stHeader"] {
        background-color: #0e1117 !important;
    }

    header[data-testid="stHeader"] button {
        color: white !important;
        background-color: transparent !important;
    }

    header[data-testid="stHeader"] button:hover {
        background-color: #2a2f3a !important;
        border-radius: 6px;
    }

    /* Three-dot menu dropdown */
    div[data-testid="stToolbarMenu"] {
        background-color: #1e222b !important;
        color: white !important;
    }

    div[data-testid="stToolbarMenu"] * {
        color: white !important;
    }

    </style>
""", unsafe_allow_html=True)

# Load trained pipeline
pipeline = joblib.load("churn_model.pkl")

# App Title
st.title("📊 Customer Churn Prediction")
st.markdown("""
Predict whether a customer is likely to **churn (leave the company)**.

**Classes:**  
0 = No Churn  
1 = Churn
""")

# Sidebar
st.sidebar.header("Customer Information")


def user_input_features():

    SeniorCitizen = st.sidebar.selectbox("Senior Citizen", ["Yes", "No"])
    Dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
    PhoneService = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
    PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])

    tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)

    MultipleLines = st.sidebar.selectbox(
        "Multiple Lines", ['No', 'No phone service', 'Yes'])

    InternetService = st.sidebar.selectbox(
        "Internet Service", ['DSL', 'Fiber optic', 'No'])

    OnlineSecurity = st.sidebar.selectbox(
        "Online Security", ['No', 'No internet service', 'Yes'])

    DeviceProtection = st.sidebar.selectbox(
        "Device Protection", ['No', 'No internet service', 'Yes'])

    TechSupport = st.sidebar.selectbox(
        "Tech Support", ['No', 'No internet service', 'Yes'])

    StreamingTV = st.sidebar.selectbox(
        "Streaming TV", ['No', 'No internet service', 'Yes'])

    StreamingMovies = st.sidebar.selectbox(
        "Streaming Movies", ['No', 'No internet service', 'Yes'])

    Contract = st.sidebar.selectbox(
        "Contract", ['Month-to-month', 'One year', 'Two year'])

    PaymentMethod = st.sidebar.selectbox(
        "Payment Method",
        ['Bank transfer (automatic)',
         'Credit card (automatic)',
         'Electronic check',
         'Mailed check']
    )

    # Binary encoding
    SeniorCitizen = 1 if SeniorCitizen == "Yes" else 0
    Dependents = 1 if Dependents == "Yes" else 0
    PhoneService = 1 if PhoneService == "Yes" else 0
    PaperlessBilling = 1 if PaperlessBilling == "Yes" else 0

    # Dummy encoding
    MultipleLines_No_phone_service = 1 if MultipleLines == 'No phone service' else 0
    MultipleLines_Yes = 1 if MultipleLines == 'Yes' else 0

    InternetService_Fiber_optic = 1 if InternetService == 'Fiber optic' else 0
    InternetService_No = 1 if InternetService == 'No' else 0

    OnlineSecurity_No_internet_service = 1 if OnlineSecurity == 'No internet service' else 0
    OnlineSecurity_Yes = 1 if OnlineSecurity == 'Yes' else 0

    DeviceProtection_No_internet_service = 1 if DeviceProtection == 'No internet service' else 0
    DeviceProtection_Yes = 1 if DeviceProtection == 'Yes' else 0

    TechSupport_No_internet_service = 1 if TechSupport == 'No internet service' else 0
    TechSupport_Yes = 1 if TechSupport == 'Yes' else 0

    StreamingTV_No_internet_service = 1 if StreamingTV == 'No internet service' else 0
    StreamingTV_Yes = 1 if StreamingTV == 'Yes' else 0

    StreamingMovies_No_internet_service = 1 if StreamingMovies == 'No internet service' else 0
    StreamingMovies_Yes = 1 if StreamingMovies == 'Yes' else 0

    Contract_One_year = 1 if Contract == 'One year' else 0
    Contract_Two_year = 1 if Contract == 'Two year' else 0

    PaymentMethod_Credit_card = 1 if PaymentMethod == 'Credit card (automatic)' else 0
    PaymentMethod_Electronic_check = 1 if PaymentMethod == 'Electronic check' else 0
    PaymentMethod_Mailed_check = 1 if PaymentMethod == 'Mailed check' else 0

    data = {
        'SeniorCitizen': SeniorCitizen,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'PaperlessBilling': PaperlessBilling,
        'MultipleLines_No phone service': MultipleLines_No_phone_service,
        'MultipleLines_Yes': MultipleLines_Yes,
        'InternetService_Fiber optic': InternetService_Fiber_optic,
        'InternetService_No': InternetService_No,
        'OnlineSecurity_No internet service': OnlineSecurity_No_internet_service,
        'OnlineSecurity_Yes': OnlineSecurity_Yes,
        'DeviceProtection_No internet service': DeviceProtection_No_internet_service,
        'DeviceProtection_Yes': DeviceProtection_Yes,
        'TechSupport_No internet service': TechSupport_No_internet_service,
        'TechSupport_Yes': TechSupport_Yes,
        'StreamingTV_No internet service': StreamingTV_No_internet_service,
        'StreamingTV_Yes': StreamingTV_Yes,
        'StreamingMovies_No internet service': StreamingMovies_No_internet_service,
        'StreamingMovies_Yes': StreamingMovies_Yes,
        'Contract_One year': Contract_One_year,
        'Contract_Two year': Contract_Two_year,
        'PaymentMethod_Credit card (automatic)': PaymentMethod_Credit_card,
        'PaymentMethod_Electronic check': PaymentMethod_Electronic_check,
        'PaymentMethod_Mailed check': PaymentMethod_Mailed_check
    }

    return pd.DataFrame([data])


input_df = user_input_features()

# Prediction Button
if st.button("🔍 Predict Customer Churn"):

    prediction = pipeline.predict(input_df)
    prediction_proba = pipeline.predict_proba(input_df)

    prob_no_churn = prediction_proba[0][0]
    prob_churn = prediction_proba[0][1]

    pred_class = prediction[0]

    status_map = {0: "No Churn", 1: "Churn"}
    description_map = {
        0: "Customer is likely to stay.",
        1: "Customer is likely to leave."
    }

    if pred_class == 1:
        background_color = "#e74c3c"
    else:
        background_color = "#2ecc71"

    st.subheader("Prediction")

    st.markdown(
        f"""
        <div style='
            background-color:{background_color};
            padding:15px;
            border-radius:8px;
            color:white;
            font-size:20px;
            font-weight:bold;
            text-align:center;
        '>
        Prediction: {status_map[pred_class]}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"**Interpretation:** {description_map[pred_class]}")

    st.subheader("Churn Probability")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("No Churn Probability", f"{prob_no_churn*100:.2f}%")

    with col2:
        st.metric("Churn Probability", f"{prob_churn*100:.2f}%")

    st.subheader("Churn Risk Level")
    st.progress(int(prob_churn * 100))

    if prob_churn > 0.65:
        st.error("⚠️ High Risk Customer")
    elif prob_churn > 0.35:
        st.warning("⚠️ Moderate Risk Customer")
    else:
        st.success("✅ Low Risk Customer")

# Footer
st.markdown("---")
st.caption("Customer Churn Prediction Model | Machine Learning Deployment")