import pandas as pd
import plotly.express as px
from IPython.display import HTML
import uuid

# -----------------------------
# Load crime dataset
# -----------------------------
df = pd.read_csv("../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Impacts/crime-rate/global_oc_index.csv")  # replace with your path

# Columns to use for tabs
crime_columns = [
    "Criminality avg.",
    "Criminal markets avg.",
    "Human trafficking",
    "Human smuggling",
    "Extortion and protection racketeering",
    "Arms trafficking",
    "Trade in counterfeit goods",
    "Illicit trade in excisable goods",
    "Flora crimes",
    "Fauna crimes",
    "Non-renewable resource crimes",
    "Heroin trade",
    "Cocaine trade",
    "Cannabis trade",
    "Synthetic drug trade",
    "Cyber-dependent crimes",
    "Financial crimes",
    "Criminal actors avg.",
    "Mafia-style groups",
    "Criminal networks",
    "State-embedded actors",
    "Foreign actors",
    "Private sector actors",
    "Resilience avg."
]

# Convert numeric columns
for col in crime_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------
# Create Plotly figures for each crime type
# -----------------------------
figs = {}
for col in crime_columns:
    fig = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color=col,
        hover_name="Country",
        color_continuous_scale="Reds",
        title=f"Global {col}"
    )
    figs[col] = fig

# -----------------------------
# Function to create HTML tabs
# -----------------------------
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
            <button class="tablinks_{tab_id}" onclick="openTab_{tab_id}(event, 'tab_{i}_{tab_id}')">{title[:20]}</button>
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
            margin-right: 2px;
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

# -----------------------------
# Display tabs
# -----------------------------
make_tabs(figs)
