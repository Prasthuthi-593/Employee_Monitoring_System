
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Employee Monitoring System",
    page_icon="📷",
    layout="wide"
)

# --- Custom CSS for Styling ---
st.markdown(
    """
    <style>
    /* Background Styling */
    .stApp {
        background: linear-gradient(to right, #00c6ff, #0072ff);
        color: white;
    }
    
    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background: #222831;
        color: white;
    }
    
    /* Title Styling */
    .title {
        font-size: 45px !important;
        color: #ffffff;
        text-align: center;
        font-weight: bold;
    }

    /* Image Styling */
    .custom-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 60%; /* Reduce image size */
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
    }

    /* Button Container (Centered Below Image) */
    .button-container {
        display: flex;
        justify-content: center;
        gap: 20px;  /* Space between buttons */
        margin-top: 20px; /* Adjust spacing from image */
    }

    /* Button Styling */
    .stButton>button {
        background-color: #FFD700 !important;
        color: black !important;
        font-size: 20px;
        border-radius: 10px;
        font-weight: bold;
        width: 220px;
        height: 55px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Navigation ---
st.sidebar.title("🔍 Navigation")
st.sidebar.page_link("pages/login.py", label="🔐 Login")
st.sidebar.page_link("pages/signup.py", label="📝 Sign Up")
st.sidebar.page_link("pages/employees.py", label="👥 View Employees")
st.sidebar.page_link("pages/monitor.py", label="📡 Real-Time Monitoring")

# --- Main Content ---
st.markdown('<p class="title">📷 Welcome to the Employee Monitoring System</p>', unsafe_allow_html=True)

# --- Reduced-Size Image ---
st.markdown(
    """
    <img src="https://cdn.prod.website-files.com/6229d00c46440bc58f8e8071/63523c2e505af34a88726b30_What%20is%20Stealth%20mode%20in%20Employee%20Monitoring%20Software%3F.jpg" 
    class="custom-image">
    """,
    unsafe_allow_html=True
)

# --- Centered Buttons Below Image ---
st.markdown('<div class="button-container">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 2])  # Centering Trick
with col2:
    login_clicked = st.button("🔐 Login")
    signup_clicked = st.button("📝 Sign Up")

st.markdown('</div>', unsafe_allow_html=True)

# --- Redirect when a button is clicked ---
if login_clicked:
    st.switch_page("pages/login.py")

if signup_clicked:
    st.switch_page("pages/signup.py")

