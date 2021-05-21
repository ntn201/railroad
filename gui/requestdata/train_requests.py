import requests
import json
from datetime import datetime

from route_requests import get_route
from seat_requests import get_seats_of_train

train_fields = ['id', 'train_name', 'train_distance']
train_url = "http://127.0.0.1:8000/train/"

def get_all_train():
    get_all_trains = requests.get(url="http://127.0.0.1:8000/train/")
    all_trains = json.loads(get_all_trains.text)
    return all_trains

def get_train(id):
    get_train_by_id = requests.get(url=f"http://127.0.0.1:8000/train/{id}/")
    train = json.loads(get_train_by_id.text)
    return train

def get_train_info(id):
    get_train_by_id = requests.get(url=f"http://127.0.0.1:8000/train/{id}/")
    train = json.loads(get_train_by_id.text) 
    train_info = {
        "train_name": train.get("train_name"),
        "route_name": get_route(train.get("route_id")),
        "departing_time": train.get("departing_time"),
        "number_of_seats": train.get("number_of_seats"),
        "taken_seats": get_seats_of_train(id)
    }
    return train_info

train_form = {   
    "route_id": "1",                                   #Reference Route
    "train_name": "HN-SG",
    "departing_time": "2021-5-21 17:00:00",
    "number_of_seats": 56
}

def create_train(request):
    create_train = requests.post(url="http://127.0.0.1:8000/train/create/", json=request)
    return create_train.status_code

print(get_train_info(1))