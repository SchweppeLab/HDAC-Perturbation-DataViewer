import streamlit as st

pages = {
    "Home": [
        st.Page("pages/homepage.py", title="Welcome to HDACi perturbation dataviewer"),
    ],
    "Data viewer": [
        st.Page('pages/correlation.py', title="Protein-Protein correlation"),
        st.Page('pages/heatmap.py', title="Heatmap"),
        st.Page("pages/volcanoplot.py", title="Volcano plot"),
    ]

}
pg = st.navigation(pages)
pg.run()