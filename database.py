import json

DB_FILE = "data.json"

def load_data():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {"bookings": {}}

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_booking(day, hour, user_id, username):
    data = load_data()
    if day not in data["bookings"]:
        data["bookings"][day] = {}
    data["bookings"][day][hour] = {
        "user_id": user_id,
        "username": username
    }
    save_data(data)

def get_bookings(day):
    data = load_data()
    return data["bookings"].get(day, {})
