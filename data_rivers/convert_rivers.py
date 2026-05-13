import geopandas as gpd

# ANA NEHIRLER
gdf1 = gpd.read_file("ALmanya_nehirler.shp")

gdf1.to_file(
    "ALmanya_nehirler.geojson",
    driver="GeoJSON"
)

print("✅ Ana nehirler hazır")


# YAN KOLLAR
gdf2 = gpd.read_file("ALmanya_nehirlerson.shp")

gdf2.to_file(
    "ALmanya_nehirlerson.geojson",
    driver="GeoJSON"
)

print("✅ Yan kollar hazır")