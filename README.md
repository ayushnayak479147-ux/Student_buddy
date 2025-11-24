# Student_buddy
**Overview**
Campus Companion is a simple Python console application designed for first-year engineering students to manage their study-related tasks efficiently. The app centralizes notes/tasks, timetable entries, and important contact information in one easy-to-use tool. It helps students organize their daily academic activities, avoid missed deadlines, and easily access key contacts like mentors or class representatives.

**Features**
- **Notes & Tasks:** Add, list, mark as done, and delete study notes or tasks with due dates and tags (exam, assignment, personal).
- **Timetable Management:** Add, view full timetable, view today’s classes/events, and delete timetable entries.
- **Contacts Directory:** Add, list, search, and delete contacts such as mentors, faculty, and peers.
- Data persistence through JSON storage ensures information is saved between sessions.
- Clear console menu interface for straightforward interaction.

**Technologies Used**
- Python 3.x
- JSON file handling for data persistence
- Built-in Python modules such as `dataclasses` and `datetime`
- Console input/output for user interaction

**Installation and Running the Project**
1. Clone or download the project files into a single directory.  
2. Ensure Python 3.x is installed on your system.  
3. Run the application from the command line:
python main.py
text
4. Follow the on-screen menu prompts to use the Notes, Timetable, and Contacts modules.

**Instructions for Testing**
- Use the menu options to add sample notes, timetable entries, and contacts.  
- Confirm the items appear correctly when listed.  
- Test marking tasks as done and deleting items to verify data updates properly.  
- Exit and restart the program to verify data persistence.

**Project Structure**
- `main.py` – Application entry point and UI menus  
- `models.py` – Data classes for Notes, TimetableEntry, and Contact  
- `storage.py` – JSON file operations for loading and saving data  
- `notes_manager.py` – Functionalities related to notes/tasks  
- `timetable_manager.py` – Functionalities related to timetable entries  
- `contacts_manager.py` – Functionalities related to contacts  

**Acknowledgments**
I am Ayush Nayak of Batch25,I have created an app which will help students not only from VIT but from all around the world 
Name-Ayush Nayak
REG NO- 25BAI11591

---
