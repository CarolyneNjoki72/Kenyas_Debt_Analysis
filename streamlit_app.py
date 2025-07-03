import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title='Kenya's Debt Analysis',
    page_icon='💰','<img src="https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg" width="60">',
    layout='wide',
    initial_sidebar_state='expanded')

alt.themes.enable('dark')

#df1 = pd.read_csv('kenya_debt_analysis.csv')

#with st.sidebar:


