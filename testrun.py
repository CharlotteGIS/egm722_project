import folium

m = folium.Map()

import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

import matplotlib.patches as mpatches
import pandas as pd
import geopandas as gpd
import pyproj

from shapely.geometry import Point, LineString, Polygon
# ---------------------------------------------------------------------------------------------------------------------
# in this section, write the script to load the data and complete the main part of the analysis.
# try to print the results to the screen using the format method demonstrated in the workbook

# load the necessary data here and transform to a UTM projection
roads = gpd.read_file('C:/Users/charl/OneDrive/Desktop/ulster/EGM722_programming/git/egm722/Week3/data_files/NI_roads.shp')


print(roads.head())
print(roads.crs)

# your analysis goes here...
print(roads.crs.to_json()) # show the representation of the CRS in JSON format

# ---------------------------------------------------------------------------------------------------------------------
# below here, you may need to modify the script somewhat to create your map.
# create a crs using ccrs.UTM() that corresponds to our CRS
roads_itm = roads.to_crs(epsg=2157) # replace XX with the correct EPSG code for Irish Transverse Mercator

print(roads_itm.head())
print(roads_itm.crs)