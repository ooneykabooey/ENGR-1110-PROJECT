import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Causers/political-instability/44434f2a-76b4-4a7b-99d6-24b0b8933456_Data.csv")

# Rename columns for easier handling
df = df.rename(columns={
    "Country Name": "Country",
    "Country Code": "Code",
    "Series Name": "Series",
    "Series Code": "SeriesCode",
})

# ---- Clean the dataset ----

# Keep only the political stability dataset
df = df[df["Series"] == "Political Stability and Absence of Violence/Terrorism: Estimate"]

# Convert wide year columns into long format
year_cols = [col for col in df.columns if col.endswith("]")]

df_long = df.melt(
    id_vars=["Country", "Code", "Series", "SeriesCode"],
    value_vars=year_cols,
    var_name="Year",
    value_name="Value"
)

# Extract numeric year (e.g. "2000 [YR2000]" → 2000)
df_long["Year"] = df_long["Year"].str.extract(r"(\d{4})").astype(int)

# Remove rows with missing ".." values
df_long = df_long.replace("..", None).dropna(subset=["Value"])

# Convert values to float
df_long["Value"] = df_long["Value"].astype(float)

# Sort by year for slider consistency
df_long = df_long.sort_values("Year")


# ---- Create Choropleth ----
fig = px.choropleth(
    df_long,
    locations="Code",               # uses ISO 3 country codes
    color="Value",
    hover_name="Country",
    animation_frame="Year",         # slider
    color_continuous_scale="Viridis",
    title="Political Stability and Absence of Violence (World Governance Indicators)"
)

# Hide autoplay button (optional)
fig.layout.updatemenus[0].buttons[0]["visible"] = False

fig.show()
