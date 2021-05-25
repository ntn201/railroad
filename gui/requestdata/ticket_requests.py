import requests
import json
from train_requests import get_train

ticket_fields = ['id', 'customer_name', 'customer_id', 'customer_phone', 'departing_station', 'destination', 'train_id', 'ticket_type', 'seat_number', 'price', 'bought_at']
ticket_url = "http://127.0.0.1:8000/ticket/"


# Basic requests
def get_all_ticket():
    get_all_tickets = requests.get(url="http://127.0.0.1:8000/ticket/")
    all_tickets = json.loads(get_all_tickets.text)
    tickets = []
    for ticket in all_tickets:
        ticket_fields = {
            'id': ticket.get('id'), 
            'customer_name': ticket.get('customer_name'), 
            'customer_id': ticket.get('customer_id'), 
            'customer_phone': ticket.get('customer_phone'), 
            'departing_station': ticket.get('departing_station'), 
            'destination': ticket.get('destination'), 
            'train_id': ticket.get('train_id'), 
            'ticket_type': ticket.get('ticket_type'), 
            'seat_number': ticket.get('seat_number'), 
            'price': ticket.get('price'), 
            'bought_at': ticket.get('bought_at')
        }
        tickets.append(ticket_fields)
    return all_tickets

def get_ticket(id):
    get_ticket_by_id = requests.get(url=f"http://127.0.0.1:8000/ticket/{id}/")
    ticket = json.loads(get_ticket_by_id.text)
    ticket = {
            'id': ticket.get('id'), 
            'customer_name': ticket.get('customer_name'), 
            'customer_id': ticket.get('customer_id'), 
            'customer_phone': ticket.get('customer_phone'), 
            'departing_station': ticket.get('departing_station'), 
            'destination': ticket.get('destination'), 
            'train_id': ticket.get('train_id'), 
            'ticket_type': ticket.get('ticket_type'), 
            'seat_number': ticket.get('seat_number'), 
            'price': ticket.get('price'), 
            'bought_at': ticket.get('bought_at')
        }
    return ticket

ticket_form = {
    "customer_name": "Vinh Nguyen",
    "customer_id": "1234567890",
    "customer_phone": "12346",
    "ticket_type": "Return-trip",                   # Return-trip or One-way 
    "train_id": 1,                                  # Train id
    "departing_id": 1,                              # Station id
    "destination_id": 2,                            # Station id
    "seat_number": [1]                              # Is an array of integer
}

def create_ticket(request):
    create_ticket = requests.post(url="http://127.0.0.1:8000/ticket/create/", json=request)
    return create_ticket.text

def update_ticket(request, id):
    update_ticket = requests.put(url=f"http://127.0.0.1:8000/ticket/{id}/", json=request)
    return update_ticket.text

def delete_ticket(id):
    delete_ticket = requests.delete(url=f"http://127.0.0.1:8000/ticket/{id}/")
    return f"Ticket id {id} is deleted"

# Custom requests
def get_all_ticket_info():
    get_all_tickets = requests.get(url="http://127.0.0.1:8000/ticket/")
    all_tickets = json.loads(get_all_tickets.text)
    tickets = []
    for ticket in all_tickets:
        ticket = {
            "customer_name": ticket.get("customer_name"),
            "customer_id": ticket.get("customer_id"),
            "customer_phone": ticket.get("customer_phone"),
            "price": ticket.get("price"),
            "train_name": get_train(ticket.get("train_id")).get("train_name"),
            "seat_number": ticket.get("seat_number")
        }
        tickets.append(ticket)
    return tickets

def get_ticket_info(id):
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

