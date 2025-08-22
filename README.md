# 57_dataViewer

An interactive web application for exploring lung cancer cell responses to epigenetic inhibition, built with **Streamlit** and **Plotly**.

## Project Overview

This data viewer presents a molecular resource based on the quantification of chromatin, proteome, and transcriptome remodeling due to histone deacetylase inhibitors (HDACi) in non-isogenic cell lines. The application provides interactive visualizations for exploring:

- **Volcano plots** - Differential protein expression analysis
- **Heatmaps** - Protein expression patterns across conditions  
- **Correlation plots** - Protein-protein correlation analysis
- **Gene set enrichment** - Pathway and functional enrichment analysis

**Created by Chelsea Lin, Schweppe Lab, UW Genome Science**

## Features

The web application includes several interactive visualization pages:

1. **Homepage** - Project overview and abstract
2. **Volcano Plot** - Interactive scatter plots showing differential protein expression with:
   - Customizable fold-change and p-value thresholds
   - Gene set enrichment analysis (KEGG, GO, Hallmark)
   - Support for both total protein and phosphorylation data
3. **Heatmap** - Clustered heatmaps of protein expression across cell lines and drugs
4. **Correlation** - Protein-protein correlation analysis with interactive scatter plots

## Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework for data science
- **[Plotly](https://plotly.com/)** - Interactive visualization library for scatter plots and volcano plots
- **[Seaborn](https://seaborn.pydata.org/)** - Statistical data visualization for heatmaps
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[NumPy](https://numpy.org/)** - Numerical computing
- **[GSEApy](https://gseapy.readthedocs.io/)** - Gene set enrichment analysis

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SchweppeLab/57_dataViewer.git
   cd 57_dataViewer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the Streamlit web application:

```bash
streamlit run dataviewer.py
```

The application will automatically open in your default web browser at `http://localhost:8501`.

## How Streamlit and Plotly Work Together

This application demonstrates how to build interactive data visualization web apps using Streamlit and Plotly:

### Streamlit Features Used:
- **Multi-page navigation** with `st.navigation()` and `st.Page()`
- **Interactive widgets** like `st.selectbox()`, `st.multiselect()` for user input
- **Layout components** with `st.columns()` and `st.container()` for organized layouts
- **Tabbed interfaces** using `st.tabs()` for organizing different views
- **Data caching** with `@st.cache_data` for performance optimization

### Plotly Integration:
- **Interactive scatter plots** with `plotly.express.scatter()` for volcano plots and correlations
- **Hover information** showing gene names and data values
- **Color mapping** for different experimental conditions
- **Trendlines** and statistical overlays
- **Custom shapes and annotations** for threshold lines
- **Seamless integration** with Streamlit using `st.plotly_chart()`

### Example Code Structure:
```python
import streamlit as st
import plotly.express as px

# Create interactive controls
selected_drug = st.selectbox("Select a Drug", drug_list)
selected_line = st.selectbox("Select a Cell Line", cell_lines)

# Generate Plotly visualization
fig = px.scatter(data, x="log2FC", y="lgpadj", color="cluster", hover_name="Gene")

# Display in Streamlit
st.plotly_chart(fig)
```

## Data

The application uses proteomics and phosphoproteomics data from lung cancer cell lines treated with various histone deacetylase inhibitors:

- **Cell lines**: A549, H292, HCT116, PC9, PSC1
- **Drugs**: Ralimetinib, CUDC101, Abexinostat, Vorinostat, TSA, Panobinostat, Belinostat
- **Data types**: Total protein expression, phosphorylation sites, viability measurements

## Contributing

This project is part of ongoing research at the Schweppe Lab. For questions or contributions, please contact the lab.

## License

Please cite appropriate publications when using this data viewer for research purposes.

