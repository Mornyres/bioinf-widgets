Just a small little experiment with Streamlit and some bioinformatics tools in Python.

Proteomics is the analysis of proteins to understand their function. This is important because proteins interact together to form biological 'machines' in living things that can carry out extremely complex actions.

This widget has 2 closely related tools. 

The first processes a FASTA sequence ([Wikipedia](https://en.wikipedia.org/wiki/FASTA_format)) which describes the amino acid sequence of the protein. It provides some analysis based on this file.

The second processes a PDB file ([Wikipedia](https://en.wikipedia.org/wiki/Protein_Data_Bank_(file_format))) representing the protein's physical structure. It provides a 3D graph of the protein.

#### Feature plans/ideas for future
-	More background info, help tips, etc.
-   More customizability in output (e.g. only show aggregate summary for multi-record FASTA)
-	More detailed FASTA sequence analysis (e.g. AA consensus or other aggregated data)
-	Selectable graph style for PDB (e.g. highlighting alpha helices and beta sheets, or different styles such as ribbon diagrams)
-	Graph annotation for PDB
-	Ability to reference PDB and FASTA from online databases by ID rather than inputting files
-	Given both PDB (physical structure) and FASTA (AA sequence) for the same protein, at least some rudimentary function prediction


**Concepts:** *Bioinformatics, Python, Data science, proteomics*

**Tools:** *Streamlit, BioPython, Pandas, plotly, numpy, py3Dmol*