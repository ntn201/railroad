import requests
import json
from datetime import datetime

from route_requests import get_route
from seat_requests import get_seats_of_train

train_fields = ['id', 'train_name', 'route_id', 'departing_time', 'number_of_seats']

# Local server
train_url = "http://127.0.0.1:8000/api/"

#Heroku server
# train_url = "https://usth-railroad.herokuapp.com/api/"


# Basic requests
def get_all_train():
    get_all_trains = requests.get(url=train_url + "train/")
    all_trains = json.loads(get_all_trains.text)
    trains = []
    for train in all_trains:
        train_fields = {
            'id': train.get('id'),
            'train_name': train.get('train_name'), 
            'route_id': train.get('route_id'), 
            'departing_time': train.get('departing_time'), 
            'number_of_seats': train.get('number_of_seats')
        }
        trains.append(train_fields)
    return trains

def get_train(id):
    get_train_by_id = requests.get(url=train_url + f"train/{id}/")
    train = json.loads(get_train_by_id.text)
    train = {
        'id': train.get('id'),
        'train_name': train.get('train_name'), 
        'route_id': train.get('route_id'), 
        'departing_time': train.get('departing_time'), 
        'number_of_seats': train.get('number_of_seats')
        }
    return train

train_form = {   
    "route_id": "1",                                   #Reference Route, use get_all_route
    "train_name": "HN-SG1",
    "departing_time": "2021-5-27 20:00:00",
    "number_of_seats": 56
}

def create_train(request):
    create_train = requests.post(url=train_url + "train/create/", json=request)
    return create_train.text
    
def update_train(request, id):
    update_train = requests.put(url=train_url + f"train/{id}/", json=request)
    return update_train.text

def delete_train(id):
    delete_train = requests.delete(url=train_url + f"train/{id}/")
    return f"train id {id} is deleted"


# Custom requests
def get_all_train_info():
    get_all_train = requests.get(url=train_url + "train/")
    all_train = json.loads(get_all_train.text)
    train_infos = []
    for train in all_train:
        train_info = {
            "train_name": train.get("train_name"),
            "route_name": get_route(train.get("route_id")),
            "departing_time": train.get("departing_time"),
            "number_of_seats": train.get("number_of_seats"),
            "taken_seats": get_seats_of_train(train.get("id"))
        }
        train_infos.append(train_info)
    return train_infos

def get_train_info(id):
    get_train_by_id = requests.get(url=train_url + f"train/{id}/")
    train = json.loads(get_train_by_id.text) 
    train_info = {
        "train_name": train.get("train_name"),
        "route_name": get_route(train.get("route_id")),
        "departing_time": train.get("departing_time"),
        "number_of_seats": train.get("number_of_seats"),
        "taken_seats": get_seats_of_train(train.get("id"))
    }
    return train_info

