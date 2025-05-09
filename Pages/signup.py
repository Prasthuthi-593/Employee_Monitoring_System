import streamlit as st
import sqlite3
import hashlib

# --- CSS Styling ---
st.markdown(
    """
    <style>
    .title {
        font-size: 36px !important;
        color: #1E90FF;
        text-align: center;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        width: 100%;
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
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name, email, password):
    try:
        c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", 
                  (name, email, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

# --- Signup Page ---
st.markdown('<p class="title">📝 Create an Account</p>', unsafe_allow_html=True)

with st.form("signup_form"):
    name = st.text_input("👤 Full Name", placeholder="Enter your full name")
    email = st.text_input("📧 Email", placeholder="Enter your email")
    password = st.text_input("🔑 Password", type="password", placeholder="Create a password")
    submit = st.form_submit_button("Sign Up")

if submit:
    if register_user(name, email, password):
        st.success("✅ Account created successfully! You can now log in.")
        st.page_link("pages/login.py", label="➡ Go to Login")
    else:
        st.error("❌ Email already exists. Please use a different one.")

conn.close()

# import streamlit as st
# import sqlite3
# import hashlib

# # --- CSS Styling ---
# st.markdown(
#     """
#     <style>
#     .signup-container {
#         max-width: 400px;
#         margin: auto;
#         padding: 40px;
#         background: #ffffff;
#         border-radius: 12px;
#         box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
#     }
#     .title {
#         font-size: 28px;
#         font-weight: bold;
#         text-align: center;
#         margin-bottom: 20px;
#     }
#     .stTextInput>div>div>input {
#         border-radius: 8px;
#         height: 40px;
#         border: 1px solid #ccc;
#     }
#     .stButton>button {
#         background-color: #007bff;
#         color: white;
#         font-size: 16px;
#         font-weight: bold;
#         border-radius: 8px;
#         padding: 10px;
#         width: 100%;
#     }
#     .login-text {
#         text-align: center;
#         font-size: 14px;
#         margin-top: 15px;
#     }
#     .login-text a {
#         color: #007bff;
#         text-decoration: none;
#         font-weight: bold;
#     }
#     body {
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             height: 100vh;
#             background-color: #121212;
#         }
#     .login-container {
#             max-width: 50%;
#             min-width: 400px;
#             padding: 20px;
#             background: #1e1e1e;
#             border-radius: 12px;
#             box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
#             text-align: center;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # --- Database Connection ---
# conn = sqlite3.connect("pages/users.db")
# c = conn.cursor()

# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# def register_user(employee_id, name, email, password):
#     try:
#         c.execute("INSERT INTO users (employee_id, name, email, password) VALUES (?, ?, ?, ?)", 
#                   (employee_id, name, email, hash_password(password)))
#         conn.commit()
#         return True
#     except sqlite3.IntegrityError:
#         return False

# # --- Signup Form ---
# st.markdown('<div class="signup-container">', unsafe_allow_html=True)
# st.markdown('<p class="title">Sign Up</p>', unsafe_allow_html=True)

# with st.form("signup_form"):
#     employee_id = st.text_input("Employee ID:", placeholder="Enter your Employee ID")
#     name = st.text_input("Name:", placeholder="Enter your full name")
#     email = st.text_input("Email:", placeholder="Enter your email")
#     password = st.text_input("Password:", type="password", placeholder="Create a password")
#     confirm_password = st.text_input("Confirm Password:", type="password", placeholder="Re-enter your password")
#     submit = st.form_submit_button("Sign Up")

# if submit:
#     if not employee_id or not name or not email or not password or not confirm_password:
#         st.error("❌ All fields are required!")
#     elif password != confirm_password:
#         st.error("❌ Passwords do not match!")
#     elif register_user(employee_id, name, email, password):
#         st.success("✅ Account created successfully! You can now log in.")
#         st.page_link("pages/login.py", label="➡ Go to Login")
#     else:
#         st.error("❌ Email already exists. Please use a different one.")

# st.markdown('<p class="login-text">Already have an account? <a href="pages/login.py">Login</a></p>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)

# conn.close()

