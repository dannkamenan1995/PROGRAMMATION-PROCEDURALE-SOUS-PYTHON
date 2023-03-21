import pandas
import geopandas as gpd
import folium as fol
import fiona as fi

shapefile = gpd.read_file('map.shp', encoding='utf-8')
shapefile