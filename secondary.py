import pandas as pd
import requests

# Fetch the data.
df = pd.read_csv("https://ourworldindata.org/grapher/number-calorie-diet-unaffordable.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})

# Fetch the metadata
metadata = requests.get("https://ourworldindata.org/grapher/number-calorie-diet-unaffordable.metadata.json?v=1&csvType=full&useColumnShortNames=true").json()
