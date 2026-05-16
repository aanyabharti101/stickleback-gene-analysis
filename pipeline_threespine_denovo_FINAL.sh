#!/bin/bash


# Author: Aanya Bharti
# Project: Threespine Stickleback De Novo Gene Identification
# Description: Full pipeline for identifying lineage-specific candidate genes using DIAMOND BLASTP
# Date: April 2026

# ==========================================
# PIPELINE: Threespine de novo gene detection
# ==========================================

# Working directory
cd /project/pi_frederic_chain_uml_edu/Stickleback/OutgroupsProteins/OrthoFinder/Results_Jun11

# ==========================================
# STEP 1: Extract threespine unassigned proteins
# ==========================================

cd Orthogroup_Sequences

# Count sequences (sanity check)
grep -c '^>' threespine_unassigned_proteins.fa
# Expected: 1460

# ==========================================
# STEP 2: DIAMOND BLASTP vs UniRef90
# ==========================================

cd ../DIAMOND_RESULTS

# Run DIAMOND (submitted via sbatch)
# Input: full-length protein sequences
# Output: alignment results

diamond blastp \
  -d /project/pi_frederic_chain_uml_edu/DIAMOND_DB/uniref90.dmnd \
  -q ../Orthogroup_Sequences/threespine_unassigned_proteins.fa \
  -o threespine_vs_uniref90_FULL_v2.diamond.tsv \
  --outfmt 6 qseqid sseqid pident evalue bitscore stitle \
  --max-target-seqs 5 \
  --evalue 1e-3 \
  --threads 8

# ==========================================
# STEP 3: Identify sequences with hits
# ==========================================

cut -f1 threespine_vs_uniref90_FULL_v2.diamond.tsv | sort -u > uniref_hits.txt

# ==========================================
# STEP 4: Get all query IDs
# ==========================================

grep "^>" ../Orthogroup_Sequences/threespine_unassigned_proteins.fa | \
sed 's/^>//' | awk '{print $1}' | sort -u > all_ids.txt

# ==========================================
# STEP 5: Identify no-hit candidates
# ==========================================

comm -23 all_ids.txt uniref_hits.txt > FINAL_nohit_candidates_77_fullLength.txt

# Count final candidates
wc -l FINAL_nohit_candidates_77_fullLength.txt
# Expected: 77

# ==========================================
# STEP 6: Map candidates to genome coordinates
# ==========================================

grep -F -f FINAL_nohit_candidates_77_fullLength.txt \
/project/pi_frederic_chain_uml_edu/Stickleback/Genome/stickleback_v5_ensembl_maker_genes_chrY.gff3.mRNA.bed \
> lineage_specific_locations_FINAL77.bed

# ==========================================
# STEP 7: Convert to TSV for visualization
# ==========================================

awk 'BEGIN{OFS="\t"} {print $5,$1,$2,$3,$4,$7}' \
lineage_specific_locations_FINAL77.bed \
> final_candidates_FINAL77.tsv
