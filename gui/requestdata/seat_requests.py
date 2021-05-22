import requests
import json


seat_fields = ['id', 'train_id', 'seat_number', 'is_taken']
seat_url = "http://127.0.0.1:8000/seat/"


# Basic requests
def get_all_seat():
    get_all_seats = requests.get(url="http://127.0.0.1:8000/seat/")
    all_seats = json.loads(get_all_seats.text)
    seats = []
    for seat in all_seats:
        seat = {
            'id': seat.get('id'), 
            'train_id': seat.get('train_id'), 
            'seat_number': seat.get('seat_number'), 
            'is_taken': seat.get('is_taken')
        }
    return seats

def get_seat(id):
    get_seat_by_id = requests.get(url=f"http://127.0.0.1:8000/seat/{id}/")
    seat = json.loads(get_seat_by_id.text)
    seat = {
            'id': seat.get('id'), 
            'train_id': seat.get('train_id'), 
            'seat_number': seat.get('seat_number'), 
            'is_taken': seat.get('is_taken')
        }
    return seat


# Custom requests
def get_seats_of_train(train_id):
    all_seats = requests.get(url="http://127.0.0.1:8000/seat/")
    all_seats = json.loads(all_seats.text)
    taken_seats = []
    for seat in all_seats:
        if seat.get("train_id") == train_id:
            if seat.get("is_taken"):
                taken_seats.append(seat.get('seat_number'))
    return taken_seats    
    