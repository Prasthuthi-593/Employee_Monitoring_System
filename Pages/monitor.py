<<<<<<< HEAD
# import streamlit as st

# import cv2
# import smtplib
# from email.message import EmailMessage
# from datetime import datetime


# # --- CSS Styling ---
# st.markdown(
#     """
#     <style>
#     .title {
#         font-size: 36px !important;
#         color: #FF4500;
#         text-align: center;
#     }
#     .stButton>button {
#         background-color: #FF4500;
#         color: white;
#         font-size: 18px;
#         border-radius: 10px;
#         width: 100%;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # --- Monitoring Page ---
# st.markdown('<p class="title">📡 Real-Time Monitoring</p>', unsafe_allow_html=True)

# def capture_snapshot():
#     cap = cv2.VideoCapture(0)
#     ret, frame = cap.read()
#     if ret:
#         image_path = "login_snapshot.jpg"
#         cv2.imwrite(image_path, frame)
#     cap.release()
#     return image_path if ret else None

# def send_login_email(employee_name, image_path):
#     sender_email = "prasthuthi593@gmail.com"
#     sender_password = "zzzw lgxz viuz emgf"
#     recipient_email = "prasthuthi2003@gmail.com"
#     subject = f"This is to inform you that {employee_name} has logged in."
#     body = f"Employee {employee_name} logged in at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."

#     msg = EmailMessage()
#     msg["Subject"] = subject
#     msg["From"] = sender_email
#     msg["To"] = recipient_email
#     msg.set_content(body)

#     if image_path:
#         with open(image_path, "rb") as f:
#             msg.add_attachment(f.read(), maintype="image", subtype="jpeg", filename="snapshot.jpg")

#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#         server.login(sender_email, sender_password)
#         server.send_message(msg)

# if "logged_in" in st.session_state and st.session_state["logged_in"]:
#     employee_name = st.session_state.get("user_name", "User")
#     st.info(f"👋 Welcome, {employee_name}! Click below to start monitoring.")

#     if st.button("🚀 Start Monitoring"):
#         snapshot = capture_snapshot()
#         send_login_email(employee_name, snapshot)
#         st.success(f"📧 Login email sent for {employee_name}")
#         st.success("🔍 Launching real-time monitoring...")
#         exec(open("posture.py").read())
# else:
#     st.error("❌ Please log in to access monitoring.")


import streamlit as st
import cv2
import smtplib
from email.message import EmailMessage
from datetime import datetime
import os

# --- CSS Styling ---
st.markdown(
    """
    <style>
    .title {
        font-size: 36px !important;
        color: #FF4500;
        text-align: center;
    }
    .stButton>button {
        background-color: #FF4500;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Monitoring Page ---
st.markdown('<p class="title">📡 Real-Time Monitoring</p>', unsafe_allow_html=True)

def capture_snapshot(filename="snapshot.jpg"):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
    cap.release()
    return filename if ret else None

def send_email(employee_name, action, image_path):
    sender_email = "prasthuthi593@gmail.com"
    sender_password = "zzzw lgxz viuz emgf"
    recipient_email = "prasthuthi2003@gmail.com"
    subject = f"Employee {employee_name} {action}"
    body = f"Employee {employee_name} {action} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg.set_content(body)

    if image_path and os.path.exists(image_path):
        with open(image_path, "rb") as f:
            msg.add_attachment(f.read(), maintype="image", subtype="jpeg", filename=image_path)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

if "logged_in" in st.session_state and st.session_state["logged_in"]:
    employee_name = st.session_state.get("user_name", "User")
    st.info(f"👋 Welcome, {employee_name}! Click below to start monitoring.")

    if st.button("🚀 Start Monitoring"):
        snapshot = capture_snapshot("login_snapshot.jpg")
        send_email(employee_name, "logged in", snapshot)
        st.success(f"📧 Login email sent for {employee_name}")
        st.success("🔍 Launching real-time monitoring...")
        exec(open("posture.py").read())
        
    if st.button("⏹ Stop Monitoring"):
        snapshot = capture_snapshot("logout_snapshot.jpg")
        send_email(employee_name, "logged off", snapshot)
        st.success(f"📧 Logout email sent for {employee_name}")
        st.warning("🔴 Monitoring stopped.")
else:
    st.error("❌ Please log in to access monitoring.")
=======

import streamlit as st
import cv2
import smtplib
from email.message import EmailMessage
from datetime import datetime
import os

# --- CSS Styling ---
st.markdown(
    """
    <style>
    .title {
        font-size: 36px !important;
        color: #FF4500;
        text-align: center;
    }
    .stButton>button {
        background-color: #FF4500;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Monitoring Page ---
st.markdown('<p class="title">📡 Real-Time Monitoring</p>', unsafe_allow_html=True)

def capture_snapshot(filename="snapshot.jpg"):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
    cap.release()
    return filename if ret else None

def send_email(employee_name, action, image_path):
    sender_email = "prasthuthi593@gmail.com"
    sender_password = "yrhd agdh orpq"  ## use your gmail app password
    recipient_email = "prasthuthi2003@gmail.com"
    subject = f"Employee {employee_name} {action}"
    body = f"Employee {employee_name} {action} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg.set_content(body)

    if image_path and os.path.exists(image_path):
        with open(image_path, "rb") as f:
            msg.add_attachment(f.read(), maintype="image", subtype="jpeg", filename=image_path)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

if "logged_in" in st.session_state and st.session_state["logged_in"]:
    employee_name = st.session_state.get("user_name", "User")
    st.info(f"👋 Welcome, {employee_name}! Click below to start monitoring.")

    if st.button("🚀 Start Monitoring"):
        snapshot = capture_snapshot("login_snapshot.jpg")
        send_email(employee_name, "logged in", snapshot)
        st.success(f"📧 Login email sent for {employee_name}")
        st.success("🔍 Launching real-time monitoring...")
        exec(open("posture.py").read())
        
    if st.button("⏹ Stop Monitoring"):
        snapshot = capture_snapshot("logout_snapshot.jpg")
        send_email(employee_name, "logged off", snapshot)
        st.success(f"📧 Logout email sent for {employee_name}")
        st.warning("🔴 Monitoring stopped.")
else:
    st.error("❌ Please log in to access monitoring.")
>>>>>>> d2893ca2bbb79b7bd0b361e9de0ff40386f753b7
