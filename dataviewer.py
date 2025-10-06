import streamlit as st

pages = {
    "Homepage": [
        st.Page("pages/homepage.py", title="Welcome to HDACi perturbation dataviewer!"),
    ],
    "Data viewer": [
        st.Page("pages/volcanoplot.py", title="Volcano plot"),
        st.Page('pages/heatmap.py', title="Heatmap"),
        st.Page('pages/correlation.py', title="Protein-Protein correlation"),
    ]

}
pg = st.navigation(pages)
pg.run()