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

df = pd.read_csv('../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Causers/economic-inequality/gini-coefficient.csv')

# Rename for easy referencing
df = df.rename(columns={
    "Gini coefficient (before tax) (World Inequality Database)": "Gini"
})

# Convert Year to a numeric value for sorting
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Drop data without any gini coefficient
df = df.dropna(subset=['Gini'])

# Sort by Year
df['Year'] = df['Year'].astype(int)
df = df.sort_values(by='Year', ascending=True)

# Build figure
fig = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="Gini",
    hover_name="Country",
    animation_frame="Year",
    color_continuous_scale=px.colors.sequential.Blues,
    title="Gini Coefficient (before tax), Over Time (WID)"
)

# Show
fig.show()


