import plotly.express as px

def plot_transactions_over_time(df):
    return px.line(df)

def plot_fraud_distribution(df):
    return px.histogram(df)

def plot_amount_distribution(df):
    return px.histogram(df)
