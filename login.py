import streamlit as st
import sqlite3
import pandas as pd
import smtplib
import ssl
from email.message import EmailMessage
import os
import hashlib 

# --- CSS Styling ---
st.markdown(
    """
    <style>
    body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        # background-color: #121212;
        background-color: #f0f2f6;
    }
    
    .title {
        font-size: 36px !important;
        color: #4CAF50;
        text-align: center;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 10px;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
   
    </style>
    
    """,
    unsafe_allow_html=True
)

# --- Database Connection ---
conn = sqlite3.connect("pages/users.db")
c = conn.cursor()

def hash_password(password):
    # return hashlib.sha256(password.encode()).hexdigest()
    if not password:  # Handle None or empty values
        return None
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(email, password):
    c.execute("SELECT * FROM users WHERE email=? AND password=?", 
              (email, hash_password(password)))
    return c.fetchone()

# --- Login Page ---
st.markdown('<p class="title">🔐 Login to Your Account</p>', unsafe_allow_html=True)


with st.form("login_form"):
    email = st.text_input("📧 Email", placeholder="Enter your email")
    password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")
    submit = st.form_submit_button("Login")

if submit:
    user = authenticate_user(email, password)
# if submit:
#     if not email or not password:  # Ensure both fields are filled
#         st.error("❌ Email and Password are required.")
#     else:
#         user = authenticate_user(email, password)
    if user:
        st.session_state["logged_in"] = True
        st.session_state["user_name"] = user[1]
        st.session_state["user_email"] = user[2]  # Store email
        st.success(f"✅ Welcome, {user[1]}!")
        # st.write(f"Entered Password: {password}")  # Debugging

        st.page_link("pages/monitor.py", label="➡ Go to Monitoring")
    else:
        st.error("❌ Invalid credentials. Please try again.")

conn.close()