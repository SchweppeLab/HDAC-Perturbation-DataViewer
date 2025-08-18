import streamlit as st

pages = {
    "Homepage": [
        st.Page("pages/homepage.py", title="Welcome to 2415 dataviewer"),
    ],
    "Data viewer": [
        st.Page("pages/volcanoplot.py", title="Volcano plot"),
        st.Page('pages/heatmap.py', title="Heatmap"),
    ]

}
pg = st.navigation(pages)
pg.run()