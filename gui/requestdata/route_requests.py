import requests
import json


route_fields = ['id', 'route_name']
route_url = "http://127.0.0.1:8000/route/"

def get_all_route():
    get_all_routes = requests.get(url="http://127.0.0.1:8000/route/")
    all_routes = json.loads(get_all_routes.text)
    return all_routes

def get_route(id):
    get_route_by_id = requests.get(url=f"http://127.0.0.1:8000/route/{id}/")
    route = json.loads(get_route_by_id.text)
    return route

print(get_route(1))