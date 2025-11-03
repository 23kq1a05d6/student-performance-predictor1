import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, r2_score

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓", layout="wide")

# -------------------------------
# UI Styling
# -------------------------------
st.markdown("""
<style>
body {background: linear-gradient(120deg, #eef2f3, #ffffff); font-family: 'Poppins', sans-serif; color: #222;}
.main {background-color: rgba(255,255,255,0.8); padding: 2rem; border-radius: 20px; box-shadow: 0px 6px 20px rgba(0,0,0,0.1);}
h1,h2,h3,h4 {color: #004aad;}
.stButton > button {background: linear-gradient(90deg, #004aad, #0074e4); color:white !important; border:none; border-radius:12px; padding:10px 20px; font-size:1.05em; transition:0.3s;}
.stButton > button:hover {background: linear-gradient(90deg, #0074e4, #00aaff); transform: scale(1.03);}
.result-box {background:white; border-radius:15px; padding:25px; text-align:center; box-shadow:0px 4px 15px rgba(0,0,0,0.1);}
.result-label {color:#004aad; font-weight:600; font-size:1.2em;}
.result-value {font-size:2em; font-weight:700;}
.pass {color:#0c9a40;}
.fail {color:#e63946;}
.info-card {background: rgba(255,255,255,0.9); border-radius:12px; padding:15px; box-shadow:0px 2px 10px rgba(0,0,0,0.05);}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.markdown("<h1 style='text-align:center;'>🎓 Student Performance Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Predict semester percentage and pass/fail outcome using academic details.</p>", unsafe_allow_html=True)
st.markdown("---")

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    try:
        data = pd.read_csv("student_data.csv")
        return data
    except FileNotFoundError:
        st.error("❌ student_data.csv not found")
        st.stop()

data = load_data()

# -------------------------------
# Model Training
# -------------------------------
@st.cache_resource
def train_models(data):
    X = data[["Attendance","PreviousCGPA","StudyHours","Assignments","Mid1Marks","Mid2Marks","QuizScores"]]
    y_class = data["PassFail"]
    y_reg = data["SemesterPercentage"]

    X_train, X_test, y_train_class, y_test_class, y_train_reg, y_test_reg = train_test_split(
        X, y_class, y_reg, test_size=0.2, random_state=42
    )

    clf = RandomForestClassifier(n_estimators=250, random_state=42)
    reg = RandomForestRegressor(n_estimators=250, random_state=42)

    clf.fit(X_train, y_train_class)
    reg.fit(X_train, y_train_reg)

    acc = accuracy_score(y_test_class, clf.predict(X_test))
    r2 = r2_score(y_test_reg, reg.predict(X_test))

    return clf, reg, acc, r2

clf, reg, acc, r2 = train_models(data)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("📈 Model Info")
st.sidebar.metric("Pass/Fail Accuracy", f"{acc*100:.1f}%")
st.sidebar.metric("R² Score", f"{r2:.2f}")
st.sidebar.info("🤖 Random Forest Model")

# -------------------------------
# User Input
# -------------------------------
st.markdown("## 🧾 Enter Student Details")

col1, col2 = st.columns(2)
with col1:
    attendance = st.number_input("📅 Attendance (%)", 0, 100, 85)
    previous_cgpa = st.number_input("🎓 Previous CGPA", 0.0, 10.0, 8.2, step=0.1)
    study_hours = st.number_input("⏰ Study Hours per Week", 0, 60, 10)
with col2:
    assignments = st.number_input("📝 Assignment Completion (%)", 0, 100, 90)
    quiz = st.number_input("🧠 Quiz/Test Score (out of 30)", 0, 30, 25)

# -------------------------------
# Mid Marks Section
# -------------------------------
st.markdown("## 📝 Enter Mid Marks (out of 30)")

num_subjects = st.number_input("Number of Subjects", 1, 10, 5)
mid1_marks, mid2_marks = [], []

cols = st.columns(min(num_subjects, 5))
for i in range(num_subjects):
    with cols[i % 5]:
        m1 = st.number_input(f"Subject {i+1} Mid1 Marks", 0, 30, 25)
        m2 = st.number_input(f"Subject {i+1} Mid2 Marks", 0, 30, 28)
        mid1_marks.append(m1)
        mid2_marks.append(m2)

total_mid1 = sum(mid1_marks)
total_mid2 = sum(mid2_marks)

st.markdown(f"""
<div class="info-card">
<b>Total Mid1 Marks:</b> {total_mid1}/{num_subjects*30} <br>
<b>Total Mid2 Marks:</b> {total_mid2}/{num_subjects*30}
</div>
""", unsafe_allow_html=True)

# -------------------------------
# Prediction
# -------------------------------
st.markdown("---")
st.markdown("## 🎯 Prediction")

if st.button("✨ Predict Result"):
    user_data = np.array([[attendance, previous_cgpa, study_hours, assignments, total_mid1, total_mid2, quiz]])
    with st.spinner("🔍 Analyzing..."):
        predicted_percentage = reg.predict(user_data)[0]
        predicted_result = clf.predict(user_data)[0]

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='result-box'><div class='result-label'>Predicted Semester %</div><div class='result-value'>{predicted_percentage:.2f}%</div></div>", unsafe_allow_html=True)
    with col2:
        color_class = "pass" if predicted_result=="Pass" else "fail"
        st.markdown(f"<div class='result-box'><div class='result-label'>Predicted Result</div><div class='result-value {color_class}'>{'✅ PASS' if predicted_result=='Pass' else '❌ FAIL'}</div></div>", unsafe_allow_html=True)

    if predicted_result=="Pass":
        st.success("🎉 You are on track for success!")
    else:
        st.error("⚠ You might need to improve your study plan.")

