import csv

# AUTHOR: Levi Daniel - lcd0063@auburn.edu

### Libraries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import requests
import json
import textwrap

## Python Stuff
import random
import re
import io
import math

from IPython.display import HTML
import uuid


def make_tabs(fig_dict):
    tab_id = str(uuid.uuid4()).replace('-', '')

    # Build the tab headers
    tab_buttons = ""
    tab_contents = ""

    for i, (title, fig) in enumerate(fig_dict.items()):
        # Convert each figure to HTML
        fig_html = fig.to_html(include_plotlyjs=(i == 0))  # Load JS only once

        # Tab button
        tab_buttons += f"""
            <button class="tablinks_{tab_id}" onclick="openTab_{tab_id}(event, 'tab_{i}_{tab_id}')">{title}</button>
        """

        # Tab content
        tab_contents += f"""
            <div id="tab_{i}_{tab_id}" class="tabcontent_{tab_id}" style="display:{'block' if i == 0 else 'none'};">
                {fig_html}
            </div>
        """

    # Full HTML structure
    full_html = f"""
    <style>
        .tab_{tab_id} {{
            overflow: hidden;
            border-bottom: 1px solid #ccc;
        }}
        .tab_{tab_id} button {{
            background-color: #444;
            border: none;
            outline: none;
            cursor: pointer;
            padding: 10px 16px;
            transition: 0.3s;
            color: white;
        }}
        .tab_{tab_id} button:hover {{
            background-color: #666;
        }}
        .tabcontent_{tab_id} {{
            display: none;
            padding-top: 10px;
        }}
    </style>

    <div class="tab_{tab_id}">
        {tab_buttons}
    </div>

    {tab_contents}

    <script>
    function openTab_{tab_id}(evt, tabName) {{
        var i, tabcontent, tablinks;
        tabcontent = document.getElementsByClassName("tabcontent_{tab_id}");
        for (i = 0; i < tabcontent.length; i++) {{
            tabcontent[i].style.display = "none";
        }}
        tablinks = document.getElementsByClassName("tablinks_{tab_id}");
        for (i = 0; i < tablinks.length; i++) {{
            tablinks[i].style.backgroundColor = "#444";
        }}
        document.getElementById(tabName).style.display = "block";
        evt.currentTarget.style.backgroundColor = "#222";
    }}
    </script>
    """

    return HTML(full_html)



##### DATA (Abbreviated from the .csv files)

ghi = pd.read_csv(
    '../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Causers/global-hunger-index/global-hunger-index.csv', delimiter=',')
scu = pd.read_csv(
    '../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Causers/global-hunger-index/share-of-children-underweight.csv', delimiter=',', quotechar='"', engine='python')
scwlh = pd.read_csv(
    '../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Causers/global-hunger-index/share-of-children-with-a-weight-too-low-for-their-height-wasting.csv', delimiter=',', quotechar='"', engine='python')
scy5ss = pd.read_csv(
    '../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Causers/global-hunger-index/share-of-children-younger-than-5-who-suffer-from-stunting.csv', delimiter=',')


## Take the code from each dataset
ghi = ghi[ghi['Code'].str.len() == 3].copy()
scu = scu[scu['Code'].str.len() == 3].copy()
scwlh = scwlh[scwlh['Code'].str.len() == 3].copy()
scy5ss = scy5ss[scy5ss['Code'].str.len() == 3].copy()





figghi = px.choropleth(
    ghi,
    locations="Code",
    color="Global Hunger Index (2021)",
    hover_name="Entity",
    color_continuous_scale="Plasma",
    locationmode="ISO-3",
    range_color=(0, ghi['Global Hunger Index (2021)'].max()),
    hover_data={"Global Hunger Index (2021)": ":,0f" + "Global Hunger Index (2021)",
                "Code": False},
    scope="world"
)

figscu = px.choropleth(
    scu,
    locations="Code",
    color="Prevalence of underweight, weight for age (% of children under 5)",
    hover_name="Entity",
    color_continuous_scale="Viridis",
    locationmode="ISO-3",
    range_color=(0, scu["Prevalence of underweight, weight for age (% of children under 5)"].max()),
    hover_data={"Prevalence of underweight, weight for age (% of children under 5)": ":,0f" + "% of Children Affected",
                "Code": False},
    scope="world"
)

figscwlh = px.choropleth(
    scwlh,
    locations="Code",
    color="Prevalence of wasting, weight for height (% of children under 5)",
    hover_name="Entity",
    color_continuous_scale="Sunsetdark",
    locationmode="ISO-3",
    range_color=(0, scwlh["Prevalence of wasting, weight for height (% of children under 5)"].max()),
    hover_data={"Prevalence of wasting, weight for height (% of children under 5)": ":,0f" + "% of Children Affected",
                "Code": False},
    scope="world"
)

figscy5ss = px.choropleth(
    scy5ss,
    locations="Code",
    color="Prevalence of stunting, height for age (% of children under 5)",
    hover_name="Entity",
    color_continuous_scale="Sunsetdark",
    locationmode="ISO-3",
    range_color=(0, scy5ss["Prevalence of stunting, height for age (% of children under 5)"].max()),
    hover_data={"Prevalence of stunting, height for age (% of children under 5)": ":,0f" + "% of Children Affected",
                "Code": False},
    scope="world"
)

app = Dash(__name__)

# Your existing figures
figs = {
    "Global Hunger Index": figghi,
    "Underweight (% under 5)": figscu,
    "Wasting (% under 5)": figscwlh,
    "Stunting (% under 5)": figscy5ss
}

make_tabs(figs)

### PYCHARM DOESNT SUPPORT HTML TABS, THIS WORKS ONLY IN NOTEBOOK ENVIRONMENTS, SUCH AS GOOGLE COLAB.