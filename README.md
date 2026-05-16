# Three-Spined Stickleback De Novo Gene Discovery Pipeline

A comparative genomics and bioinformatics research pipeline focused on identifying candidate lineage-specific and potential de novo genes in three-spined stickleback using orthogroup analysis, large-scale homology searches, and downstream evolutionary analysis.

This project combines HPC-based workflows, sequence analysis, and computational genomics methods to investigate genes that may have originated uniquely within the three-spined stickleback lineage.

---

## Overview

The pipeline analyzes orthogroup datasets generated across multiple stickleback species with a primary focus on three-spined stickleback.

The main objective is to identify:
- three-spined stickleback-specific orthogroups
- lineage-specific genes
- candidate de novo genes lacking detectable homologs outside sticklebacks

The workflow integrates:
- orthogroup filtering
- protein sequence extraction
- DIAMOND BLASTP homology searches
- genomic coordinate mapping
- phylogenetic analysis
- downstream comparative genomics workflows

---

## Research Goals

- Identify threespine-specific orthogroups
- Extract candidate protein-coding genes
- Perform large-scale homology searches
- Filter proteins lacking significant non-self hits
- Investigate evolutionary relationships between candidate genes
- Generate high-confidence candidate lineage-specific genes

---

## Dataset Summary

| Category | Count |
|---|---|
| Threespine-specific orthogroups | 899 |
| Extracted threespine gene IDs | 1,959 |
| Predicted protein sequences | 795 |
| Swiss-Prot no-hit proteins | 347 |
| Final high-confidence candidate genes | 77 |

---

## Technologies & Tools

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

### 1. Orthogroup Identification

Orthogroups unique to three-spined stickleback were identified from OrthoFinder outputs by comparing gene presence across multiple stickleback species.

Input files:
```text
Orthogroups.GeneCount.tsv
Orthogroups.tsv
```

---

### 2. Protein Sequence Extraction

Candidate three-spined stickleback gene IDs were extracted and matching protein sequences were retrieved from OrthoFinder FASTA outputs.

Generated outputs:
```text
threespine_gene_ids.txt
threespine_unique_proteins.fa
```

---

### 3. DIAMOND BLASTP Homology Searches

Large-scale similarity searches were performed using DIAMOND BLASTP against:
- Swiss-Prot
- UniRef90
- RefSeq

Example command:

```bash
diamond blastp \
  -d uniref90.dmnd \
  -q threespine_unassigned_proteins.fa \
  -o threespine_vs_uniref90_FULL_v2.diamond.tsv \
  --outfmt 6 \
  --sensitive
```

The pipeline was executed on a SLURM-managed HPC cluster for large-scale sequence analysis.

---

### 4. Candidate Gene Filtering

Proteins lacking significant non-self hits were retained as candidate lineage-specific or potential de novo genes.

Filtering included:
- self-hit removal
- low-quality alignment filtering
- cross-database validation

Final candidate outputs:
```text
FINAL_nohit_candidates_77_fullLength.txt
```

---

### 5. Genome Coordinate Mapping

Candidate genes were mapped back to genomic coordinates using BED annotation files.

Generated outputs:
```text
lineage_specific_locations_FINAL77.bed
final_candidates_FINAL77.tsv
```

---

### 6. Phylogenetic & Evolutionary Analysis

Additional Python workflows were developed for phylogenetic analysis and evolutionary distance computation using the Ensembl REST API and Biopython.

These scripts:
- retrieve phylogenetic gene trees
- generate `.nwk` Newick tree files
- compute interspecies evolutionary distances
- export comparative analysis tables

Example scripts:

```bash
python3 biofind.py
python3 bioinfo.py
python3 bioinfo1.py
```

---

## Example Workflow

1. Identify three-spined stickleback-specific orthogroups
2. Extract candidate protein sequences
3. Perform large-scale homology searches
4. Filter proteins lacking detectable homologs
5. Map candidate genes to genomic coordinates
6. Retrieve phylogenetic gene trees
7. Compute evolutionary distances
8. Export downstream analysis tables and visualizations

---

## Key Findings

- Multiple orthogroups showed lineage-specific duplicate expansions
- Hundreds of proteins lacked detectable homologs outside sticklebacks
- 77 high-confidence candidate lineage-specific genes remained after stringent filtering
- Comparative phylogenetic analyses revealed varying evolutionary distances across fish species

---

## Future Improvements

- Expanded multi-species genomic comparisons
- Transcriptomic expression validation
- Automated orthogroup classification
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
