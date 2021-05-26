import requests
import json


schedule_fields = ['id', 'route_id', 'station_id', 'arrive_order', 'travel_time']


# Local server
url = "http://127.0.0.1:8000/api/"

#Heroku server
# url = "https://usth-railroad.herokuapp.com/api/"


# Basic requests
def get_all_schedule():
    get_all_schedules = requests.get(url=url + "schedule/")
    all_schedules = json.loads(get_all_schedules.text)
    schedules = []
    for schedule in all_schedules:
        schedule = {
            'id': schedule.get('id'), 
            'route_id': schedule.get('route_id'), 
            'station_id': schedule.get('station_id'), 
            'arrive_order': schedule.get('arrive_order'), 
            'travel_time': schedule.get('travel_time')
        }
        schedules.append(schedule)
    return schedules

def get_schedule(id):
    get_schedule_by_id = requests.get(url=url + f"schedule/{id}/")
    schedule = json.loads(get_schedule_by_id.text)
    schedule = {
            'id': schedule.get('id'), 
            'route_id': schedule.get('route_id'), 
            'station_id': schedule.get('station_id'), 
            'arrive_order': schedule.get('arrive_order'), 
            'travel_time': schedule.get('travel_time')
        }
    return schedule

# Custom requests

# print(get_all_schedule())