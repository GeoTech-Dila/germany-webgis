import geopandas as gpd

# veriyi oku
gdf = gpd.read_file("ALmanya_eyaletler.shp")

# 🔥 doğru alan hesaplama için projeksiyon değiştir
gdf = gdf.to_crs(epsg=3035)

# alan hesapla (m²)
gdf["area_m2"] = gdf.geometry.area

# hektara çevir
gdf["area_ha"] = gdf["area_m2"] / 10000

# 🔥 tekrar 4326'ya dön (HARİTA İÇİN ŞART)
gdf = gdf.to_crs(epsg=4326)

# geojson olarak kaydet
gdf.to_file("states.geojson", driver="GeoJSON")

print("✅ GeoJSON hazır (alan dahil)")