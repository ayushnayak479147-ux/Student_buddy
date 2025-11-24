from dataclasses import dataclass
from datetime import date

@dataclass
class Note:
    note_id: int
    title: str
    description: str
    due_date: str  # "YYYY-MM-DD"
    tag: str       # e.g. "exam", "assignment"
    status: str    # "pending" or "done"

@dataclass
class TimetableEntry:
    entry_id: int
    course_name: str
    day: str        # e.g. "Mon"
    start_time: str # "09:00"
    end_time: str   # "10:00"
    venue: str

@dataclass
class Contact:
    contact_id: int
    name: str
    role: str       # "mentor", "faculty", "CR"
    phone: str
    email: str