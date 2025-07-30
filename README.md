# Cheminformatics and Molecular Database Analysis

This repository, inspired by and referencing the work of **Gustavo Seabra** ([Github](https://github.com/gmseabra)), provides a hands-on introduction to cheminformatics, molecular data exploration, and virtual screening workflows using Python, RDKit, and machine learning.


- **IntroCheminf**: Fundamentals of cheminformatics and RDKit usage.
- **MolDB-Exploration**: Exploration and curation of a real-world bioactivity dataset (COX-2 inhibitors).
- **MolDB-Screening**: Virtual screening, docking, and machine learning acceleration for large molecular libraries.


## Folder Summaries

### 1. `IntroCheminf`

- **Notebook**: `Introduction_to_Cheminformatics.ipynb`
- **Skills Covered**:  
  - Chemical informatics basics
  - Practical use of RDKit and PandasTools
  - Descriptor and fingerprint calculation
  - 2D and 3D molecule visualization

### 2. `MolDB-Exploration`

- **Notebook**: `ChEMBL_COX-2_Exploration.ipynb`
- **Skills Covered**:  
  - Data cleaning and feature engineering for chemical datasets
  - Handling duplicates, missing values, and outliers
  - Machine learning workflow for activity prediction

### 3. `MolDB-Screening`

- **Notebook**: `DB_Screening.ipynb`
- **Skills Covered**:  
  - Practical virtual screening (docking) pipeline
  - Application of ML regression/classification for fast bioactivity filtering
  - Efficient handling of large-scale molecular data

---

## Installation & Requirements

- **Python version**: 3.7+
- **Recommended environment**:  
  Use [conda](https://docs.conda.io/en/latest/) or [mamba](https://mamba.readthedocs.io/en/latest/) for dependency management.

- **Key packages**:
  - `rdkit`
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`
  - `py3dmol`
  - `AutoDock Vina` (for docking example, see their [official docs](https://autodock-vina.readthedocs.io/))

- **Setup example (conda):**
  ```bash
  conda create -n cheminf python=3.8 rdkit pandas scikit-learn matplotlib seaborn py3dmol
  conda activate cheminf
  # For docking: install AutoDock Vina separately (see their docs)
