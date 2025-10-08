# HDAC  Perturbation Data viewer

An interactive web application for exploring lung cancer cell responses to epigenetic inhibition, built with **Streamlit** and **Plotly**.

## Project Overview
The application uses proteomics and phosphoproteomics data from lung cancer cell lines treated with various histone deacetylase inhibitors (HDACi):

- **Cell lines**: A549, H292, HCT116, PC9, PSC1
- **Drugs**: Ralimetinib, CUDC101, Abexinostat, Vorinostat, TSA, Panobinostat, Belinostat
- **Data types**: Total protein expression, phosphorylation sites, viability measurements

The preprint can be found at [bioRxiv](https://doi.org/10.1101/2024.05.23.592075)

## Features

The web application includes several interactive visualization pages:

1. **Homepage** - Project overview and abstract
2. **Correlation** - Protein-protein correlation analysis with interactive scatter plots
3. **Volcano Plot** - Interactive scatter plots showing differential protein expression with:
   - Support for both total protein and phosphorylation data
   - Customizable fold-change and p-value thresholds
   - Gene set enrichment analysis (KEGG, GO, Hallmark)
   - Kinase-Substrate Enrichment Analysis (KSEA)
4. **Heatmap** - Clustered heatmaps of protein expression across cell lines and drugs

## Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework for data science
- **[Plotly](https://plotly.com/)** - Interactive visualization library for scatter plots and volcano plots
- **[Seaborn](https://seaborn.pydata.org/)** - Statistical data visualization for heatmaps
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[NumPy](https://numpy.org/)** - Numerical computing
- **[GSEApy](https://gseapy.readthedocs.io/)** - Gene set enrichment analysis

## Installation

### Prerequisites

- **For Docker (Recommended):**
  - [Docker](https://docs.docker.com/get-docker/) (version 20.10 or later)
  - [Docker Compose](https://docs.docker.com/compose/install/) (usually included with Docker Desktop)

- **For Local Installation:**
  - Python 3.11 or later
  - pip package manager

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SchweppeLab/57_dataViewer.git
   cd 57_dataViewer
   ```

2. **Install dependencies (for local installation only):**
   ```bash
   pip install -r requirements.txt
   ```
   
   *Note: If using Docker, dependencies are automatically installed in the container.*

## Running the Application

### Option 1: Docker (Recommended)

Docker provides an isolated, consistent environment with all dependencies pre-installed. This is the easiest and most reliable way to run the application.

#### Using Docker Compose (Easiest)

1. **Start the application:**
   ```bash
   docker compose up
   ```
   
   *Note: If you have Docker Compose V1, use `docker-compose up` instead.*

   The first time you run this command, Docker will:
   - Build the image (may take a few minutes)
   - Install all Python dependencies
   - Start the application

2. **Access the application:**
   
   Open your web browser and navigate to `http://localhost:3838`

3. **Stop the application:**
   
   Press `Ctrl+C` in the terminal, or in a new terminal run:
   ```bash
   docker compose down
   ```

4. **View logs:**
   ```bash
   docker compose logs -f
   ```

#### Using Docker Directly

If you prefer not to use Docker Compose:

1. **Build the Docker image:**
   ```bash
   docker build -t 57_dataviewer .
   ```

2. **Run the container:**
   ```bash
   docker run -p 3838:3838 57_dataviewer
   ```

3. **Access the application:**
   
   Open your web browser and navigate to `http://localhost:3838`

4. **Stop the container:**
   
   Press `Ctrl+C` in the terminal, or find the container ID and stop it:
   ```bash
   docker ps
   docker stop <container_id>
   ```

#### Docker Configuration Details

The Docker setup includes:
- **Base Image**: Python 3.11 slim (lightweight and optimized)
- **Port**: 3838 (mapped to host port 3838)
- **Data Volume**: The `data/` directory is mounted as read-only, allowing data updates without rebuilding
- **Auto-restart**: Container restarts automatically unless manually stopped (Docker Compose only)
- **Environment**: Streamlit configured for headless operation suitable for containers

### Option 2: Local Python Installation

To run the application directly with Python (without Docker):

1. **Ensure dependencies are installed:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Streamlit web application:**
   ```bash
   streamlit run dataviewer.py
   ```

   The application will automatically open in your default web browser at `http://localhost:8501`.

### Troubleshooting

**Docker Issues:**
- **Port already in use**: If port 3838 is already in use, you can change it in `docker-compose.yml` or use a different port:
  ```bash
  docker run -p 8080:3838 57_dataviewer
  ```
- **Permission denied**: On Linux, you may need to run Docker commands with `sudo` or add your user to the docker group
- **Container won't start**: Check logs with `docker compose logs` or `docker logs <container_id>`
- **Changes not reflected**: If you modify the code, rebuild with `docker compose up --build`

**Python Issues:**
- **Module not found**: Ensure all dependencies are installed with `pip install -r requirements.txt`
- **Port 8501 in use**: Streamlit will automatically try the next available port

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

## Contributing and License

This project is part of ongoing research at the Schweppe Lab under an MIT license. For questions or contributions, please contact the lab.

