import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Employee Attrition Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("EA.csv")

df = load_data()

st.title("📊 Employee Attrition Insights Dashboard")
st.markdown("This advanced dashboard delivers macro and micro-level insights on employee attrition, designed for HR leadership and stakeholders.")

# Sidebar filters
st.sidebar.header("🎛️ Filters")
departments = st.sidebar.multiselect("Department", df['Department'].unique(), default=df['Department'].unique())
genders = st.sidebar.multiselect("Gender", df['Gender'].unique(), default=df['Gender'].unique())
job_roles = st.sidebar.multiselect("Job Role", df['JobRole'].unique(), default=df['JobRole'].unique())

filtered_df = df[
    (df['Department'].isin(departments)) &
    (df['Gender'].isin(genders)) &
    (df['JobRole'].isin(job_roles))
]

# Tabs
macro, micro, advanced = st.tabs(["📊 Macro Trends", "🔍 Micro Analysis", "📈 Correlation & Drivers"])

with macro:
    st.subheader("1. Overall Attrition Rate")
    st.markdown("This pie chart shows the percentage of employees who have left vs stayed.")
    fig1 = px.pie(df, names="Attrition", hole=0.3)
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("2. Attrition by Department")
    fig2 = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("3. Attrition by Gender")
    fig3 = px.histogram(filtered_df, x="Gender", color="Attrition", barmode="group")
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("4. Attrition by Business Travel")
    fig4 = px.histogram(filtered_df, x="BusinessTravel", color="Attrition", barmode="group")
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("5. Attrition by Job Role")
    fig5 = px.histogram(filtered_df, x="JobRole", color="Attrition", barmode="group")
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("6. Attrition by Marital Status")
    fig6 = px.histogram(filtered_df, x="MaritalStatus", color="Attrition", barmode="group")
    st.plotly_chart(fig6, use_container_width=True)

    st.subheader("7. Age Distribution of Leavers")
    fig7 = px.histogram(filtered_df[filtered_df["Attrition"] == "Yes"], x="Age", nbins=30)
    st.plotly_chart(fig7, use_container_width=True)

    st.subheader("8. Salary Distribution of Leavers")
    fig8 = px.box(filtered_df, x="Attrition", y="MonthlyIncome", color="Attrition")
    st.plotly_chart(fig8, use_container_width=True)

with micro:
    st.subheader("9. Job Satisfaction vs Attrition")
    fig9 = px.histogram(filtered_df, x="JobSatisfaction", color="Attrition", barmode="group")
    st.plotly_chart(fig9, use_container_width=True)

    st.subheader("10. Work-Life Balance vs Attrition")
    fig10 = px.histogram(filtered_df, x="WorkLifeBalance", color="Attrition", barmode="group")
    st.plotly_chart(fig10, use_container_width=True)

    st.subheader("11. Job Involvement vs Attrition")
    fig11 = px.histogram(filtered_df, x="JobInvolvement", color="Attrition", barmode="group")
    st.plotly_chart(fig11, use_container_width=True)

    st.subheader("12. Relationship Satisfaction vs Attrition")
    fig12 = px.histogram(filtered_df, x="RelationshipSatisfaction", color="Attrition", barmode="group")
    st.plotly_chart(fig12, use_container_width=True)

    st.subheader("13. Years At Company")
    fig13 = px.box(filtered_df, x="Attrition", y="YearsAtCompany", color="Attrition")
    st.plotly_chart(fig13, use_container_width=True)

    st.subheader("14. Years in Current Role")
    fig14 = px.box(filtered_df, x="Attrition", y="YearsInCurrentRole", color="Attrition")
    st.plotly_chart(fig14, use_container_width=True)

    st.subheader("15. Years With Current Manager")
    fig15 = px.box(filtered_df, x="Attrition", y="YearsWithCurrManager", color="Attrition")
    st.plotly_chart(fig15, use_container_width=True)

    st.subheader("16. Years Since Last Promotion")
    fig16 = px.box(filtered_df, x="Attrition", y="YearsSinceLastPromotion", color="Attrition")
    st.plotly_chart(fig16, use_container_width=True)

with advanced:
    st.subheader("17. Numeric Feature Correlation Heatmap")
    st.markdown("Understand inter-feature correlations for numeric variables.")
    numeric = filtered_df.select_dtypes(include='number')
    corr = numeric.corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=False, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    st.subheader("18. Attrition Distribution by Education Field")
    fig18 = px.histogram(filtered_df, x="EducationField", color="Attrition", barmode="group")
    st.plotly_chart(fig18, use_container_width=True)

    st.subheader("19. Percent Salary Hike vs Attrition")
    fig19 = px.box(filtered_df, x="Attrition", y="PercentSalaryHike", color="Attrition")
    st.plotly_chart(fig19, use_container_width=True)

    st.subheader("20. Training Times Last Year vs Attrition")
    fig20 = px.histogram(filtered_df, x="TrainingTimesLastYear", color="Attrition", barmode="group")
    st.plotly_chart(fig20, use_container_width=True)

# Age Range Slider in Sidebar
age_min = int(df["Age"].min())
age_max = int(df["Age"].max())
age_range = st.sidebar.slider(
    "Select Age Range",
    min_value=age_min,
    max_value=age_max,
    value=(age_min, age_max)
)
