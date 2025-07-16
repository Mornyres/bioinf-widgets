#import Bio
from Bio import SeqIO
#import networkx as nx
import streamlit as st


from utils.fasta import fasta_file
from utils.pdb import PDB


st.title("Basic proteomics widget")

#option = st.sidebar.selectbox("Choose analysis type", ["Protein sequence proteomics (FASTA)", "Protein Visualization (PDB)"])
with open('./README.md','r') as f:
    readme_content = f.read()

with st.expander("About", expanded=True):
    st.markdown(readme_content)
st.markdown('''
    #### By :green[Forest LeBlanc]  
    [forestleblanc.com](https://forestleblanc.com/)
    ''')

st.subheader("Protein sequence proteomics (FASTA)")
#with st.expander("Protein sequence proteomics (FASTA)"):
#if option == "Protein sequence proteomics (FASTA)":
    # Upload FASTA
    
fasta_file_input = st.file_uploader("Upload a protein FASTA file", type=["fasta", "fa"])

if fasta_file_input is not None:
    fasta_input = fasta_file_input
    st.subheader("Sequence Information")
    fasta_file = fasta_file(file=fasta_input)

else:
    fasta_input = "./examples/crab_anapl.fasta"
    st.subheader("Sequence Information (example file)")
    fasta_file = fasta_file(file_handler=fasta_input)

fasta_file.format_summary(summary_only=False, exclude=[])


st.subheader("Protein Visualization (PDB)")
#with st.expander("Protein Visualization (PDB)"):
#elif option == "Protein Visualization (PDB)":

pdb_file = st.file_uploader("Upload a protein PDB file", type=["pdb","ent"])

if pdb_file is not None:
    # Structure viewer
    st.subheader("Protein Structure Viewer")
    pdb = PDB(file=pdb_file) 
    
else:
    st.subheader("Protein Structure Viewer (example PDB file)")
    pdb_filepath = "./examples/pdb1aoi.ent"
    pdb = PDB(filepath=pdb_filepath)   

st.write(pdb.format())
pdb.show_structure_file()