# Employee Monitoring System - Setup and Installation Guide

This guide will walk you through setting up and running the Employee Monitoring System project. The project includes:

- **Streamlit Frontend** for user interface (runs on **port 8501**)
- **Webcam-based Monitoring Module** using YOLOv8 and Dlib
- **SQLite Database** to store user information

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your system:

- ✅ [Python 3.9](https://www.python.org/downloads/release/python-390/)
- ✅ [Git](https://git-scm.com/)
- ✅ Python packages: OpenCV, Dlib, Streamlit, Numpy, Pandas, Ultralytics
- ✅ A webcam (for real-time monitoring)

---

<<<<<<< HEAD
## Clone the Repository (or Download Files)

If hosted on GitHub:

```bash
git clone https://github.com/Prasthuthi-593/Employee_Monitoring_System.git


=======
>>>>>>> d2893ca2bbb79b7bd0b361e9de0ff40386f753b7
## 📁 Step 1: Choose Your Project Directory and Open Terminal

1. Select the directory where you want to install the Employee Monitoring project.  
2. Open a **Command Prompt or Terminal** in that selected directory.

---

## ⚙️ Step 2: Install Required Dependencies

Run the following:

```bash
pip install streamlit opencv-python dlib pandas numpy ultralytics
pip install ./dlib-19.22.99-cp39-cp39-win_amd64.whl  # Local Dlib wheel
```

> Make sure `shape_predictor_68_face_landmarks.dat` and `yolov8n.pt` are in the root directory.

---

## 🗃️ Step 3: Prepare the Database

The SQLite database file `users.db` is already located inside the `pages/` folder.

✅ No additional setup needed — it will auto-update with user sign-ups.

---

## 🚀 Step 4: Run the Streamlit Web App

In the root directory of the project, run:

```bash
streamlit run app.py
```

If that fails, try:

```bash
python -m streamlit run app.py
```

🖥️ This will launch the web UI at: [http://localhost:8501](http://localhost:8501)

---

## 🎥 Step 5: Start Posture Monitoring Manually (Optional)

If the real-time monitoring doesn’t start from the Streamlit interface or if you prefer to run it directly, use:

```bash
python posture.py
```

📸 This opens a webcam feed and shows posture alerts with live feedback.  
📧 Email alerts will be sent for any posture violations.

---

<<<<<<< HEAD
## 📬 Email Configuration (Optional)
=======
## 📬 Email Configuration 
>>>>>>> d2893ca2bbb79b7bd0b361e9de0ff40386f753b7

Update the email credentials in `posture.py` and `employees.py`:

```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use Gmail App Password
OWNER_EMAIL = "admin_email@example.com"
```

<<<<<<< HEAD
=======

>>>>>>> d2893ca2bbb79b7bd0b361e9de0ff40386f753b7
