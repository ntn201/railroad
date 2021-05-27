import requests
import json


route_fields = ['id', 'route_name']

# Local server
# url = "http://127.0.0.1:8000/api/"

#Heroku server
url = "https://usth-railroad.herokuapp.com/api/"


#Basic requests
def get_all_route():
    get_all_routes = requests.get(url=url + "route/")
    all_routes = json.loads(get_all_routes.text)
    routes = []
    for route in all_routes:
        route = {
            'id': route.get('id'), 
            'route_name': route.get('route_name')
        }
        routes.append(route)
    return routes

def get_route(id):
    get_route_by_id = requests.get(url=url + f"route/{id}/")
    route = json.loads(get_route_by_id.text)
    route = {
            'id': route.get('id'), 
            'route_name': route.get('route_name')
        }
    return route.get("route_name")

# Custom requests
def get_all_route_name():
    get_all_routes = requests.get(url=url + "route/")
    all_routes = json.loads(get_all_routes.text)
    routes = []
    for route in all_routes:
        routes.append(route.get("route_name"))
    return routes    
    