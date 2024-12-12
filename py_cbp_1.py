import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

st.set_page_config(
    page_title="Employee Productivity Prediction",
    page_icon="📊",
    layout="centered"
)

# Load dataset
data = pd.read_csv("employee_productivity_data.csv")
data["stress_level"] = pd.to_numeric(data["stress_level"], errors="coerce")
data["working_hours"] = pd.to_numeric(data["working_hours"], errors="coerce")
data["leaves_taken"] = pd.to_numeric(data["leaves_taken"], errors="coerce")
data["productivity_rate"] = pd.to_numeric(data["productivity_rate"], errors="coerce")

# Model training
X = data[["stress_level", "working_hours", "leaves_taken"]]
y = data["productivity_rate"]

model = LinearRegression()
model.fit(X, y)

# UI and Prediction
st.image(
    "https://www.activtrak.com/cdn-cgi/image/quality=80,width=1024,format=webp-content/uploads/2024/05/"
    "blog-header-how-employee-satisfaction-and-productivity-are-connected-q224.jpg",
    use_column_width=True
)

st.title("📈 Predicting Employee Productivity")
st.subheader("Enter the following details")

# User Inputs
stress_level = st.number_input("Stress Level", min_value=0, max_value=10, step=1)
working_hours = st.number_input("Working Hours", min_value=0, max_value=12)
leaves_taken = st.number_input("No. of Leaves Taken", min_value=0, max_value=30)
predict = st.button("Predict Productivity")

# Prediction and visualization
if predict:
    if stress_level >= 0 and working_hours > 0 and leaves_taken >= 0:
        prediction = model.predict([[stress_level, working_hours, leaves_taken]])
        st.markdown(f"""
        <div class="prediction-box">
            <h2>Predicted Productivity Level:</h2>
            <h3>{prediction[0]:.2f}</h3>
        </div>
        """, unsafe_allow_html=True)

    # Visualization: Scatter Plot
    st.subheader("Working Hours vs Productivity Rate")
    fig, ax = plt.subplots()
    ax.scatter(data["working_hours"], data["productivity_rate"], color="skyblue", label="Actual Data", edgecolor="black")
    ax.set_xlabel("Working Hours", fontsize=12, labelpad=10)
    ax.set_ylabel("Productivity Rate", fontsize=12, labelpad=10)
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)

    st.write("")
