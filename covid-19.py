import pandas as pd
import folium as fol

# Lecture d'un fichier CSV
data = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

# Tri des données et conservation de la première occurrence de chaque pays
data = data.sort_values(['location', 'date'], ascending=[True, False])
data = data.drop_duplicates(subset='location', keep='first')

# Création d'une carte
m = fol.Map(tiles='cartodbpositron', zoom_start=2)

# Ajout de marqueurs pour chaque pays avec des données continentales non nulles
for index, row in data.iterrows():
    if not pd.isna(row['continent']):
        # Différenciation des marqueurs en fonction du nombre de cas
        if row['total_cases'] > 5000000:
            color = 'red'
        elif row['total_cases'] > 1000000:
            color = 'orange'
        elif row['total_cases'] > 100000:
            color = 'yellow'
        else:
            color = 'green'
        # Ajout d'un marqueur avec un popup
        fol.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['location'] + ': ' + str(row['total_cases']),
            icon=fol.Icon(color=color, icon='info-sign')
        ).add_to(m)

# Ajout d'une légende avec une échelle de couleurs
colors = ['green', 'yellow', 'orange', 'red']
labels = ['<100k', '100k-1M', '1M-5M', '>5M']
for i in range(len(colors)):
    fol.Marker(
        location=[0, 0],
        icon=fol.Icon(color=colors[i])
    ).add_to(m)
    fol.Marker(
        location=[-5, 0],
        icon=fol.DivIcon(html='<span style="font-size: 14px; color: black;">' + labels[i] + '</span>')
    ).add_to(m)

# Affichage de la carte
m