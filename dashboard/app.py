
import streamlit as st
import pandas as pd
import numpy as np
import sys
import os

# Fix import path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

# Load data correctly
data_path = os.path.join(BASE_DIR, "data", "transactions.csv")
df = pd.read_csv(data_path)

# ✅ Load model accuracy
accuracy_file = os.path.join(BASE_DIR, "app", "ml", "accuracy.txt")

if os.path.exists(accuracy_file):
    with open(accuracy_file, "r") as f:
        accuracy = float(f.read())

    st.subheader("Model Performance")
    st.write(f"Model Accuracy: {accuracy * 100:.2f}%")
else:
    st.write("⚠ Model accuracy not found. Please train model.")


from app.services.ml_predictor import predict_category
from app.services.advisor import generate_advice





st.title("SpendWise AI Dashboard")


# ✅ STEP 1: Apply AI category classification
df['category'] = df['description'].apply(predict_category)

# ✅ STEP 2: Summary
st.subheader("Summary")

total_income = df[df['type']=='credit']['amount'].sum()
total_expense = df[df['type']=='debit']['amount'].sum()

st.write(f"Total Income: ₹{total_income}")
st.write(f"Total Expense: ₹{total_expense}")
st.write(f"Total Records: {len(df)}")

# ✅ STEP 3: Show sample data
st.subheader("Sample Data")
st.dataframe(df.head(20))

# ✅ STEP 4: Category analysis
st.subheader("Expense by Category")

expense_df = df[df['type']=='debit']
category_summary = expense_df.groupby('category')['amount'].sum()

st.bar_chart(category_summary)

# ✅ STEP 5: Top spending category
top_category = category_summary.idxmax()
st.subheader("Top Category")
st.write(f"You spend most on: {top_category}")

# ✅ STEP 6: Anomaly detection (AI logic)
mean = df['amount'].mean()
std = df['amount'].std()

df['z_score'] = (df['amount'] - mean) / std
anomalies = df[df['z_score'] > 2]

st.subheader("Unusual Transactions")
st.dataframe(anomalies.head(10))

# ✅ STEP 7: Subscription detection
subscription_df = df[df['category'] == 'Subscription']

st.subheader("Subscriptions")
st.write(subscription_df.groupby('description')['amount'].mean())

# ✅ STEP 8: AI Advice
advice = generate_advice(total_expense, top_category)

st.subheader("AI Financial Advice")
st.write(advice)

# ✅ STEP 9: Monthly Trend
df['date'] = pd.to_datetime(df['date'])
monthly = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()

st.subheader("Monthly Spending Trend")
st.line_chart(monthly)
