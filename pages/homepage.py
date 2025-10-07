import streamlit as st

st.markdown("### Welcome to the data viewer of")
st.markdown("# Defining the heterogeneous molecular landscape of lung cancer cell responses to epigenetic inhibition")
st.markdown(
    """
    **Preprint**: [bioRxiv 2024.05.23.592075v3](https://www.biorxiv.org/content/10.1101/2024.05.23.592075v3)
    """)
st.markdown(
    """
    [**Schweppe Lab**](https://www.schweppelab.org/)
    """)
st.markdown(
    """
    **UW Genome Sciences**
    """)
st.markdown("---")

st.markdown(
    """
    ### Abstract
    Epigenetic inhibitors exhibit powerful antiproliferative and anticancer activities. 
    However, cellular responses to small-molecule epigenetic inhibition are heterogeneous 
    and dependent on factors such as the genetic background, metabolic state, and on-/off-target engagement 
    of individual small-molecule compounds. The molecular study of the extent of this heterogeneity often measures 
    changes in a single cell line or using a small number of compounds. To more comprehensively profile the effects of  
    small-molecule perturbations and their influence on these heterogeneous cellular responses, we present a molecular 
    resource based on the quantification of chromatin, proteome, and transcriptome remodeling due to histone deacetylase 
    inhibitors (HDACi) in non-isogenic cell lines. Through quantitative molecular profiling of 10,621 proteins, these 
    data reveal coordinated molecular remodeling of HDACi treated cancer cells. HDACi-regulated proteins differ greatly 
    across cell lines with  consistent (JUN, MAP2K3, CDKN1A) and divergent (CCND3, ASF1B, BRD7) cell-state effectors. 
    Together these data provide valuable insight into cell-type driven and heterogeneous responses that must be 
    taken into consideration when monitoring molecular perturbations in culture models.
    """
)
st.image("data/abstract.png")
st.markdown(
    """
    Table 1. Large-scale analyses of drug perturbations.
    |Name|Type|Cell line|No. of drugs|Drug Concentration|Duration|Reference|
    |---|---|---|---|---|---|---|
    |This dataset|Proteomics|A549, H292, HCT116, PC9, PSC1|6|10 uM|24h|
    |DeepCoverMOA|Proteomics|HCT116|875|10 uM|24 h|[Mitchell et al., 2023](https://pubmed.ncbi.nlm.nih.gov/36593396/)
    |Sci-plex|Transcriptomics|A549, K562, and MCF7|188|10 nM, 100 nM, 1 uM, 10 uM|24 h|[Srivatsan et al., 2020](https://www.science.org/doi/10.1126/science.aax6234)
    |PRISM|Viability assay|578 cell lines, including H292, HCT116, PC-9 & A549|1448|610 pM, 2.4 nM, 9.8 nM, 39 nM, 156 nM, 625 nM, 2.5 uM, 10 uM|5 days|[Corsello et al., 2020](https://www.nature.com/articles/s43018-019-0018-6)
    |decryptM|PTM & proteomics|13 cell lines, including PC9 & A549|31|10 nM, 30 nM, 100 nM, 300 nM, 1 uM, 3 uM, 10 uM, 30 uM, 100 uM||[Zecha et al., 2023](https://www.science.org/doi/10.1126/science.ade3925)
    |decryptE|Proteomics|Jurkat|144|1 nM, 10 nM, 100 nM, 1uM, 10 uM|18 h|[Eckert et al., 2024](https://www.nature.com/articles/s41587-024-02218-y)
   """
)
