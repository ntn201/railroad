import requests
import json
from .train_requests import get_train
from .seat_requests import get_all_seat

ticket_fields = ['id', 'customer_name', 'customer_id', 'customer_phone', 'departing_station', 'destination', 'train_id', 'ticket_type', 'seat_number', 'price', 'bought_at']

# Local server
# url = "http://127.0.0.1:8000/api/"

#Heroku server
url = "https://usth-railroad.herokuapp.com/api/"


# Basic requests
def get_all_ticket():
    get_all_tickets = requests.get(url=url + "ticket/")
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
    get_ticket_by_id = requests.get(url=url + f"ticket/{id}/")
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
    "customer_name": "Vinh",
    "customer_id": "1234567890",
    "customer_phone": "12346",
    "ticket_type": "Return-trip",                   # Return-trip or One-way 
    "train_id": 1,                                  # Train id
    "departing_id": 1,                              # Station id
    "destination_id": 2,                            # Station id
    "seat_number": [2]                              # Is an array of integer
}

ticket_update_form = {
    # "customer_name": "Vinh",                      # Optional
    # "customer_id": "1234567890",                  # Optional
    # "customer_phone": "12346",                    # Optional
    # "ticket_type": "Return-trip",                 # Optional
    "train_id": 1,                                  
    # "departing_id": 1,                            # Optional  
    # "destination_id": 2,                          # Optional 
    # "seat_number": 2                              # Optional 
}

def create_ticket(request):
    create_ticket = requests.post(url=url + "ticket/create/", json=request)
    print(create_ticket.text)
    return create_ticket.text

def update_ticket(request, id):
    ticket = get_ticket(id)
    seat_change = get_ticket(id).get('seat_number')
    seats = get_all_seat()
    for seat in seats:
        if seat.seat_number == seat_change and seat.train_name == get_train(ticket.get("train_id")).get("train_name"):
            seat.is_taken = False
            seat.save()

    update_ticket = requests.put(url=url + f"ticket/{id}/", json=request)
    return update_ticket.text

def delete_ticket(id):
    delete_ticket = requests.delete(url=url + f"ticket/{id}/")
    return f"Ticket id {id} is deleted"

# Custom requests
def get_all_ticket_info():
    get_all_tickets = requests.get(url=url + "ticket/")
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
    get_ticket_by_id = requests.get(url=url + f"ticket/{id}/")
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

def get_ticket_by_phone(customer_phone):
    get_all_tickets = requests.get(url=url + "ticket/")
    all_tickets = json.loads(get_all_tickets.text)
    found_ticket = []
    for ticket in all_tickets:
        if ticket.get("customer_phone") == customer_phone:
            ticket_info = {
                "customer_name": ticket.get("customer_name"),
                "customer_id": ticket.get("customer_id"),
                "customer_phone": ticket.get("customer_phone"),
                "price": ticket.get("price"),
                "train_name": get_train(ticket.get("train_id")).get("train_name"),
                "seat_number": ticket.get("seat_number")
            }
            found_ticket.append(ticket_info)
            
    return found_ticket
    

# print(get_all_ticket())