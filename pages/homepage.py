import streamlit as st

st.markdown("### Welcome to the data viewer of")
st.markdown("# Defining the heterogeneous molecular landscape of lung cancer cell responses to epigenetic inhibition")
st.markdown(
    """
    **Schweppe Lab**
    """)
st.markdown(
    """
    **UW Genome Science**
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
    ### Introduction
    Deconvoluting the myriad effects downstream of small molecule perturbations is essential to therapeutic development. Whole proteome and transcriptome analyses of these perturbations can validate and identify proposed mechanisms of action and identify cellular effects for therapeutics and tool compounds. To date, however, many large-scale proteome analyses of drug perturbations have been limited to a single  cell line treated with a cohort of small-molecule tool compounds and therapeutic drugs (Table 1). The selection of  cell lines in these studies has been in part a practical consideration as each new cell line included leads to a rapid expansion in the number of samples that must be processed and compared. Unfortunately, this often means sacrificing understanding of the diverse molecular contexts of different cellular models to enable the analysis of larger cohorts of small-molecule compounds (P.-H. Chen et al., 2019).

    Table 1. large-scale analyses of drug perturbations.
    |Name|Type|Cell line|No. of drugs|Drug Concentration|Duration|Reference|
    |---|---|---|---|---|---|---|
    |This dataset|Proteomics|A549, H292, HCT116, PC9, PSC1|6|10 uM|24h|
    |DeepCoverMOA|Proteomics|HCT116|875|10 uM|24 h|Mitchell et al., 2023
    |Sci-plex|Transcriptomics|A549, K562, and MCF7|188|10 nM, 100 nM, 1 uM, 10 uM|24 h|Srivatsan et al., 2020
    |PRISM|Viability assay|578 cell lines, including H292, HCT116, PC-9 & A549|1448|610 pM, 2.4 nM, 9.8 nM, 39 nM, 156 nM, 625 nM, 2.5 uM, 10 uM|5 days|Corsello et al., 2020
    |decryptM|PTM & proteomics|13 cell lines, including PC9 & A549|31|10 nM, 30 nM, 100 nM, 300 nM, 1 uM, 3 uM, 10 uM, 30 uM, 100 uM||Zecha et al., 2023
    |decryptE|Proteomics|Jurkat|144|1 nM, 10 nM, 100 nM, 1uM, 10 uM|18 h|Eckert et al., 2024

    Large-scale viability screening of small molecule perturbations in the PRISM dataset has shown that drugs targeting the same protein or pathway can drive heterogeneous responses in cancer cells (Corsello et al., 2020). Recent transcriptome efforts for bulk and single-cell samples have also uncovered divergent cellular responses when cells are treated with therapeutic and tool compounds (Srivatsan et al., 2020). At the single-cell level, these studies revealed inconsistent molecular responses of individual, isogenic cells to small molecule perturbation suggesting that additional context and molecular understanding are necessary to dissect the molecular consequences of chemical perturbation. More challenging still is the fact that  transcriptomic profiling of cellular perturbations cannot measure the direct protein targets of many of these perturbations (Maltz & Wollman, 2022). Thus, owing to the limited correlation between RNA and protein measurements (Wang et al., 2019), there remains a gap in our knowledge of the proteomic consequences of drug perturbations across multiple, representative cell lines.
    
    Recently, several studies have aimed to bridge this gap. These include the DeepCoverMOA and decryptE datasets (Mitchell et al., 2023; Zecha et al., 2023), which represent some of the largest, publicly-available chemical perturbation-based proteomic datasets. The DeepCoverMOA analyzed HCT116 cells in response to 875 therapeutic and tool compounds and revealed that a majority of the measurable proteome was accessible to regulation by small molecule treatment. The resulting proteome remodeling responses were then used to assemble proteomic networks to define consistent chemical mechanisms of actions. In a related study, the decryptE dataset studied dose-dependent chemical responses of 144 compounds in Jurkat cells to determine similarities and differences in cellular mechanisms of action. Yet, an important caveat to these two studies was that the whole proteome analysis to decipher compound mechanisms of action were each done in single, isogenic cell lines which may not be representative of the genetic and molecular heterogeneity when considering non-isogenic cell models (Begley & Ellis, 2012; Raghavan, 2022).  Interestingly, both the DeepCoverMOA and decryptE datasets evidenced high overall compound activity for histone deacetylase (HDAC) inhibitors (HDACi) such as vorinostat, quisinostat, and nexturastat (Mitchell et al., 2023; Zecha et al., 2023).
    
    HDAC regulation is key to the cellular chromatin state and is frequently dysregulated in cancer (Y. Li & Seto, 2016) and known to exhibit lineage-specific dependencies in cancer cells (Y. Zhang et al., 2023). This relationship between HDACs and cancer progression has driven a decades-long effort to develop targeted chemical HDAC inhibitors (HDACi) (Yoshida et al., 1990) and FDA approvals for several of these inhibitors to treat lymphomas and melanomas (B. S. Mann et al., 2007; McDermott & Jimeno, 2014; Richardson et al., 2015). While HDAC inhibitors have shown promising preclinical results for many cancers, clinical trial results vary (Mamdani & Jalal, 2020). Vorinostat monotherapy in non-small cell lung cancer (NSCLC) patients did not show objective antitumor activity, but toxicity with adverse effects such as fatigue (Traynor et al., 2009, p. 20). Other phase II monotherapy of romidepsin and pivaloyloxymethyl butyrate resulted in little efficacy in patients, and had side effects such as fatigue, nausea, and dysgeusia (Reid et al., 2004; Schrump et al., 2008).
    
    While comprehensive understanding of the pleiotropic molecular consequences remains elusive (Miyanaga et al., 2008), treatment of cells with HDACi induces expression of p21/CDKN1a leading to cell cycle arrest (Richon et al., 1996; Xiao et al., 1999), alters expression of c-Jun (Vrana et al., 1999) and the apoptotic regulators Bcl-2 and Bcl-xL (X. X. Cao et al., 2001; Fandy & Srivastava, 2006), attenuates AKT/mTOR signaling leading to autophagy (Y.-L. Liu et al., 2010), and suppresses IFN-mediated signaling (Shulak et al., 2014). Recent chemoproteomics analyses have also revealed that heterogeneous responses to HDAC inhibition may be driven in part by the abundance of HDAC protein complex members and the engagement of off-target HDACi binders such as MBLAC2 (Lechner et al., 2022). Thus, these effects have been shown to be both cell-type dependent and cell-type independent, further confounding our understanding of the molecular consequences of HDACi cellular treatments. 
    
    Here, we set out to determine the effects of the HDACi treatment on proteome remodeling in non-isogenic cell lines. In particular we focused on cell treatments with well established HDACi compounds to enable comparative analyses to previous datasets such as DeepCoverMOA and decryptE—including, belinostat, CUDC-101, trichostatin A (TSA), panobinostat, abexinostat and vorinostat (SAHA). We did this in the context of a genetically diverse panel of lung cancer cell lines with KRas, EGFR, TP53, CDKN1A, STK11 mutations and integrated proteomic, phosphoproteomic, and transcriptomics to establish a resource to explore drivers of the heterogeneous HDACi responses in these cells. Quantification of histone modifications status in multiple cell lines and thermal stability analyses then allowed us to determine the molecular linkage and effects of on-target and off-target protein engagement with HDAC inhibitors. These data represent an important resource to understand how chemical perturbation analyses are affected by preclinical cell line choice and exploration of how cellular diversity affects the characterization of small molecule compound mechanisms of action.
   """
)
