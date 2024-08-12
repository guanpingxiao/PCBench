import pandas as pd
us_cities = pd.read_csv('us-cities-top-1k.csv')
us_cities = us_cities.query("State in ['New York', 'Ohio']")
import plotly.express as px
fig = px.line_mapbox(us_cities, lat='lat', lon='lon', color='State')
