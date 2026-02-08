import plotly.express as px
from .styles import CUSTOM_COLOR_SCALE

def plot_generic_choropleth(data, geojson, locations_col, feature_key, value_col, title, labels_map):
    fig = px.choropleth(
        data,
        geojson=geojson,
        locations=locations_col,
        featureidkey=feature_key,
        color=value_col,
        color_continuous_scale=CUSTOM_COLOR_SCALE,
        title=title,
        labels=labels_map
    )

    fig.update_geos(fitbounds="locations", visible=False)

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        geo_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=30, b=0),
        coloraxis_colorbar=dict(title=labels_map.get(value_col, "Valor"))
    )
    
    return fig