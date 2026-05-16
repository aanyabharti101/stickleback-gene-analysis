# Comparative Genomics & Lineage-Specific Gene Analysis

A bioinformatics research project focused on comparative genomics, lineage-specific gene discovery, and evolutionary analysis using phylogenetic workflows, sequence homology methods, and automated gene tree analysis.

This project explores evolutionary relationships across fish species through computational genomics techniques including Newick tree parsing, genetic distance analysis, and Ensembl gene tree retrieval.

---

## Features

- Automated gene tree retrieval from the Ensembl REST API
- Phylogenetic tree generation and parsing
- Genetic distance computation between species
- Comparative genomics workflows
- Evolutionary relationship analysis
- BED and FASTA file handling
- Export of structured analysis tables
- Automated `.nwk` tree generation

---

## Technologies Used

- Python
- Biopython
- Pandas
- Requests
- Ensembl REST API
- Comparative Genomics Methods
- Phylogenetic Analysis

---

## Core Functionality

### Gene Tree Retrieval
The project retrieves phylogenetic gene trees from Ensembl using species names and Ensembl gene IDs.

Generated outputs include:
- Newick (`.nwk`) tree files
- phylogenetic relationship data
- gene tree identifiers

### Genetic Distance Analysis
Using Biopython phylogenetic tools, the workflow:
- parses Newick trees
- computes evolutionary distances between species
- exports structured CSV distance tables

### Comparative Genomics Workflow
The project supports:
- lineage-specific gene exploration
- evolutionary relationship analysis
- homolog investigation
- multi-species genomic comparisons

---

## Getting Started

### Requirements

- Python 3
- Biopython
- Pandas
- Requests

### Installation

```bash
git clone https://github.com/aanyabharti101/lineage-specific-gene-pipeline.git
cd lineage-specific-gene-pipeline
```

Install dependencies:

```bash
pip install biopython pandas requests
```

---

## Running the Scripts

### `biofind.py`

Retrieves phylogenetic gene trees directly from the Ensembl REST API and saves them as `.nwk` Newick tree files for downstream evolutionary analysis.

Run:

```bash
python3 biofind.py
```

---

### `bioinfo.py`

Computes evolutionary and genetic distances between species using parsed Newick trees and exports the results into a structured CSV table for analysis.

Run:

```bash
python3 bioinfo.py
```

Output:
- `EDA_distance_table.csv`

---

### `bioinfo1.py`

Provides interactive retrieval of fish gene trees by allowing users to input a species name and Ensembl gene ID dynamically.

The script:
- fetches gene tree data
- previews tree structure
- saves the resulting `.nwk` file locally

Run:

```bash
python3 bioinfo1.py
```

---

## Project Structure

```text
lineage-specific-gene-pipeline/
├── biofind.py                         # Gene tree retrieval from Ensembl
├── bioinfo.py                         # Genetic distance computation workflow
├── bioinfo1.py                        # Interactive gene tree fetcher
├── lineage_specific_locations.bed     # Genomic interval data
├── Danio_rerio.fa                     # Example FASTA sequence file
├── *.nwk                              # Generated phylogenetic trees
├── *.csv                              # Exported analysis tables
└── README.md
```

---

## Example Workflow

1. Retrieve phylogenetic gene trees from Ensembl
2. Save trees in Newick format
3. Parse trees using Biopython
4. Compute interspecies genetic distances
5. Export structured analysis tables for downstream analysis

---

## Future Improvements

- Expanded multi-species phylogenetic analysis
- Interactive tree visualizations
- Automated orthogroup classification
- HPC pipeline integration
- Statistical evolutionary modeling
- Additional genomic annotation workflows

---

## Acknowledgements

- Ensembl REST API
- Biopython
- Comparative genomics research resources
- Open-source bioinformatics libraries
