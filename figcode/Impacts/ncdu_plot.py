#
# @author LEVI DANIEL (lcd0063@auburn.edu)
#
#
#
#
#
## Libraries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd
import plotly.express as px
import requests
import json
import textwrap

## Python Stuff
import random
import re
import io
import math

# Func to wrap text
def wrap_text(text, width):
    """Wraps text via specified width, joined by HTML line breaks."""
    lines = textwrap.wrap(text, width=width)
    return "<br>".join(lines)

##### DATA

ncdu = pd.read_csv(
    '../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Impacts/ncdu/number-calorie-diet-unaffordable.csv', delimiter=',')

ncdu = ncdu[ncdu['Code'].str.len() == 3].copy()

with open(
        '../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Impacts/ncdu/number-calorie-diet-unaffordable.metadata.json', 'r') as f:
    metadata = json.load(f)

# Take the mappings from the .json and list them as variables
chart_title = metadata["chart"]["title"]
chart_subtitle = metadata["chart"]["subtitle"]
citation_text = metadata["columns"]["Number of people who cannot afford sufficient calories"]["citationLong"]
hover_unit = metadata["columns"]["Number of people who cannot afford sufficient calories"]["unit"]

# Wrap subtitle text at 150 chars.
wrapped_subtitle = wrap_text(chart_subtitle, width=150)

# choropleth (world map of data)
fig = px.choropleth(
    ncdu,
    locations="Code",
    color = "Number of people who cannot afford sufficient calories",
    locationmode="ISO-3",
    hover_name="Entity",
    color_continuous_scale=["#FFFFE0", "#FFA500","#FF0000", "#8B0000"],
    range_color=(0, ncdu['Number of people who cannot afford sufficient calories'].max()),  # Set color bar range
    hover_data={
        "Number of people who cannot afford sufficient calories": ':,0f ' + hover_unit,
        "Code": False},
    scope="world",
)

# Change how the color bar on the right presents itself.
fig.update_layout(
    coloraxis_colorbar=dict(
        title=f"{hover_unit}",
        tickformat=',.0f' # Use commas for thousands separator, no decimals
    ),
    # Add some margin to the bottom to make room for annotation
    margin=dict(b=150,t=100),
    # Subtitle below title
    title={
        'text': f"<b>{chart_title}</b><br><sup>{wrapped_subtitle}</sup>",
        'y': 0.98,  # Position near the top of the *figure*
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    width=1200,
    height=700
)

# Annotation citing source and any disclaimer about the data
fig.add_annotation(
    text="Source: Our World in Data (Data for 2021)",
    showarrow=False,
    xref="paper",  # Reference the figure paper as a whole
    yref="paper",  # Reference the figure paper as a whole
    x=0,  # Position X at the left edge of the figure
    y=-0.4,  # Position Y below the bottom of the map
    xanchor='left',  # Anchor the text to the left
    yanchor='top',  # Anchor the text to the top
    font=dict(size=10, color="grey"),
    align="left"
)

fig.show()