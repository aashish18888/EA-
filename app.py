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

st.title("📊 Employee Attrition Dashboard")
st.markdown("Analyze attrition trends across departments, roles, satisfaction, and demographics.")

# Sidebar
st.sidebar.header("🔍 Filter Data")
departments = st.sidebar.multiselect("Select Department", df['Department'].unique(), default=df['Department'].unique())
genders = st.sidebar.multiselect("Select Gender", df['Gender'].unique(), default=df['Gender'].unique())
overtime = st.sidebar.selectbox("OverTime", options=["All"] + df['OverTime'].unique().tolist())

filtered_df = df[df['Department'].isin(departments) & df['Gender'].isin(genders)]
if overtime != "All":
    filtered_df = filtered_df[filtered_df['OverTime'] == overtime]

# Tabs
tab1, tab2, tab3 = st.tabs(["📈 Macro Overview", "📉 Micro Analysis", "🧮 Correlations"])

with tab1:
    st.subheader("1. Overall Attrition Rate")
    st.markdown("Shows the proportion of employees who have left vs stayed.")
    fig1 = px.pie(df, names="Attrition", title="Attrition Distribution")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("2. Attrition by Department")
    st.markdown("Compare attrition counts across departments.")
    fig2 = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("3. Attrition by Gender")
    st.markdown("Visualize gender-wise attrition distribution.")
    fig3 = px.histogram(filtered_df, x="Gender", color="Attrition", barmode="group")
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("4. Attrition by Education Field")
    fig4 = px.histogram(filtered_df, x="EducationField", color="Attrition", barmode="group")
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("5. Age Distribution by Attrition")
    fig5 = px.histogram(filtered_df, x="Age", color="Attrition", nbins=30, barmode="overlay")
    st.plotly_chart(fig5, use_container_width=True)

with tab2:
    st.subheader("6. Job Role vs Attrition")
    fig6 = px.histogram(filtered_df, x="JobRole", color="Attrition", barmode="group")
    st.plotly_chart(fig6, use_container_width=True)

    st.subheader("7. Monthly Income by Attrition")
    fig7 = px.box(filtered_df, x="Attrition", y="MonthlyIncome", color="Attrition")
    st.plotly_chart(fig7, use_container_width=True)

    st.subheader("8. Job Satisfaction vs Attrition")
    fig8 = px.histogram(filtered_df, x="JobSatisfaction", color="Attrition", barmode="group")
    st.plotly_chart(fig8, use_container_width=True)

    st.subheader("9. Work-Life Balance by Attrition")
    fig9 = px.histogram(filtered_df, x="WorkLifeBalance", color="Attrition", barmode="group")
    st.plotly_chart(fig9, use_container_width=True)

    st.subheader("10. Overtime vs Attrition")
    fig10 = px.histogram(filtered_df, x="OverTime", color="Attrition", barmode="group")
    st.plotly_chart(fig10, use_container_width=True)

    st.subheader("11. Training Times vs Attrition")
    fig11 = px.histogram(filtered_df, x="TrainingTimesLastYear", color="Attrition", barmode="group")
    st.plotly_chart(fig11, use_container_width=True)

    st.subheader("12. Percent Salary Hike vs Attrition")
    fig12 = px.box(filtered_df, x="Attrition", y="PercentSalaryHike", color="Attrition")
    st.plotly_chart(fig12, use_container_width=True)

with tab3:
    st.subheader("13. Tenure: Years at Company vs Attrition")
    fig13 = px.histogram(filtered_df, x="YearsAtCompany", color="Attrition", barmode="overlay", nbins=20)
    st.plotly_chart(fig13, use_container_width=True)

    st.subheader("14. Years in Current Role")
    fig14 = px.box(filtered_df, x="Attrition", y="YearsInCurrentRole", color="Attrition")
    st.plotly_chart(fig14, use_container_width=True)

    st.subheader("15. Years with Current Manager")
    fig15 = px.box(filtered_df, x="Attrition", y="YearsWithCurrManager", color="Attrition")
    st.plotly_chart(fig15, use_container_width=True)

    st.subheader("16. Job Involvement")
    fig16 = px.histogram(filtered_df, x="JobInvolvement", color="Attrition", barmode="group")
    st.plotly_chart(fig16, use_container_width=True)

    st.subheader("17. Environment Satisfaction")
    fig17 = px.histogram(filtered_df, x="EnvironmentSatisfaction", color="Attrition", barmode="group")
    st.plotly_chart(fig17, use_container_width=True)

    st.subheader("18. Relationship Satisfaction")
    fig18 = px.histogram(filtered_df, x="RelationshipSatisfaction", color="Attrition", barmode="group")
    st.plotly_chart(fig18, use_container_width=True)

    st.subheader("19. Performance Rating")
    fig19 = px.histogram(filtered_df, x="PerformanceRating", color="Attrition", barmode="group")
    st.plotly_chart(fig19, use_container_width=True)

    st.subheader("20. Correlation Heatmap")
    st.markdown("Correlation of numerical features with each other.")
    num_df = filtered_df.select_dtypes(include='number')
    corr = num_df.corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
