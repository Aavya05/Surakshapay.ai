import streamlit as st

def kpi_card(title, value):
    st.metric(title, value)

def fraud_alert_card(*args, **kwargs):
    pass
