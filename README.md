# Stickleback Lineage-Specific Gene Discovery Pipeline

A comparative genomics and bioinformatics research pipeline focused on identifying candidate lineage-specific and potential de novo genes in three-spined stickleback using orthogroup analysis, phylogenetic workflows, and large-scale homology searches.

This project combines computational biology methods, evolutionary analysis, and HPC-based workflows to investigate gene evolution across multiple fish species.

---

## Overview

The pipeline analyzes orthogroups generated across multiple stickleback species:

- Three-spined stickleback
- Four-spined stickleback
- Nine-spined stickleback

The primary goal is to identify:
- species-specific orthogroups
- lineage-specific genes
- candidate de novo genes lacking detectable homology outside sticklebacks

The workflow integrates orthogroup filtering, FASTA sequence extraction, phylogenetic tree analysis, and large-scale DIAMOND BLASTP searches on an HPC cluster.

---

## Features

- Orthogroup filtering and comparative genomics workflows
- Automated phylogenetic gene tree retrieval using the Ensembl REST API
- Genetic distance computation between species
- Large-scale homology searches with DIAMOND BLASTP
- FASTA and BED file processing
- Candidate lineage-specific gene filtering
- Automated Newick (`.nwk`) tree generation and parsing
- HPC-compatible Bash and Python workflows
- Evolutionary relationship analysis across fish species

---

## Research Goals

- Identify threespine-specific orthogroups
- Extract candidate protein-coding genes
- Perform large-scale homology searches
- Filter proteins lacking non-self hits
- Analyze phylogenetic relationships between species
- Generate high-confidence candidate de novo genes

---

## Dataset Summary

| Category | Count |
|---|---|
| Threespine-specific orthogroups | 899 |
| Extracted threespine gene IDs | 1,959 |
| Predicted protein sequences | 795 |
| Swiss-Prot no-hit proteins | 347 |
| High-confidence lineage-specific candidates | 219 |

---

## Technologies Used

### Bioinformatics Tools
- OrthoFinder
- DIAMOND BLASTP
- BLAST+
- Biopython
- ETE Toolkit
- MEGA

### Programming & Analysis
- Python
- Bash
- R
- Linux Command Line

### Infrastructure
- SLURM HPC Cluster
- Remote Linux Environment

---

## Pipeline Workflow

### 1. Orthogroup Analysis

Species-specific orthogroups were identified using OrthoFinder output files.

Filtering criteria:
- Three-spined stickleback > 0
- Four-spined stickleback = 0
- Nine-spined stickleback = 0

Input files:
```text
Orthogroups.GeneCount.tsv
Orthogroups.tsv
```

---

### 2. Gene & Protein Extraction

Candidate threespine gene IDs were extracted and matched protein sequences were retrieved from OrthoFinder FASTA outputs.

Generated outputs:
```text
threespine_gene_ids.txt
threespine_unique_proteins.fa
```

---

### 3. Homology Searches

Large-scale similarity searches were performed using DIAMOND BLASTP against:
- Swiss-Prot
- UniRef90
- RefSeq

Example command:

```bash
diamond blastp \
  -d swissprot.dmnd \
  -q threespine_unique_proteins.fa \
  -o diamond_results.tsv \
  --outfmt 6 \
  --sensitive
```

---

### 4. Candidate De Novo Gene Filtering

Proteins lacking significant non-self hits were retained as candidate lineage-specific or potential de novo genes.

Filtering included:
- self-hit removal
- low-quality alignment filtering
- cross-database validation

---

### 5. Phylogenetic Analysis

Additional Python workflows retrieve and analyze phylogenetic gene trees from the Ensembl REST API.

These scripts:
- generate `.nwk` Newick tree files
- compute genetic distances between species
- analyze evolutionary relationships
- export structured CSV analysis tables

---

## Python Workflow Scripts

### `biofind.py`

Retrieves phylogenetic gene trees directly from Ensembl and saves them as `.nwk` files for downstream evolutionary analysis.

Run:

```bash
python3 biofind.py
```

---

### `bioinfo.py`

Computes genetic and evolutionary distances between species using parsed Newick trees and exports structured CSV tables.

Run:

```bash
python3 bioinfo.py
```

Output:
```text
EDA_distance_table.csv
```

---

### `bioinfo1.py`

Interactive workflow that allows users to input species names and Ensembl gene IDs dynamically to retrieve phylogenetic gene trees.

Run:

```bash
python3 bioinfo1.py
```

---

## Example Workflow

1. Identify lineage-specific orthogroups
2. Extract candidate protein sequences
3. Run large-scale homology searches
4. Filter non-homologous proteins
5. Retrieve phylogenetic gene trees
6. Compute interspecies evolutionary distances
7. Export structured downstream analysis tables

---

## Project Structure

```text
stickleback-gene-analysis/
├── scripts/
│   ├── extract_threespine_orthogroups.sh
│   ├── extract_proteins.sh
│   └── run_diamond.sh
│
├── phylogenetics/
│   ├── biofind.py
│   ├── bioinfo.py
│   └── bioinfo1.py
│
├── data/
│   ├── lineage_specific_locations.bed
│   ├── Danio_rerio.fa
│   └── *.nwk
│
├── results/
│   ├── EDA_distance_table.csv
│   └── diamond_results.tsv
│
└── README.md
```

---

## Key Findings

- Many orthogroups showed lineage-specific duplicate expansions
- Hundreds of proteins lacked detectable homologs outside sticklebacks
- Candidate de novo genes may contribute to adaptive evolution in sticklebacks
- Comparative phylogenetic analysis revealed varying evolutionary distances across fish species

---

## Future Improvements

- Expanded multi-species genomic analysis
- Automated orthogroup classification
- Transcriptomic expression validation
- Interactive phylogenetic visualizations
- Additional HPC workflow automation
- Statistical evolutionary modeling pipelines

---

## Author

Aanya Bharti  
Bioinformatics Research Assistant  
University of Massachusetts Lowell

Advisor: Dr. Frederic Chain

---

## Acknowledgements

- Ensembl REST API
- Biopython
- OrthoFinder
- DIAMOND BLASTP
- Open-source bioinformatics research tools
