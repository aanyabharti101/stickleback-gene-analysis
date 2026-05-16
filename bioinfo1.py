import requests

species = "gasterosteus_aculeatus"
gene_id = "ENSGACG00000008041"  # official EDA gene

headers = {"Accept": "text/x-nh"}

for tree_type in ["genetree", "cafe/genetree"]:
    url = f"https://rest.ensembl.org/{tree_type}/member/id/{species}/{gene_id}"
    print(f"\nFetching {tree_type} for {gene_id} ({species})...")

    response = requests.get(url, headers=headers)
    if not response.ok:
        print(f"Error fetching {tree_type}: {response.status_code}")
        continue

    tree_code = response.text.strip()
    if not tree_code:
        print(f"⚠️ Empty tree returned for {tree_type}")
        continue

    filename = f"{species}_{gene_id}_{tree_type.replace('/', '_')}.nwk"
    with open(filename, "w") as f:
        f.write(tree_code)

    print(f"✅ Saved {tree_type} tree → {filename}")
