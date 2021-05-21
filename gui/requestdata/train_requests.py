import requests
import json

from schedule_requests import get_schedule

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

train_form = {   
    "route_id": "1",                                    #Reference Route
    "train_name": "HN-SG",
    "departing_time": "2021-5-21 17:00:00",
    "number_of_seats": 56
}

def create_train(request):
    create_train = requests.post(url="http://127.0.0.1:8000/train/create/", json=request)
    return create_train.status_code

get_route(get_train(6).get("route_id"))

print()