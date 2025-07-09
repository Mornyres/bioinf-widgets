import plotly.express as px
import plotly.graph_objects as go

#def plot_composition(comp_dict):
#    df = [{"AA": aa, "Fraction": frac} for aa, frac in comp_dict.items()]
#   return px.bar(df, x="AA", y="Fraction", title="Amino Acid Composition")

def create_composition_plot(comp):
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