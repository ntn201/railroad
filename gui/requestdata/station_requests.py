import requests
import json


station_fields = ['id', 'station_name', 'station_distance']

# Local server
url = "http://127.0.0.1:8000/api/"

#Heroku server
# url = "https://usth-railroad.herokuapp.com/api/"

# Basic requests
def get_all_station():
    get_all_stations = requests.get(url=url+"station/")
    all_stations = json.loads(get_all_stations.text)
    stations = []
    for station in all_stations:
        station = {
            'id': station.get('id'), 
            'station_name': station.get('station_name'), 
        }
        stations.append(station)
    return stations

def get_station(id):
    get_station_by_id = requests.get(url=url + f"station/station/{id}/")
    station = json.loads(get_station_by_id.text)
    station = {
            'id': station.get('id'), 
            'station_name': station.get('station_name'), 
        }
    return station

station_form = {
    'station_name': 'Ha Noi',
}

def create_station(request):
    create_station = requests.post(url=url + "station/", json=request)
    print(url + "/station?")
    return create_station.text

def update_station(request, id):
    update_station = requests.put(url=url + f"station/{id}/", json=request)
    return update_station.text

def delete_station(id):
    delete_station = requests.delete(url=url + f"station/{id}/")
    return f"station id {id} is deleted"

# Custom requests

# print(get_all_station())