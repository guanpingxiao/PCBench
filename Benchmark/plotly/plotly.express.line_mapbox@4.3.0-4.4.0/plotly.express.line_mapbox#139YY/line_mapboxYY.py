import pandas as pd
us_cities = pd.read_csv('us-cities-top-1k.csv')
us_cities = us_cities.query("State in ['New York', 'Ohio']")
import plotly.express as px
fig = px.line_mapbox(us_cities,  'lat',  'lon',  'State',  None,  None,  None,  None, line_group=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, zoom=8)
