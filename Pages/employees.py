# import streamlit as st
# import sqlite3
# import pandas as pd

# # --- CSS Styling ---
# st.markdown(
#     """
#     <style>
#     .title {
#         font-size: 36px !important;
#         color: #4B0082;
#         text-align: center;
#     }
#     .stDataFrame {
#         border-radius: 10px;
#         overflow: hidden;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # --- Database Connection ---
# conn = sqlite3.connect("users.db")

# st.markdown('<p class="title">👥 Employee Directory</p>', unsafe_allow_html=True)

# df = pd.read_sql_query("SELECT id, name, email FROM users", conn)
# st.dataframe(df.style.set_properties(**{"border-radius": "10px"}))

# conn.close()



import streamlit as st
import sqlite3
import pandas as pd
import smtplib
import ssl
from email.message import EmailMessage
import os

# --- Database Connection ---
conn = sqlite3.connect("pages/users.db", check_same_thread=False)
cursor = conn.cursor()

st.title("👥 Employee Directory")

# Function to Fetch Employee Data
def fetch_employee_data():
    return pd.read_sql_query("SELECT id, name, email FROM users", conn)

# def fetch_employee_data():
#     conn = sqlite3.connect("pages/users.db")
#     df = pd.read_sql_query("SELECT id, name, email FROM users", conn)
#     conn.close()

#     if df.empty:
#         st.warning("⚠ No employee data found in the database. Email will not be sent.")
#         return None  # Prevent sending empty files
#     return df



#Function to Export Employee Data to Excel
def export_to_excel(df):
    file_path = "employees.xlsx"
    df.to_excel(file_path, index=False)
    return file_path

# def export_to_excel(df):
#     file_path = "employees.xlsx"
#     if df is None:
#         st.error("❌ Cannot generate Excel file: No employee data available.")
#         return None

#     try:
#         df.to_excel(file_path, index=False)
#         if os.path.exists(file_path):
#             st.success(f"✅ Excel file generated at: {file_path}")
#             return file_path
#         else:
#             st.error("❌ Failed to generate the Excel file.")
#             return None
#     except Exception as e:
#         st.error(f"❌ Error generating Excel file: {e}")
#         return None


# Fetch Employee Data
df = fetch_employee_data()

# Display Employee Table only once
if df is not None and not df.empty:
    st.dataframe(df)
else:
    st.error("❌ No employee data available.")


# # Fetch Employee Data
# df = fetch_employee_data()

# # Debugging: Check if data is fetched
# if df is not None:
#     st.write("Fetched Employee Data:", df)  # Show data in Streamlit
# else:
#     st.error("❌ No employee data available.")


# Function to Send Email with Updated Excel
def send_email_with_attachment(receiver_email):
    sender_email = "prasthuthi593@gmail.com"  # Change this
    sender_password = "zzzw lgxz viuz emgf"  # Use an app password for security
    subject = "Updated Employee List"
    body = "Attached is the latest employee data."

    # Export to Excel
    file_path = export_to_excel(fetch_employee_data())

    # Ensure file exists before sending
    if not os.path.exists(file_path):
        st.error("Error: Excel file not found.")
        return

    # Create Email
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(body)

    # Attach Excel File
    with open(file_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename="employees.xlsx")

    # Send Email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        st.success("📧 Employee list sent to the owner!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

# def send_email_with_attachment(receiver_email):
#     sender_email = "prasthuthi593@gmail.com"  # Change this
#     sender_password = "zzzw lgxz viuz emgf"  # Use an app password for security
#     subject = "Updated Employee List"
#     body = "Attached is the latest employee data."

#     st.write(f"Sending Email to: {receiver_email}")  # Debugging step


#     # Generate Excel File
#     df = fetch_employee_data()
#     file_path = export_to_excel(df)

#     if not file_path or not os.path.exists(file_path):
#         st.error("❌ Error: Excel file not found or not generated.")
#         return

#     # Create Email
#     msg = EmailMessage()
#     msg["Subject"] = subject
#     msg["From"] = sender_email
#     msg["To"] = receiver_email
#     msg.set_content(body)

#     try:
#         with open(file_path, "rb") as f:
#             msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename="employees.xlsx")

#         context = ssl.create_default_context()
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#             server.login(sender_email, sender_password)
#             server.send_message(msg)

#         st.success("📧 Employee list sent successfully!")
#     except Exception as e:
#         st.error(f"❌ Failed to send email: {e}")


# Check for new employees
if "last_employee_count" not in st.session_state:
    st.session_state.last_employee_count = cursor.execute("SELECT COUNT(*) FROM users").fetchone()[0]

current_count = cursor.execute("SELECT COUNT(*) FROM users").fetchone()[0]

if current_count > st.session_state.last_employee_count:
    owner_email = "prasthuthi2003@gmail.com"  # Change this
    send_email_with_attachment(owner_email)
    st.session_state.last_employee_count = current_count  # Update count

# # Display Employee Table
# df = fetch_employee_data()
# st.dataframe(df)
