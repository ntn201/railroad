import requests
import json
from train_requests import get_train

ticket_fields = ['id', 'ticket_name', 'ticket_distance']
ticket_url = "http://127.0.0.1:8000/ticket/"

def get_all_ticket():
    get_all_tickets = requests.get(url="http://127.0.0.1:8000/ticket/")
    all_tickets = json.loads(get_all_tickets.text)
    return all_tickets

def get_ticket(id):
    get_ticket_by_id = requests.get(url=f"http://127.0.0.1:8000/ticket/{id}/")
    ticket = json.loads(get_ticket_by_id.text)
    ticket_info = {
        "customer_name": ticket.get("customer_name"),
        "customer_id": ticket.get("customer_id"),
        "customer_phone": ticket.get("customer_phone"),
        "price": ticket.get("price"),
        "train_name": get_train(ticket.get("train_id")).get("train_name"),
        "seat_number": ticket.get("seat_number")
    }
    return ticket_info


ticket_form = {
    "customer_name": "Vinh Nguyen",
    "customer_id": "0000000001",
    "customer_phone": "12346",
    "ticket_type": "Return-trip",                   # Return-trip or One-way 
    "train_name": "HN-SG1",     
    "starting_station": "Ha Noi",                   # Reference Station
    "destination": "Sai Gon",                       # Reference Station
    "seat_number": [10,11]                              # Is an array of integer
}

def create_ticket(request):
    create_ticket = requests.post(url="http://127.0.0.1:8000/ticket/create/", json=request)
    return create_ticket.text

print(get_ticket(4))