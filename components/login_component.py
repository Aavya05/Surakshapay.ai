import streamlit as st

def render_login_component(key=None):   # ✅ accept key
    st.subheader("🔐 Login")

    username = st.text_input("Username", key=f"{key}_user" if key else "user")
    password = st.text_input("Password", type="password", key=f"{key}_pass" if key else "pass")

    if st.button("Login", key=f"{key}_btn" if key else "btn"):
        if username == "admin" and password == "admin":
            st.success("Login successful!")
            return {"status": "success", "user": username}
        else:
            st.error("Invalid credentials")
            return {"status": "failed"}

    return None
