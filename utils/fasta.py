from Bio import SeqIO
from Bio.SeqUtils import molecular_weight, IsoelectricPoint as iep
from collections import Counter
from io import StringIO

import streamlit as st

import plotly.express as px
import plotly.graph_objects as go

aa_hydrophobicity = {
    'A': 1.8,  'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
    'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
    'L': 3.8,  'K': -3.9, 'M': 1.9,  'F': 2.8,  'P': -1.6,
    'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
}

aa_commonNames = {
    "A": "alanine",
    "R": "arginine",
    "N": "asparagine",
    "D": "aspartic acid",
    "C": "cysteine",
    "Q": "glutamine",
    "E": "glutamic acid",
    "G": "glycine",
    "H": "histidine",
    "I": "isoleucine",
    "L": "leucine",
    "K": "lysine",
    "M": "methionine",
    "F": "phenylalanine",
    "P": "proline",
    "S": "serine",
    "T": "threonine",
    "W": "tryptophan",
    "Y": "tyrosine",
    "V": "valine"
}

class fasta_file:
    def __init__(self, file=None, file_handler=None):
        if file is not None:
            self.file_handler = StringIO(file.getvalue().decode("utf-8"))
        elif file_handler is not None:
            self.file_handler = file_handler
        else:
            raise ValueError("Provide either FASTA filepath or .pdb file")
        
        self.records = []

        for record_text in SeqIO.parse(self.file_handler, 'fasta'):
            record = fasta_record(record_text)
            self.records.append(record)

    def format_summary(self, summary_only = False, exclude = []):
            nRecords = len(self.records)
            for idx,record in enumerate(self.records):
                if idx not in exclude:
                    if (summary_only and (nRecords >= 2)):
                        continue
                    else:
                        st.subheader(f"Record {idx + 1}")
                        st.write(record.format())

                        st.plotly_chart(record.composition_plot())

            if (nRecords >= 2):
                st.subheader(f"Aggregate")
                st.text("TODO")
                # TODO: consensus if all records same length

class fasta_record:
    def __init__(self, record):
        self.id = record.id
        self.seq = str(record.seq)
        self.is_valid = self.is_valid_sequence()
        
        self.mol_weight = molecular_weight(self.seq, seq_type="protein")
        self.iep = iep.IsoelectricPoint(self.seq).pi()
        self.aa_counts = Counter(str(self.seq))
        self.aa_composition = self.compute_composition()
        self.gravy = self.compute_gravy()


    def format(self):
        return {
            "ID": self.id,
            "Length": len(self.seq),
            "Molecular Weight (Da or g/mol)": self.mol_weight,
            "Isoelectric Point (pI)": round(self.iep, 2),
            "Grand Average of Hydropathy (GRAVY)": round(self.gravy,2),
            "Amino Acid Composition": {f"{key} ({aa_commonNames[key]})": f"{value} ({round(self.aa_composition[key]*100.0,2)}%)" for key, value in dict(self.aa_counts).items()}
        }

    def compute_composition(self):
        total = sum(self.aa_counts.values())

        return {aa: count / total for aa, count in sorted(self.aa_counts.items())}
    
    def compute_gravy(self):
        return sum(aa_hydrophobicity[aa] for aa in self.seq) / len(self.seq)
    
    def is_valid_sequence(self):
        return all(aa in aa_hydrophobicity for aa in self.seq)
    
    def composition_plot(self):
        comp = dict(self.aa_composition)

        fig = go.Figure(data=[
            go.Bar(x=list(comp.keys()), y=list(comp.values()), marker_color="teal")
        ])

        fig.update_layout(
            title="Amino Acid Composition",
            xaxis_title="Amino Acid",
            yaxis_title="Proportion",
            yaxis=dict(range=[0, max(comp.values()) * 1.1]),
        )

        return fig