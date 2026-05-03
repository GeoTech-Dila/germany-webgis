import geopandas as gpd

gdf = gpd.read_file("ALmanya_eyaletler.shp")

gdf = gdf.to_crs(epsg=3035)

gdf["area_ha"] = gdf.geometry.area / 10000

gdf = gdf.to_crs(epsg=4326)

gdf.to_file("states.geojson", driver="GeoJSON")

print(gdf.columns)  # 👈 kontrol için