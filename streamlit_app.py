import streamlit as st
import pandas as pd
import plotly.express as px

# Load your datasets
df_summary = pd.read_csv("kenya_debt_analysis.csv")  # Dataset 1
df_breakdown = pd.read_csv("Kenya's_debt_analysis.csv")  # Dataset 2

# Sidebar filter
st.sidebar.title("🔍 Filters")
years = sorted(df_summary['Year'].unique(), reverse=True)
selected_year = st.sidebar.selectbox("Select Year", years)

# Filter both datasets by year
summary_filtered = df_summary[df_summary['Year'] == selected_year]
breakdown_filtered = df_breakdown[df_breakdown['Year'] == selected_year]

# Header
st.title("📊 Kenya Public Debt Dashboard")
st.markdown(f"**Selected Year:** {selected_year}")

# Metrics Row
col1, col2, col3 = st.columns(3)
col1.metric("Total Public Debt", f"${summary_filtered['Total_Debt'].values[0]:,.0f}")
col2.metric("Debt-to-GDP Ratio", f"{summary_filtered['Debt_GDP_Ratio'].values[0]}%")
col3.metric("Interest Payments", f"${summary_filtered['Interest_Payments'].values[0]:,.0f}")

# Line Chart: Domestic, External, and Total Debt Over Time
st.subheader("📈 Debt Trend Over Time")

debt_trend = df_summary[["Year", "Domestic_Debt", "External_Debt", "Total_Debt"]].sort_values("Year")

fig_debt_trend = px.line(debt_trend, 
                         x="Year", 
                         y=["Domestic_Debt", "External_Debt", "Total_Debt"],
                         labels={"value": "Amount", "variable": "Debt Type"},
                         title="Domestic, External, and Total Debt Over Time")
st.plotly_chart(fig_debt_trend)

# Line Chart: Debt-to-GDP Ratio Over Time
st.subheader("📉 Debt-to-GDP Ratio Over Time")

gdp_trend = df_summary[["Year", "Debt_GDP_Ratio"]].sort_values("Year")

fig_gdp_ratio = px.line(gdp_trend, 
                        x="Year", 
                        y="Debt_GDP_Ratio",
                        labels={"Debt_GDP_Ratio": "Debt-to-GDP (%)"},
                        title="Debt-to-GDP Ratio Over Time")
st.plotly_chart(fig_gdp_ratio)

# Debt Type Breakdown Chart
st.subheader("📌 Debt Composition Breakdown")
fig1 = px.bar(breakdown_filtered.melt(id_vars="Year", var_name="Debt Type", value_name="Amount"),
              x="Debt Type", y="Amount", color="Debt Type", title="Debt by Category")
st.plotly_chart(fig1)

# Domestic vs External
st.subheader("💰 Domestic vs External Debt")
fig2 = px.pie(summary_filtered, values=[summary_filtered['External_Debt'].values[0],
                                        summary_filtered['Domestic_Debt'].values[0]],
              names=["External Debt", "Domestic Debt"],
              title="Debt Source Share")
st.plotly_chart(fig2)

# Raw Data View
with st.expander("📄 View Raw Data"):
    st.write("Summary Table", summary_filtered)
    st.write("Debt Breakdown", breakdown_filtered)

# Optional: Download button
st.download_button("📥 Download Summary CSV", summary_filtered.to_csv(index=False), file_name="debt_summary.csv")


