
import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Employee Dashboard", layout="wide")

# Title
st.title("📊 Employee Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("employee_data.csv", parse_dates=["DoJ", "EndDate", "Dob"])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
departments = st.sidebar.multiselect("Department", df['Department'].unique(), default=df['Department'].unique())
genders = st.sidebar.multiselect("Gender", df['Gender'].unique(), default=df['Gender'].unique())
statuses = st.sidebar.multiselect("Status", df['status'].unique(), default=df['status'].unique())
categories = st.sidebar.multiselect("Category", df['Category'].unique(), default=df['Category'].unique())


filtered = df[
    (df['Department'].isin(departments)) &
    (df['Gender'].isin(genders)) &
    (df['status'].isin(statuses)) &
    (df['Category'].isin(categories))
]

# Show filtered data
st.subheader("📋 Filtered Employee Data")
st.dataframe(filtered)

# Charts section
st.markdown("## 📈 Visual Insights")

# Bar chart: Employees per Department
dept_counts = filtered['Department'].value_counts().reset_index()
dept_counts.columns = ['Department', 'Count']
fig1 = px.bar(dept_counts, x='Department', y='Count', title='Employees per Department')
st.plotly_chart(fig1, use_container_width=True)

# Pie chart: Gender distribution
gender_counts = filtered['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']
fig2 = px.pie(gender_counts, names='Gender', values='Count', title='Gender Distribution')
st.plotly_chart(fig2, use_container_width=True)

# Bar chart: Average salary by Designation
avg_salary = filtered.groupby("Designation")["Salary"].mean().reset_index()
fig3 = px.bar(avg_salary, x="Designation", y="Salary", title="Average Salary by Designation")
st.plotly_chart(fig3, use_container_width=True)
