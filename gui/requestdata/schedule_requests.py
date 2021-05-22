import requests
import json


schedule_fields = ['id', 'route_id', 'station_id', 'arrive_order', 'travel_time']
schedule_url = "http://127.0.0.1:8000/schedule/"


# Basic requests
def get_all_schedule():
    get_all_schedules = requests.get(url="http://127.0.0.1:8000/schedule/")
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
    get_schedule_by_id = requests.get(url=f"http://127.0.0.1:8000/schedule/{id}/")
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
