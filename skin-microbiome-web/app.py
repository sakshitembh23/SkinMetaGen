import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="Skin Microbiome Analyzer", layout="wide")
st.title("Skin Microbiome Metagenomic Analysis")

st.markdown("""
Upload your raw sequencing data (FASTQ/FASTA). The app will run a metagenomic pipeline (QC → Trimming → MetaPhlAn → Assembly → Bowtie → Binning → Kraken2), then generate a detailed report with food suggestions based on your skin microbiome.
""")

uploaded_files = st.file_uploader(
    "Upload raw sequence files (FASTQ/FASTA, paired or single-end)",
    type=["fastq", "fq", "fasta", "fa", "gz"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} files uploaded. (Pipeline will run here in the full version)")
    
    # Create tabs for different sections of the report
    tab1, tab2, tab3, tab4 = st.tabs(["Microbiome Overview", "Taxonomic Analysis", "Functional Analysis", "Recommendations"])
    
    with tab1:
        st.header("Microbiome Overview")
        
        # Sample data for visualization
        bacteria_data = {
            'Bacteria': ['Staphylococcus epidermidis', 'Cutibacterium acnes', 'Staphylococcus aureus', 
                        'Corynebacterium spp.', 'Micrococcus luteus'],
            'Abundance': [35, 25, 15, 12, 8]
        }
        df = pd.DataFrame(bacteria_data)
        
        # Create pie chart
        fig = px.pie(df, values='Abundance', names='Bacteria', 
                     title='Top 5 Bacterial Species Distribution')
        st.plotly_chart(fig)
        
        # Diversity metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Shannon Diversity Index", "2.5", "0.3")
        with col2:
            st.metric("Species Richness", "156", "12")
        with col3:
            st.metric("Evenness", "0.68", "-0.05")
    
    with tab2:
        st.header("Taxonomic Analysis")
        
        # Create sample taxonomy data
        taxonomy_data = {
            'Phylum': ['Firmicutes', 'Actinobacteria', 'Proteobacteria', 'Bacteroidetes'],
            'Abundance': [45, 30, 15, 10]
        }
        df_tax = pd.DataFrame(taxonomy_data)
        
        # Bar chart for phylum level
        fig2 = px.bar(df_tax, x='Phylum', y='Abundance', 
                      title='Phylum Level Distribution')
        st.plotly_chart(fig2)
        
        # Detailed taxonomy table
        st.subheader("Detailed Taxonomy")
        taxonomy_details = pd.DataFrame({
            'Taxonomic Level': ['Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species'],
            'Most Abundant': ['Firmicutes', 'Bacilli', 'Bacillales', 'Staphylococcaceae', 
                            'Staphylococcus', 'epidermidis'],
            'Relative Abundance': ['45%', '40%', '35%', '30%', '25%', '20%']
        })
        st.dataframe(taxonomy_details)
    
    with tab3:
        st.header("Functional Analysis")
        
        # Sample pathway data
        pathways = {
            'Pathway': ['Fatty acid biosynthesis', 'Vitamin B metabolism', 
                       'Amino acid synthesis', 'Antibiotic resistance'],
            'Abundance': [85, 75, 65, 45]
        }
        df_path = pd.DataFrame(pathways)
        
        # Horizontal bar chart for pathways
        fig3 = px.bar(df_path, x='Abundance', y='Pathway', orientation='h',
                      title='Top Metabolic Pathways')
        st.plotly_chart(fig3)
        
        # Functional annotations
        st.subheader("Key Functional Annotations")
        st.write("""
        - **Antimicrobial Production**: High levels of bacteriocin production genes
        - **Barrier Function**: Enhanced expression of ceramide synthesis pathways
        - **Immune Modulation**: Presence of immunomodulatory gene clusters
        - **Metabolic Activity**: Active vitamin B synthesis pathways
        """)
    
    with tab4:
        st.header("Personalized Recommendations")
        
        # Dietary recommendations
        st.subheader("Dietary Recommendations")
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
            ### Foods to Increase
            - Omega-3 rich foods (walnuts, flaxseed)
            - Fermented foods (yogurt, kefir)
            - Prebiotic foods (garlic, onions)
            - Vitamin B-rich foods (whole grains, eggs)
            """)
        with col2:
            st.write("""
            ### Foods to Moderate
            - High-sugar foods
            - Processed foods
            - Dairy products (if sensitive)
            - Alcohol
            """)
        
        # Lifestyle recommendations
        st.subheader("Lifestyle Recommendations")
        st.write("""
        1. **Skincare Routine**:
           - Use gentle, pH-balanced cleansers
           - Apply prebiotic-rich moisturizers
           - Avoid harsh exfoliants
        
        2. **Environmental Factors**:
           - Maintain humidity levels (40-60%)
           - Use air purifiers
           - Avoid excessive sun exposure
        
        3. **Stress Management**:
           - Practice regular meditation
           - Ensure adequate sleep (7-8 hours)
           - Regular exercise
        """)
    
    # Download button for the report
    st.markdown("---")
    report_date = datetime.now().strftime("%Y-%m-%d")
    st.download_button(
        "Download Full Report (PDF)",
        data="This is a placeholder PDF report with detailed microbiome analysis.",
        file_name=f"skin_microbiome_report_{report_date}.pdf"
    )
else:
    st.info("Please upload your sequencing files to begin analysis.")
