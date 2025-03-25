import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Student Data Generator", layout="wide")
st.markdown('<h1 style="color:blue;">💾 Student CSV File Generator 📜</h1>', unsafe_allow_html=True)

names = ["Umaima Khan", "Shahana Tariq", "Umer Khan", "Ambreen Gul", "Adnan Ishrat", "Ayesha Khalil", "Ali Ahmad", "Khalid Mahboob", "Kabir Khan", "Farhan Ali", "Sami Ullah", "Alishba Naz","Tanzeela Bano"]

# Create an empty list to hold all student data
students = []
for i in range(11):
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A", "B", "C", "D", "E"]),
        "Marks": random.randint(50, 100)
    }
    students.append(student)  # Append the student dictionary to the list

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(students)
st.markdown('<h3 style="color: orange;">Generated Student Data</h3>', unsafe_allow_html=True)
st.dataframe(df)

# Generate CSV file
csv_file = df.to_csv(index=False).encode("utf-8")  # Corrected typo: `cncode` to `encode`
st.download_button("Download CSV File", csv_file, "student.csv", "text/csv")
st.markdown("""
    <div style="background-color: green; padding: 10px; border-radius: 5px; text-align: center; font-size: 24px; color: white;">
        <b>🥇 Student Record Generated Successfully</b> || <i>By Muhammad Tariq Mahboob</i>
    </div>
""", unsafe_allow_html=True)
