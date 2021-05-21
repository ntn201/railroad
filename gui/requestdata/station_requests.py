import requests
import json


station_fields = ['id', 'station_name', 'station_distance']
station_url = "http://127.0.0.1:8000/station/"

def get_all_station():
    get_all_stations = requests.get(url="http://127.0.0.1:8000/station/")
    all_stations = json.loads(get_all_stations.text)
    return all_stations

def get_station(id):
    get_station_by_id = requests.get(url=f"http://127.0.0.1:8000/station/{id}/")
    station = json.loads(get_station_by_id.text)
    return station
