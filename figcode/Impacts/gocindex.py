import pandas as pd
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display, clear_output

# -----------------------------
# Load your dataset
# -----------------------------
df = pd.read_csv("../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Impacts/crime-rate/global_oc_index.csv")  # <-- change to your file name

# Fix country column
df = df.rename(columns={"Country": "Country"})

# Crime-related numeric columns
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
    "Resilience avg.",
]

# Ensure numeric values
for col in crime_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------
# Function to draw the map
# -----------------------------
def make_map(crime_type):
    clear_output(wait=True)  # clears previous map
    display(dropdown)        # keeps dropdown visible

    fig = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color=crime_type,
        hover_name="Country",
        color_continuous_scale="Reds",
        title=f"Global {crime_type}",
    )
    fig.update_layout(height=600)
    fig.show()

# -----------------------------
# Dropdown widget
# -----------------------------
dropdown = widgets.Dropdown(
    options=crime_columns,
    value="Criminality avg.",
    description="Crime Type:",
    layout=widgets.Layout(width="50%")
)

# Callback
def on_change(change):
    if change["type"] == "change" and change["name"] == "value":
        make_map(change["new"])

dropdown.observe(on_change)

# Display UI
display(dropdown)
make_map(dropdown.value)
