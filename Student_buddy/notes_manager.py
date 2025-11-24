from datetime import datetime
import storage

def list_notes():
    data = storage.load_all()
    notes = data["notes"]
    if not notes:
        print("No notes/tasks found.")
        return
    print("\n--- Notes / Tasks ---")
    for n in notes:
        print(f"{n['note_id']}. {n['title']} [{n['status']}] - due {n['due_date']} ({n['tag']})")

def add_note():
    data = storage.load_all()
    notes = data["notes"]

    title = input("Title: ").strip()
    desc = input("Description: ").strip()
    due_date = input("Due date (YYYY-MM-DD): ").strip()
    tag = input("Tag (exam/assignment/personal): ").strip() or "general"

    # simple validation
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Note not added.")
        return

    note_id = storage.get_next_id(notes, "note_id")
    note = {
        "note_id": note_id,
        "title": title,
        "description": desc,
        "due_date": due_date,
        "tag": tag,
        "status": "pending"
    }
    notes.append(note)
    data["notes"] = notes
    storage.save_all(data)
    print("Note/task added.")

def mark_note_done():
    data = storage.load_all()
    notes = data["notes"]
    if not notes:
        print("No notes to update.")
        return
    note_id = int(input("Enter note id to mark as done: "))
    for n in notes:
        if n["note_id"] == note_id:
            n["status"] = "done"
            storage.save_all(data)
            print("Note marked as done.")
            return
    print("Note id not found.")

def delete_note():
    data = storage.load_all()
    notes = data["notes"]
    if not notes:
        print("No notes to delete.")
        return
    note_id = int(input("Enter note id to delete: "))
    new_notes = [n for n in notes if n["note_id"] != note_id]
    if len(new_notes) == len(notes):
        print("Note id not found.")
        return
    data["notes"] = new_notes
    storage.save_all(data)
    print("Note deleted.")