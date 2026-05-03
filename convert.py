import geopandas as gpd

gdf = gpd.read_file("ALmanya_eyaletler.shp")
gdf.to_file("states.geojson", driver="GeoJSON")

print("Bitti")