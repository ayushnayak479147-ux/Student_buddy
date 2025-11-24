import notes_manager
import timetable_manager
import contacts_manager

def notes_menu():
    while True:
        print("\n--- Notes / Tasks Menu ---")
        print("1. List notes")
        print("2. Add note")
        print("3. Mark note as done")
        print("4. Delete note")
        print("0. Back to main menu")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            notes_manager.list_notes()
        elif choice == "2":
            notes_manager.add_note()
        elif choice == "3":
            notes_manager.mark_note_done()
        elif choice == "4":
            notes_manager.delete_note()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

def timetable_menu():
    while True:
        print("\n--- Timetable Menu ---")
        print("1. List full timetable")
        print("2. Add timetable entry")
        print("3. View today's timetable")
        print("4. Delete timetable entry")
        print("0. Back to main menu")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            timetable_manager.list_timetable()
        elif choice == "2":
            timetable_manager.add_timetable_entry()
        elif choice == "3":
            timetable_manager.view_today_timetable()
        elif choice == "4":
            timetable_manager.delete_timetable_entry()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

def contacts_menu():
    while True:
        print("\n--- Contacts Menu ---")
        print("1. List contacts")
        print("2. Add contact")
        print("3. Search contacts")
        print("4. Delete contact")
        print("0. Back to main menu")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            contacts_manager.list_contacts()
        elif choice == "2":
            contacts_manager.add_contact()
        elif choice == "3":
            contacts_manager.search_contacts()
        elif choice == "4":
            contacts_manager.delete_contact()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

def main():
    while True:
        print("\n==== Campus Companion ====")
        print("1. Notes / Tasks")
        print("2. Timetable")
        print("3. Contacts")
        print("0. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            notes_menu()
        elif choice == "2":
            timetable_menu()
        elif choice == "3":
            contacts_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
