import storage

def list_contacts():
    data = storage.load_all()
    contacts = data["contacts"]
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contacts ---")
    for c in contacts:
        print(f"{c['contact_id']}. {c['name']} ({c['role']}) - {c['phone']} | {c['email']}")

def add_contact():
    data = storage.load_all()
    contacts = data["contacts"]

    name = input("Name: ").strip()
    role = input("Role (mentor/faculty/CR/other): ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    contact_id = storage.get_next_id(contacts, "contact_id")
    contact = {
        "contact_id": contact_id,
        "name": name,
        "role": role,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    data["contacts"] = contacts
    storage.save_all(data)
    print("Contact added.")

def search_contacts():
    data = storage.load_all()
    contacts = data["contacts"]
    if not contacts:
        print("No contacts to search.")
        return
    key = input("Search by name or role: ").strip().lower()
    results = [c for c in contacts if key in c["name"].lower() or key in c["role"].lower()]
    if not results:
        print("No matching contacts.")
        return
    print("\n--- Search Results ---")
    for c in results:
        print(f"{c['contact_id']}. {c['name']} ({c['role']}) - {c['phone']} | {c['email']}")

def delete_contact():
    data = storage.load_all()
    contacts = data["contacts"]
    if not contacts:
        print("No contacts to delete.")
        return
    contact_id = int(input("Enter contact id to delete: "))
    new_contacts = [c for c in contacts if c["contact_id"] != contact_id]
    if len(new_contacts) == len(contacts):
        print("Contact id not found.")
        return
    data["contacts"] = new_contacts
    storage.save_all(data)
    print("Contact deleted.")