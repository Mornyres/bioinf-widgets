import streamlit.components.v1 as components
import py3Dmol

def show_structure_id(pdb_id):
    view = py3Dmol.view(query=f"pdb:{pdb_id}", width=600, height=400)
    view.setStyle({'cartoon': {'color': 'spectrum'}})
    view.zoomTo()
    view.render()
    components.html(view._make_html(), height=400)

def show_structure_file(pdb):
    view = py3Dmol.view(width=600, height=400)
    view.addModel(pdb, "pdb")
    view.setStyle({"cartoon": {"color": "spectrum"}})
    view.zoomTo()
    view.render()
    components.html(view._make_html(), height=400)
