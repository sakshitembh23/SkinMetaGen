import streamlit as st
from pathlib import Path

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
    # Placeholder for pipeline execution and report generation
    st.info("Running mock analysis pipeline...")
    # Simulate results
    st.markdown("### Microbiome Summary (Mock)")
    st.write({
        "Dominant Taxa": ["Staphylococcus epidermidis", "Cutibacterium acnes"],
        "Diversity Index": 2.5,
        "Pathways": ["Fatty acid biosynthesis", "Vitamin B metabolism"]
    })
    st.markdown("### Personalized Food Suggestions (Mock)")
    st.write([
        "Increase intake of omega-3 rich foods (e.g., walnuts, flaxseed)",
        "Consume more fermented foods (e.g., yogurt, kefir)"
    ])
    st.markdown("---")
    st.download_button("Download Sample Report (PDF)", data="This is a placeholder PDF report.", file_name="skin_microbiome_report.pdf")
else:
    st.info("Please upload your sequencing files to begin analysis.")
