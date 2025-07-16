import streamlit.components.v1 as components
import py3Dmol
from Bio.PDB import PDBParser
from io import StringIO

# Allow nullable parameters for formatting metadata output in case we have an oddly formed input file
nf = lambda pdb, x: x if (pdb.hasattr(x) and pdb.getattr(x) is not None) else "N/A"

class PDB():
    def __init__(self, filepath=None, file=None, id=None):

        if filepath is not None:
            self.file_handler = filepath
            with open(filepath,'r') as f:
                self.pdb_content = f.read()

        elif file is not None:
            self.pdb_content = file.getvalue().decode("utf-8")
            self.file_handler = StringIO(file.getvalue().decode("utf-8"))

        elif id is not None:
            None

        else:
            raise ValueError("Provide either PDB ID or .pdb file")
        
        parser = PDBParser()
        
        
        self.structure = parser.get_structure('protein_id', self.file_handler)
        
        self.header_info = self.structure.header

        self.title = self.header_info.get('name') 
        self.keywords = self.header_info.get('keywords')

    def format(self):
        return {
            "Title": self.title,
            "Keywords" : self.keywords,
        }
    
    def show_structure_id(self):
        
        view = py3Dmol.view(query=f"pdb:{pdb_id}", width=600, height=400)
        view.setStyle({'cartoon': {'color': 'spectrum'}})
        view.zoomTo()
        view.render()
        components.html(view._make_html(), height=400)

    def show_structure_file(self):

        # if self.file is not None:
        #     pdb_content = self.file
        # elif self.pdb_filepath is not None:
        #     with open(self.pdb_filepath, 'r') as f:
        #         pdb_content = f.read()

        pdb_content = self.pdb_content
        view = py3Dmol.view(width=600, height=400)
        view.addModel(pdb_content, "pdb")
        view.setStyle({"cartoon": {"color": "spectrum"}})
        view.zoomTo()
        view.render()
        components.html(view._make_html(), height=400)
