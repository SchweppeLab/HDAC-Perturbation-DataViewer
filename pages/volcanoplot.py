import streamlit as st
import pandas as pd
import plotly.express as px
from data.shared_data import load_data, load_list
import numpy as np
import gseapy as gp

st.set_page_config(page_title="Drug Response Explorer", layout="wide")
st.title("Drug Response Explorer for Lung Cancer Cell Lines")

# Load data
col1, col2, col3 = st.columns(3)
with col1.container(border=True, height = 300):
    st.header('Filter')
    selected_drug = st.selectbox("Select a Drug", load_list('drug'),index = 1)
    selected_line = st.selectbox("Select a Cell Line", load_list('line'))

with col2.container(border=True,height = 300):
    st.header('Threshold')
    fc_thresh = st.selectbox("X Cutoff (FC)", (1.1,1.25,1.5,1.75,2,2.5,3,5), index = 4)
    up_thresh = np.log2(fc_thresh)
    down_thresh = -np.log2(fc_thresh)
    p_thresh = st.selectbox("Y Cutoff (adjust p value)", (0.001, 0.01, 0.05, 0.1,1), index = 2)

with col3.container(border=True, height=300):
     st.header('Enrichment')
     methodinput = st.selectbox('Selet an enrichment method', ('KEGG','MF','BP','CC','Hallmark'))
methoddic = {'KEGG':'KEGG_2021_Human','BP':'GO_Biological_Process_2021','CC':'GO_Cellular_Component_2021','MF':'GO_Molecular_Function_2021','Hallmark':'MSigDB_Hallmark_2020'}
enrmethod = methoddic[methodinput]

tab1, tab2, tab3 = st.tabs(['Total','Phos','Total vs Phos'])

with tab1:
    df = load_data('total')
# Volcano Plot
    volcano_df = df[(df["Drug"] == selected_drug) & (df["Line"] == selected_line)].copy()
    volcano_df['cluster'] = np.select(
        [((volcano_df['padj'] < p_thresh) & (volcano_df['log2FC'] > up_thresh)),((volcano_df['padj'] < p_thresh) & (volcano_df['log2FC'] < down_thresh))],
            ['up', 'down'], 'notreg')
    upgene = volcano_df[volcano_df['cluster'] == 'up']['Gene'].unique().tolist()
    downgene = volcano_df[volcano_df['cluster'] == 'down']['Gene'].unique().tolist()
    upno = len(upgene)
    downno = len(downgene)
    fig_volcano = px.scatter(
        volcano_df, x="log2FC", y="lgpadj", color="cluster",
        hover_name="Gene",
        color_discrete_map={"up": "crimson", "notreg": "gray",'down':'blue'}
    )
    fig_volcano.update_layout(height=600)
    st.plotly_chart(fig_volcano)

    upenr = gp.enrichr(gene_list= upgene,
                        organism='human',
                        gene_sets=enrmethod, 
                        outdir= None,
                        background= None,
    ).results[['Term','Overlap', 'P-value','Adjusted P-value']]

    downenr = gp.enrichr(gene_list= downgene,
                        organism='human',
                        gene_sets=enrmethod, 
                        outdir= None,
                        background= None,
    ).results[['Term','Overlap', 'P-value','Adjusted P-value']]

    col4, col5 = st.columns(2)

    col4.write(f'{downno} Down Regulated Proteins')
    col4.dataframe(downenr)

    col5.write(f'{upno} Up Regulated Proteins')
    col5.dataframe(upenr)

with tab2:
    df2 = load_data('phos')
# Volcano Plot
    volcano_df2 = df2[(df2["Drug"] == selected_drug) & (df2["Line"] == selected_line)].copy()
    volcano_df2['cluster'] = np.select(
        [((volcano_df2['padj'] < p_thresh) & (volcano_df2['log2FC'] > up_thresh)),((volcano_df2['padj'] < p_thresh) & (volcano_df2['log2FC'] < down_thresh))],
            ['up', 'down'], 'notreg')
    fig_volcano2 = px.scatter(
        volcano_df2, x="log2FC", y="lgpadj", color="cluster",
        hover_name="Site",
        color_discrete_map={"up": "crimson", "notreg": "gray",'down':'blue'}
    )
    fig_volcano2.update_layout(height=600)
    st.plotly_chart(fig_volcano2)

with tab3:
    combinedata= volcano_df2[['Gene','Site','log2FC']].join(volcano_df[['Gene','log2FC']].set_index('Gene'), on='Gene',rsuffix ='_total',lsuffix = '_phos')
    combinedata['cluster']  = np.select(
        [(combinedata['log2FC_total'] >-1)&(combinedata['log2FC_total'] <1)&(combinedata['log2FC_phos'] >1),
         (combinedata['log2FC_total'] >-1)&(combinedata['log2FC_total'] <1)&(combinedata['log2FC_phos'] < -1)],
            ['up', 'down'], 'notreg')
    combine_fig = px.scatter(
        combinedata, x = 'log2FC_total',y='log2FC_phos',color='cluster', trendline='ols', trendline_scope="overall",
        hover_name='Site',
        color_discrete_map={"up": "crimson", "notreg": "gray",'down':'blue'}
    )
    combine_fig.add_shape(
        type = 'line',
        x0 = 1, x1 = 1,
        y0 =-5, y1 = 5,
        line = dict(color = 'gray', dash = 'dash') 
    )
    combine_fig.add_shape(
        type = 'line',
        x0 = -1, x1 = -1,
        y0 =-5, y1 = 5,
        line = dict(color = 'gray', dash = 'dash') 
    )
    combine_fig.add_shape(
        type = 'line',
        x0 = -5, x1 = 5,
        y0 =-1, y1 = -1,
        line = dict(color = 'gray', dash = 'dash') 
    )
    combine_fig.add_shape(
        type = 'line',
        x0 = -5, x1 = 5,
        y0 =1, y1 = 1,
        line = dict(color = 'gray', dash = 'dash') 
    )
    st.plotly_chart(combine_fig)