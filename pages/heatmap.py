import streamlit as st
import pandas as pd
import plotly.express as px
from data.shared_data import load_data, load_list
import numpy as np
import gseapy as gp
import seaborn as sns

st.set_page_config(page_title="Heatmap", layout="wide")
st.title("Protein Expression Heatmap Explorer")
df = load_data('combine')
select_list = df['Site'].unique().tolist()

col1, col2 = st.columns([2,3])
with col1.container(border=True, height = 400):
    st.header('Filter')
    selected_protein = st.multiselect("Select Proteins or Phosphosites", select_list, default=['HDAC1','HDAC2','HDAC3','HDAC4','HDAC5','HDAC6','HDAC7','HDAC8','HDAC9','HDAC10'])
    fc_thresh = st.selectbox("Fold Change Threshold", (1.1,1.25,1.5,1.75,2,2.5,3,5), index = 4)
    up_thresh = np.log2(fc_thresh)
    down_thresh = -np.log2(fc_thresh)
    p_thresh = st.selectbox("Adjust p value Threshold", (0.001, 0.01, 0.05, 0.1,1), index = 4)
with col2.container(border=True, height = 400):
    st.header('Summary')
    select_data = df[df['Site'].isin(selected_protein)]
    select_data['cluster'] = np.select(
    [((select_data['padj'] < p_thresh) & (select_data['log2FC'] > up_thresh)),((select_data['padj'] < p_thresh) & (select_data['log2FC'] < down_thresh))],
        ['up', 'down'], 'notreg')
    genact = select_data.groupby(['Site']).agg(
        linetotal = ('Line', lambda x : len(x.unique())),
        total = ('Line', 'size'),
        up=('cluster', lambda x: (x == 'up').sum()),
        down=('cluster', lambda x: (x =='down').sum()),
    ).reset_index()
    genact.columns = ['Name','No. of lines','No. of cell line by drug groups','No. of up-regulated groups','No. of down-regulated groups']
    genact = genact.set_index('Name')

    st.table(genact)

st.header('Heatmap')
length = len(selected_protein)
col3, col4 = st.columns([19, 1], gap="small")

with col3.container(border=False):    
    select_data = df[df['Site'].isin(selected_protein)]
    length = len(selected_protein)
    pivot_data = select_data.pivot_table(index='Site', columns=["Line",'Drug'], values="log2FC")
    pivot_data.columns = pivot_data.columns.map('{0[0]}_{0[1]}'.format)
    pivot_data=pivot_data.fillna(0)
    fig = sns.clustermap(pivot_data,
                    annot = True,
                    cmap= sns.diverging_palette(255, 6, s = 100, l =35, as_cmap=True),
                    dendrogram_ratio=(.05, .1), #(row, col)
                    row_cluster=True,
                    col_cluster=False,
                    linewidth=.5,
                    fmt = '.1f', cbar = False,figsize=(10, length/2+1),
                    center = 0,vmin = -2, vmax = 2,
                    annot_kws={"size": 6})
    fig.cax.set_visible(False)
    fig.cax.xaxis.tick_top()
    st.pyplot(fig)
with col4.container(border=False):
    st.image("data/heatmap_color bar.png")
