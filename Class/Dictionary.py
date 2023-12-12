contacts = {}

def add_contact(name, phone):
    if name in contacts:
        print(f"Contact {name} already exists. Use 'update' to change the phone number.")
    else:
        contacts[name] = phone
        print(f"Contact {name} added!")

def get_phone(name):
    if name in contacts:
        print(f"The phone number for {name} is {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

def update_phone(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print(f"Phone number for {name} updated to {new_phone}")
    else:
        print(f"Contact {name} not found.")

def remove_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed.")
    else:
        print(f"Contact {name} not found.")

def display_contacts():
    print("Contact List:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

while True:
    command = input("What would you like to do? ('add', 'get', 'update', 'remove', 'display', 'quit') ").lower()

    if command == 'add':
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)

    elif command == 'get':
        name = input("Enter the name to retrieve the phone number: ")
        get_phone(name)

    elif command == 'update':
        name = input("Enter the name to update: ")
        new_phone = input("Enter the new phone number: ")
        update_phone(name, new_phone)

    elif command == 'remove':
        name = input("Enter the name to remove: ")
        remove_contact(name)

    elif command == 'display':
        display_contacts()

    elif command == 'quit':
        print("Goodbye!")
        break

    else:
        print("Invalid command. Please try again.")
