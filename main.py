from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typeID import TypeID

from stationID import StationID

from stationsID import StationsID


app = FastAPI()

origins = [
    "http://192.168.1.2"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

id_request = TypeID()

station_name_request = StationID()

@app.get("/itemID/{item_name}")
async def get_iteme_id(item_name: str):
    item_id = id_request.getID(item_name)
    return {"typeID": item_id}

@app.get("/stationID/{station_id}")
async def get_station_name(station_id: str):
    station_name = station_name_request.getID(station_id)
    return {"stationName": station_name}
