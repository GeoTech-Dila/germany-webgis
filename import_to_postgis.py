import geopandas as gpd
from sqlalchemy import create_engine

# shapefile oku
gdf = gpd.read_file("ALmanya_eyaletler.shp")

print(gdf.columns)  # kolonları görelim

# PostGIS bağlantısı
engine = create_engine("postgresql://postgres:1234@localhost:5432/germany_gis")

# veriyi gönder
gdf.to_postgis(
    "germany_states",
    engine,
    if_exists="replace",
    index=False
)

print("✅ PostGIS'e aktarıldı")