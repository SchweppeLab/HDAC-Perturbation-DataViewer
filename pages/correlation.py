import streamlit as st
import pandas as pd
import plotly.express as px
from data.shared_data import load_data, load_list
import numpy as np
import gseapy as gp
import seaborn as sns

st.set_page_config(page_title="Protein correlation", layout="wide")
st.title("Protein correlation Explorer")
df = load_data('combine')
select_list = df['Site'].unique().tolist()
df = df.pivot_table(index=["Line", 'Drug'], columns=['Site'], values="log2FC").dropna(thresh = 29,axis=1)
select_list = df.columns.tolist()

col1, col2 = st.columns([1,2])
with col1.container(border=True, height = 800):
    st.header('Filter')
    selected_protein = st.selectbox("Select A Protein or Phosphosite", select_list, index=select_list.index('HDAC7'))
    st.header('Pearson Correlation')
    data1 = df[[selected_protein]]     
    data2 = df.drop(columns=[selected_protein]) 
    corrdata = data1.apply(data2.corrwith, method = 'pearson')
    corrdata.columns = ['Pearson r']
    corrdata['abs_r'] = corrdata['Pearson r'].abs()
    corrdata = corrdata.sort_values(by='abs_r', ascending=False)
    st.dataframe(corrdata['Pearson r'])
    
with col2.container(border=True, height = 800):
    st.header('Correlation Plot')
    selected_protein2 = st.selectbox("Select Another Protein or Phosphosite", select_list, index=select_list.index('FUCA1'))
    df = df.reset_index()
    fig_correlation = px.scatter(
        df, x=selected_protein, y=selected_protein2, 
        color='Drug', symbol='Line', 
        trendline="ols",trendline_scope="overall"
    )
    fig_correlation.update_layout(height=600,width=600)
    st.plotly_chart(fig_correlation)
