# Skin Microbiome Metagenomic Analysis

A Streamlit web application for analyzing skin microbiome sequencing data and providing personalized recommendations.

## Features

- Upload and process raw sequencing data (FASTQ/FASTA)
- Comprehensive microbiome analysis pipeline
- Interactive visualizations of microbial composition
- Detailed taxonomic analysis
- Functional pathway analysis
- Personalized dietary and lifestyle recommendations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SkinMetaGen.git
cd SkinMetaGen
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
cd skin-microbiome-web
streamlit run app.py
```

The application will be available at http://localhost:8501

## Project Structure

```
SkinMetaGen/
├── skin-microbiome-web/
│   └── app.py
├── requirements.txt
└── README.md
```

## Dependencies

- Streamlit
- Pandas
- NumPy
- Plotly

## License

MIT License 