import requests
import json


station_fields = ['id', 'station_name', 'station_distance']
station_url = "http://127.0.0.1:8000/station/"

# Basic requests
def get_all_station():
    get_all_stations = requests.get(url="http://127.0.0.1:8000/station/")
    all_stations = json.loads(get_all_stations.text)
    stations = []
    for station in all_stations:
        station = {
            'id': station.get('id'), 
            'station_name': station.get('station_name'), 
            'station_distance': station.get('station_distance')
        }
        stations.append(station)
    return stations

def get_station(id):
    get_station_by_id = requests.get(url=f"http://127.0.0.1:8000/station/{id}/")
    station = json.loads(get_station_by_id.text)
    station = {
            'id': station.get('id'), 
            'station_name': station.get('station_name'), 
            'station_distance': station.get('station_distance')
        }
    return station

station_form = {
    'station_name': 'Ha Noi 1',
    'station_distance': 0
}

def create_station(request):
    create_station = requests.post(url="http://127.0.0.1:8000/station/", json=request)
    return create_station.text

def update_station(request, id):
    update_station = requests.put(url=f"http://127.0.0.1:8000/station/{id}/", json=request)
    return update_station.text

def delete_station(id):
    delete_station = requests.delete(url=f"http://127.0.0.1:8000/station/{id}/")
    return f"station id {id} is deleted"

# Custom requests


print(get_all_station())
