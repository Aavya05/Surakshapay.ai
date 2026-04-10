import streamlit as st

def render_login():
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.success("Login successful!")
            return True
        else:
            st.error("Invalid credentials")
            return False

    return False
