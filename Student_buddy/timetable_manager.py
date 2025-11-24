import storage

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def list_timetable():
    data = storage.load_all()
    entries = data["timetable"]
    if not entries:
        print("No timetable entries.")
        return
    print("\n--- Timetable ---")
    for e in entries:
        print(f"{e['entry_id']}. {e['course_name']} {e['day']} {e['start_time']}-{e['end_time']} @ {e['venue']}")

def add_timetable_entry():
    data = storage.load_all()
    entries = data["timetable"]

    course = input("Course name: ").strip()
    day = input("Day (Mon/Tue/...): ").strip()
    if day not in DAYS:
        print("Invalid day. Entry not added.")
        return
    start_time = input("Start time (HH:MM): ").strip()
    end_time = input("End time (HH:MM): ").strip()
    venue = input("Venue: ").strip()

    entry_id = storage.get_next_id(entries, "entry_id")
    entry = {
        "entry_id": entry_id,
        "course_name": course,
        "day": day,
        "start_time": start_time,
        "end_time": end_time,
        "venue": venue
    }
    entries.append(entry)
    data["timetable"] = entries
    storage.save_all(data)
    print("Timetable entry added.")

def view_today_timetable():
    from datetime import datetime
    data = storage.load_all()
    entries = data["timetable"]
    if not entries:
        print("No timetable entries.")
        return
    day_index = datetime.today().weekday()  # 0=Mon
    today_day = DAYS[day_index]
    today_entries = [e for e in entries if e["day"] == today_day]
    if not today_entries:
        print(f"No entries for today ({today_day}).")
        return
    print(f"\n--- Today's Timetable ({today_day}) ---")
    for e in today_entries:
        print(f"{e['course_name']} {e['start_time']}-{e['end_time']} @ {e['venue']}")

def delete_timetable_entry():
    data = storage.load_all()
    entries = data["timetable"]
    if not entries:
        print("No entries to delete.")
        return
    entry_id = int(input("Enter entry id to delete: "))
    new_entries = [e for e in entries if e["entry_id"] != entry_id]
    if len(new_entries) == len(entries):
        print("Entry id not found.")
        return
    data["timetable"] = new_entries
    storage.save_all(data)
    print("Timetable entry deleted.")