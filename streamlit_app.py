import streamlit as st
import pandas as pd
import altair as alt
#import plotly.express as px


st.set_page_config(
    page_title='Kenya Debt Analysis',
    page_icon='💰',
    initial_sidebar_state='expanded')

alt.themes.enable('dark')

df1 = pd.read_csv('kenya_debt_analysis.csv')

with st.sidebar:
    st.title('💰 Kenyas Debt Analysis')

    year_list = list(df1['Year'].unique())[::-1] #newest year appears first
    df1['Year'] = df1['Year'].astype(int)
    selected_year = st.selectbox('Select year here', year_list, index=(len(year_list)-1))
    df1_selected_year = df1[df1['Year'] == selected_year]
    df1_selected_year_sorted = df1_selected_year.sort_values(by='Total', ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

st.line_chart(
    df1,
    x='Year'
    y=['External Debt', 'Domestic Debt', 'Total'],
    x_label='Year',
    y_label='Amount in million shillings' )



