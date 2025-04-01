import streamlit as st
import pandas as pd
import joblib

# Load trained model and scaler
model = joblib.load("fraud_detection_model.pkl")
scaler = joblib.load("scaler.pkl")

# -------------------- Custom CSS for Modern UI --------------------
st.markdown("""
    <style>
        /* Background Gradient */
        body {
            background: linear-gradient(to right, #141e30, #243b55);
            color: white;
        }

        /* Header */
        .main-title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #00c6ff;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }

        /* Transaction Form Card */
        .form-container {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
        }

        /* Modern Button */
        .stButton>button {
            background: linear-gradient(to right, #00c6ff, #0072ff);
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 24px;
            border: none;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        }

        .stButton>button:hover {
            background: linear-gradient(to right, #0072ff, #00c6ff);
            transform: scale(1.05);
            transition: 0.3s ease-in-out;
        }

        /* Prediction Result */
        .result-box {
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }

        .legit {
            background: rgba(0, 255, 0, 0.2);
            color: #00ff00;
        }

        .fraud {
            background: rgba(255, 0, 0, 0.2);
            color: #ff0000;
        }

    </style>
""", unsafe_allow_html=True)

# -------------------- UI Layout --------------------
st.markdown("<h1 class='main-title'>💳 New Age Bank - Fraud Detection System</h1>", unsafe_allow_html=True)

st.markdown("### 🔍 Enter Transaction Details to Detect Fraud")

with st.container():
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)

    # Input fields
    amount = st.number_input("💰 Transaction Amount ($)", min_value=0.1, max_value=10000.0, value=50.0)
    transaction_type = st.selectbox("🔄 Transaction Type", ["Online", "ATM", "POS"])
    location = st.selectbox("📍 Transaction Location", ["New York", "Los Angeles", "San Francisco", "Chicago", "Miami", "Houston", "Seattle", "Boston", "Denver", "Atlanta"])
    card_type = st.selectbox("💳 Card Type", ["Credit", "Debit"])
    merchant_category = st.selectbox("🏪 Merchant Category", ["Groceries", "Electronics", "Travel", "Fashion", "Restaurants", "Automotive", "Entertainment"])

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------- Data Processing --------------------
data = pd.DataFrame({
    "Amount": [amount],
    "TransactionType_ATM": [1 if transaction_type == "ATM" else 0],
    "TransactionType_POS": [1 if transaction_type == "POS" else 0],
    "TransactionType_Online": [1 if transaction_type == "Online" else 0],
    "Location_New York": [1 if location == "New York" else 0],
    "Location_Los Angeles": [1 if location == "Los Angeles" else 0],
    "Location_San Francisco": [1 if location == "San Francisco" else 0],
    "Location_Chicago": [1 if location == "Chicago" else 0],
    "Location_Miami": [1 if location == "Miami" else 0],
    "Location_Houston": [1 if location == "Houston" else 0],
    "Location_Seattle": [1 if location == "Seattle" else 0],
    "Location_Boston": [1 if location == "Boston" else 0],
    "Location_Denver": [1 if location == "Denver" else 0],
    "Location_Atlanta": [1 if location == "Atlanta" else 0],
    "CardType_Credit": [1 if card_type == "Credit" else 0],
    "CardType_Debit": [1 if card_type == "Debit" else 0],
    "MerchantCategory_Groceries": [1 if merchant_category == "Groceries" else 0],
    "MerchantCategory_Electronics": [1 if merchant_category == "Electronics" else 0],
    "MerchantCategory_Travel": [1 if merchant_category == "Travel" else 0],
    "MerchantCategory_Fashion": [1 if merchant_category == "Fashion" else 0],
    "MerchantCategory_Restaurants": [1 if merchant_category == "Restaurants" else 0],
    "MerchantCategory_Automotive": [1 if merchant_category == "Automotive" else 0],
    "MerchantCategory_Entertainment": [1 if merchant_category == "Entertainment" else 0]
})

# Scale the amount
data["Amount"] = scaler.transform(data[["Amount"]])

# -------------------- Make Prediction --------------------
if st.button("🚀 Check for Fraud"):
    prediction = model.predict(data)
    if prediction[0] == 1:
        st.markdown("<div class='result-box fraud'>⚠️ Fraudulent Transaction Detected!</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result-box legit'>✅ Legitimate Transaction</div>", unsafe_allow_html=True)
