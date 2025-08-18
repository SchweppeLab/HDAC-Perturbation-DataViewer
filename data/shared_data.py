
import sqlite3
import pandas as pd
import streamlit as st

@st.cache_data
def load_data(dataset):
    if dataset == "total":
        df = pd.read_csv("data/long_Sum.csv")
        df = df[df['cv'] <30]
        df = df[['Gene','Uniprot','Line','Drug','log2FC','padj','lgpadj']]
    elif dataset == 'phos':
        df= pd.read_csv("data/long_Sum_phos.csv")
        df = df[df['cv'] <30]
        df = df[['Gene','Uniprot','Site','Line','Drug','log2FC','padj','lgpadj']]
    elif dataset == "viability":
        df = pd.read_csv('data/viability.csv')
        df = df.melt(id_vars=['Drug'], var_name='Line', value_name='Ratio mean')
    elif dataset == 'combine':
        total = pd.read_csv("data/long_Sum.csv")
        phos = pd.read_csv("data/long_Sum_phos.csv")
        total = total[['Gene','Uniprot','Line','Drug','log2FC','padj','lgpadj']]
        total['Site'] =total['Gene']
        phos = phos[['Gene','Uniprot','Site','Line','Drug','log2FC','padj','lgpadj']]
        df = pd.concat([total, phos], ignore_index=True)
    else:
        raise ValueError(f"Unknown dataset name: {dataset}")
    return df



def load_list(listname):
    if listname == 'drug':
        df = sorted(['Ralimetinib', 'CUDC101', 'Abexinostat','Vorinostat','TSA', 'Panobinostat','Belinostat'])
    elif listname == 'line':
        df = sorted(['A549', 'HCT116', 'PC9', 'PSC1','H292'])
    else:
        raise ValueError(f'Unkown list name: {listname}')
    return df
