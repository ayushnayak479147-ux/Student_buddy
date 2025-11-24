import json
import os

DATA_FILE = "campus_companion_data.json"

def _init_file():
    if not os.path.exists(DATA_FILE):
        empty = {"notes": [], "timetable": [], "contacts": []}
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(empty, f, indent=2)

def load_all():
    _init_file()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_all(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_next_id(items, key_name):
    if not items:
        return 1
    return max(item[key_name] for item in items) + 1