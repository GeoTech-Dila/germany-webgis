import geopandas as gpd

gdf = gpd.read_file("data_airport2/ALmanya_airports.shp")

# koordinat sistemini düzelt (çok önemli)
gdf = gdf.to_crs(epsg=4326)

# GeoJSON olarak kaydet
gdf.to_file("data_airport2/ALmanya_airports.geojson", driver="GeoJSON")

print("Dönüştürüldü ✅")