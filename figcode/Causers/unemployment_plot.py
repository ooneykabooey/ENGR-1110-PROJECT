import csv

# AUTHOR: Levi Daniel - lcd0063@auburn.edu

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

# Load main WDI dataset (the one with 1960, 1961, ...)
df = pd.read_csv(
    "../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Causers/unemployment/API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_130165.csv", skiprows=4)
df.columns = df.columns.str.strip()  # remove any accidental whitespace

# Load indicator info
indicators = pd.read_csv(
    "../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Causers/unemployment/Metadata_Indicator_API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_130165.csv")
indicators.columns = indicators.columns.str.strip()

# Filter to unemployment indicator
indicator_code = "SL.UEM.TOTL.ZS"
df = df[df["Indicator Code"] == indicator_code]

# Drop unused columns
value_cols = [col for col in df.columns if col.isdigit()]
id_cols = ["Country Name", "Country Code"]
df = df[id_cols + value_cols]

# Convert from wide to long format
df_long = df.melt(
    id_vars=id_cols,
    var_name="Year",
    value_name="UnemploymentRate"
)

# Convert year to number
df_long["Year"] = df_long["Year"].astype(int)

# Remove rows with missing data
df_long = df_long.dropna(subset=["UnemploymentRate"])

# Create interactive map with slider
fig = px.choropleth(
    df_long,
    locations="Country Code",
    color="UnemploymentRate",
    hover_name="Country Name",
    animation_frame="Year",
    color_continuous_scale="Viridis",
    title="Unemployment Rate Over Time"
)

fig.update_layout(
    coloraxis_colorbar=dict(title="% Unemployed"),
    margin=dict(l=0, r=0, t=50, b=0)
)

fig.show()