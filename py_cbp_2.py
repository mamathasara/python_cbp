import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# Sample data
data = pd.DataFrame({
    "stress_level": ["Low", "Medium", "High"],
    "productivity_rate": [80, 60, 40]
})

# Visualization 2: Bar Chart
if not data.empty:
    avg_productivity = data.groupby("stress_level")["productivity_rate"].mean()
    st.subheader("Average Productivity by Stress Level")
    fig, ax = plt.subplots()
    ax = avg_productivity.plot(kind="bar", color="#65a67a", edgecolor="black", ax=ax)
    ax.set_xlabel("Stress Level", fontsize=12, labelpad=10)
    ax.set_ylabel("Average Productivity Rate", fontsize=12, labelpad=10)
    plt.xticks(rotation=0)
    st.pyplot(fig)
else:
    st.write("Please enter valid inputs")

# Styling
st.markdown("""
<style>
/* Apply a gradient background to the entire page */
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #e0f7fa, #1ebee7);
    color: #12327e;
}

/* Prediction box styling */
.prediction-box {
    background-color: #ffeb3b;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    color: #12327e;
    font-weight: bold;
    box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2);
}

/* Title and subheader styling */
.stTitle { color: #12327e; font-family: 'Poppins', sans-serif; text-align: center; }
.stSubheader { color: #3949ab; font-family: 'Arial', sans-serif; text-align: center; margin-top: 10px; }

/* Button styling */
.stButton button {
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 8px 20px;
}

.stButton button:hover {
    background-color: #388e3c;
}
</style>
""", unsafe_allow_html=True)
