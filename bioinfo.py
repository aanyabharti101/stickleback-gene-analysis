# DRAFT1:
#This version shows how I can pull the EDA gene tree for several fish species automatically.
#Each species gets its own .nwk file, which can be opened in a phylogenetic viewer like iTOL or FigTree.
#It uses the genetree/member/id endpoint, so each call returns the full Newick tree and the shared tree ID.”


# fish_gene_trees.py
import requests

# A few example fish genes, list can be expanded
genes = {
    "gasterosteus_aculeatus": ["ENSGACG00000017632"],  # Stickleback EDA

}

for species, gene_ids in genes.items():
    for gene_id in gene_ids:
        url = f"https://rest.ensembl.org/genetree/member/id/{species}/{gene_id}"
        headers = {"Content-Type": "application/json"}
        print(f"\n Fetching tree for {gene_id} ({species})...")
        response = requests.get(url, headers=headers)

        if not response.ok:
            print(f" Error fetching {gene_id}: {response.status_code}")
            continue

        data = response.json()
        tree_id = data.get("id", "N/A")
        tree_code = data.get("tree", "")

        print(f" {gene_id} → Tree {tree_id}")
        filename = f"{species}_{gene_id}_tree.nwk"
        with open(filename, "w") as f:
            f.write(tree_code)
        print(f" Saved tree to {filename}")





#DRAFT2:

#This second version lets a user input any fish species and Ensembl gene ID interactively.
#It fetches the corresponding gene tree and shows the Newick structure, while saving tree to a file.


# get_fish_tree.py

import requests
import textwrap

print(" Ensembl Fish Gene Tree Fetcher")
print("———————————————")

# Ask user for species and gene ID
species = input("Enter fish species (e.g. gasterosteus_aculeatus): ").strip()
gene_id = input("Enter Ensembl Gene ID (e.g. ENSGACG00000017632): ").strip()

# Build the request URL
url = f"https://rest.ensembl.org/genetree/member/id/{species}/{gene_id}"
headers = {"Content-Type": "application/json"}

print("\n🔎 Fetching tree from Ensembl...")
response = requests.get(url, headers=headers)

if not response.ok:
    print(f" Error: {response.status_code} - {response.text}")
    exit()

data = response.json()

# Extract key info
tree_id = data.get("id", "N/A")
tree_newick = data.get("tree", "")

# Show summary
print(f"\n Tree retrieved successfully!")
print(f"   Gene Tree ID: {tree_id}")
print(f"   Tree length: {len(tree_newick)} characters")

# Show a short preview of the tree
print("\n Tree code (Newick format, first 250 chars):")
print(textwrap.fill(tree_newick[:250] + "...", width=80))

# Save the tree to a file
filename = f"{species}_{gene_id}_tree.nwk"
with open(filename, "w") as f:
    f.write(tree_newick)

print(f"\n Full tree saved to: {filename}")
print("Done!")




