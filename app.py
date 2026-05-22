import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Snitch Dashboard",
    layout="wide"
)

st.title("Snitch D2C Growth Dashboard")

# Load CSV directly
df = pd.read_csv("funnel_data.csv")

# Group metrics
summary = df.groupby("category").agg({
    "viewed_pdp": "sum",
    "added_to_cart": "sum",
    "purchased": "sum"
}).reset_index()

summary.rename(columns={
    "viewed_pdp": "PDP Views",
    "added_to_cart": "Cart Adds",
    "purchased": "Purchases"
}, inplace=True)

# KPI Metrics
total_purchases = summary["Purchases"].sum()
total_cart = summary["Cart Adds"].sum()

conversion_rate = round(
    (total_purchases / total_cart) * 100,
    2
)

col1, col2 = st.columns(2)

col1.metric("Total Purchases", total_purchases)
col2.metric("Conversion Rate", f"{conversion_rate}%")

# Table
st.subheader("Category Performance")

st.dataframe(summary)

# Chart
fig = px.bar(
    summary,
    x="category",
    y="Purchases",
    title="Purchases by Category"
)

st.plotly_chart(fig)
