import geopandas as geo
import pandas as pd
import folium as fol

# Lecture d'un fichier shapefile

shapefile = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
shapefile= shapefile.sort_values(['location', 'date'], ascending=[True, False])
shapefile= shapefile.drop_duplicates(subset='location', keep='first')

map = fol.Map(tiles='cartodbpositron', zoom_start=2)

for index, row in shapefile.iterrows():
    if not shapefile.isna(row['continent']):
        fol.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['location'] + ': ' + str(row['total_cases']),
            icon=fol.Icon(color='red', icon='info-sign')
        ).add_to(map)


map
