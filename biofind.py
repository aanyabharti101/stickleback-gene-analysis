# bioinfo_EDA_distance.py
from io import StringIO
from Bio import Phylo
import pandas as pd

# Replace with your Newick tree file
newick_file = "gasterosteus_aculeatus_ENSGACG00000008041_genetree.nwk"

# Load the tree
tree = Phylo.read(newick_file, "newick")

# The target species label (stickleback)
target_label = "ENSGACG00000008041"  # update if different

# Find the target clade
target_clade = None
for clade in tree.find_clades():
    if target_label in str(clade.name):
        target_clade = clade
        break

if not target_clade:
    raise ValueError(f"Target label '{target_label}' not found in tree!")

# Compute distance from target to all other tips
data = []
for leaf in tree.get_terminals():
    if leaf.name == target_label:
        continue
    dist = tree.distance(target_clade, leaf)
    # Extract species name (assuming format like "ENSGACG00000008041_Gasterosteus_aculeatus")
    parts = leaf.name.split("_")
    species_name = "_".join(parts[1:]) if len(parts) > 1 else leaf.name
    data.append([species_name, dist])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Species", "Genetic Distance"])

# Sort by distance
df = df.sort_values("Genetic Distance").reset_index(drop=True)

# Save and print
df.to_csv("EDA_distance_table.csv", index=False)
print(df)
print("\n Table saved as 'EDA_distance_table.csv'")
