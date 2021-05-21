import requests
import json


schedule_fields = ['id', 'schedule_name']
schedule_url = "http://127.0.0.1:8000/schedule/"

def get_all_schedule():
    get_all_schedules = requests.get(url="http://127.0.0.1:8000/schedule/")
    all_schedules = json.loads(get_all_schedules.text)
    return all_schedules

def get_schedule(id):
    get_schedule_by_id = requests.get(url=f"http://127.0.0.1:8000/schedule/{id}/")
    schedule = json.loads(get_schedule_by_id.text)
    return schedule

print(get_schedule(1))