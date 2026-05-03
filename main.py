from fastapi import FastAPI
import json

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # herkes erişebilir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"status": "API çalışıyor"}

@app.get("/states")
def get_states():
    with open("states.geojson", "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/states_list")
def states_list():
    with open("states.geojson", "r", encoding="utf-8") as f:
        data = json.load(f)
        return [f["properties"]["name"] for f in data["features"]]
