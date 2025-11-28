import pandas as pd
import plotly.express as px

# Load CSV
df = pd.read_csv("../../content/drive/MyDrive/COLAB/ENGR-1110-Project/Impacts/housing/IMF_GHW.csv")  # replace with your path

# Quick check
print(df.head())

# Filter for a specific quarter, e.g., 2021-Q4
df_q4 = df[df['TIME_PERIOD'] == '2021-Q4']

# Optional: ensure numeric
df_q4['OBS_VALUE'] = pd.to_numeric(df_q4['OBS_VALUE'], errors='coerce')

# -----------------------------
# Plot choropleth
# -----------------------------
fig = px.choropleth(
    df,
    locations="REF_AREA",
    color="OBS_VALUE",
    hover_name="REF_AREA_LABEL",
    animation_frame="TIME_PERIOD",   # slider by quarter
    color_continuous_scale="Viridis",
    title="House Price-to-Income Ratio Over Time",
    labels={'OBS_VALUE':'House Price-to-Income Ratio'},
    locationmode="ISO-3"
)

fig.update_layout(
    height=600
)

fig.show()

