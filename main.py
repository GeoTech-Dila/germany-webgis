from fastapi import FastAPI
from sqlalchemy import create_engine, text
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine("postgresql://postgres:1234@localhost:5432/germany_gis")


# 🌍 1. HARİTA VERİSİ
@app.get("/states")
def get_states():
    query = text("""
    SELECT name, ST_AsGeoJSON(ST_Transform(geometry, 4326)) as geom
    FROM germany_states;
    """)

    with engine.connect() as conn:
        result = conn.execute(query)

        features = []

        for row in result:
            features.append({
                "type": "Feature",
                "geometry": json.loads(row.geom),
                "properties": {
                    "name": row.name
                }
            })

    return {"type": "FeatureCollection", "features": features}


# 📋 2. DASHBOARD LİSTESİ 👇 BURAYA EKLE
@app.get("/states_list")
def states_list():
    query = text("""
    SELECT name
    FROM germany_states
    ORDER BY name;
    """)

    with engine.connect() as conn:
        result = conn.execute(query)
        return [row.name for row in result]
