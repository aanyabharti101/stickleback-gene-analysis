import pandas as pd
from ete3 import Tree, TreeStyle, RectFace, faces, TextFace, NodeStyle

# load BED file
genes = pd.read_csv("lineage_specific_locations.bed",
                    sep="\t",
                    header=None,
                    names=["chr","start","end","strand","transcript","geneID","gene_label"])

chromosomes = genes["chr"].unique()

def make_chrom_tree(chrom_name, df):
    t = Tree()
    t.name = chrom_name

    nstyle = NodeStyle() 
    nstyle["size"] = 0
    t.set_style(nstyle)

    for _, row in df.iterrows():
        n = t.add_child(name=row["geneID"])

        gene_color = "#1b9e77" if row["strand"] == "+" else "#d95f02"

        gene_block = RectFace(
            width=25,
            height=12,
            fgcolor="black",
            bgcolor=gene_color
        )

        faces.add_face_to_node(gene_block, n, column=0, position="branch-right")

        label = TextFace(row["geneID"], fsize=8)
        faces.add_face_to_node(label, n, column=1, position="branch-right")

    return t

trees = []

for chrom in chromosomes:
    df = genes[genes["chr"] == chrom]
    trees.append(make_chrom_tree(chrom, df))

ts = TreeStyle()
ts.mode = "c"     # circular = oval chromosome look
ts.show_leaf_name = False
ts.title.add_face(TextFace("Chromosome Gene Map", fsize=16), column=0)

for tree in trees:
    tree.show(tree_style=ts)
