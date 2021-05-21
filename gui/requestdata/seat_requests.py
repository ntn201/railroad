import requests
import json


seat_fields = ['id', 'seat_name', 'seat_distance']
seat_url = "http://127.0.0.1:8000/seat/"

def get_all_seat():
    get_all_seats = requests.get(url="http://127.0.0.1:8000/seat/")
    all_seats = json.loads(get_all_seats.text)
    return all_seats

def get_seats_of_train(train_id):
    all_seats = requests.get(url="http://127.0.0.1:8000/seat/")
    all_seats = json.loads(all_seats.text)
    taken_seats = []
    for seat in all_seats:
        if seat.get("is_taken"):
            taken_seats.append(seat.get('seat_number'))
    return taken_seats

def get_seat(id):
    get_seat_by_id = requests.get(url=f"http://127.0.0.1:8000/seat/{id}/")
    seat = json.loads(get_seat_by_id.text)
    return seat

print(get_seats_of_train(1))