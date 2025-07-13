#import Bio
from Bio import SeqIO
#import networkx as nx
import streamlit as st
from io import StringIO


from utils.fasta import fasta_record
from utils.plot import create_composition_plot
from utils.pdb import PDB

st.title("Basic proteomics widget")

#option = st.sidebar.selectbox("Choose analysis type", ["Protein sequence proteomics (FASTA)", "Protein Visualization (PDB)"])

with st.expander("Protein sequence proteomics (FASTA)"):
#if option == "Protein sequence proteomics (FASTA)":
    # Upload FASTA
    
    fasta_file = st.file_uploader("Upload a protein FASTA file", type=["fasta", "fa"])

    if fasta_file is not None:
        input_string = StringIO(fasta_file.getvalue().decode("utf-8"))
        st.subheader("Sequence Information")

    else:
        input_string = "./examples/crab_anapl.fasta"
        st.subheader("Sequence Information (example file)")


    i = 1
    for record_text in SeqIO.parse(input_string, 'fasta'):
        st.subheader(f"Record {i}")
        record = fasta_record(record_text)
        
        st.write(record.format())

        st.plotly_chart(create_composition_plot(dict(record.aa_composition)))
        i = i + 1


with st.expander("Protein Visualization (PDB)"):
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