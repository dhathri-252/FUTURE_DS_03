import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/marketing_funnel.csv")

# Calculate conversion rate
df["ConversionRate"] = (df["Conversions"] / df["Visitors"]) * 100

# Title
st.title("Marketing Funnel & Conversion Dashboard")

# Dataset
st.subheader("Marketing Funnel Dataset")
st.write(df)

# KPI Metrics
total_visitors = df["Visitors"].sum()
total_leads = df["Leads"].sum()
total_conversions = df["Conversions"].sum()

overall_conversion = (total_conversions / total_visitors) * 100

st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Visitors", total_visitors)
col2.metric("Leads", total_leads)
col3.metric("Conversions", total_conversions)
col4.metric("Conversion Rate", f"{overall_conversion:.2f}%")

# Bar Chart
st.subheader("Conversions by Channel")

fig, ax = plt.subplots()
ax.bar(df["Channel"], df["Conversions"])

plt.xticks(rotation=20)

st.pyplot(fig)

# Funnel Visualization
st.subheader("Marketing Funnel")

funnel_values = [
    total_visitors,
    total_leads,
    total_conversions
]

funnel_labels = [
    "Visitors",
    "Leads",
    "Conversions"
]

fig2, ax2 = plt.subplots()
ax2.plot(funnel_labels, funnel_values, marker='o')

st.pyplot(fig2)

# Conversion Rate Table
st.subheader("Channel Conversion Rates")

st.write(df[["Channel", "ConversionRate"]])