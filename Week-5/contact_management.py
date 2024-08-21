import pickle

def read_contacts(filename):
    """Read contacts from a text file."""
    contacts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                contacts.append(line.strip())
    except FileNotFoundError:
        print(f"File {filename} not found. No contacts to display.")
    return contacts

def write_contacts(filename, contacts):
    """Write contacts to a text file."""
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(contact + '\n')

def save_contacts_binary(filename, contacts):
    """Save contacts in a binary file."""
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)

def load_contacts_binary(filename):
    """Load contacts from a binary file."""
    try:
        with open(filename, 'rb') as file:
            contacts = pickle.load(file)
    except (FileNotFoundError, EOFError):
        contacts = []
    return contacts

def add_contact(filename, binary_filename, contact):
    """Add a new contact to both the text and binary files."""
    contacts = read_contacts(filename)
    contacts.append(contact)
    write_contacts(filename, contacts)
    
    contacts_binary = load_contacts_binary(binary_filename)
    contacts_binary.append(contact)
    save_contacts_binary(binary_filename, contacts_binary)

def remove_contact(filename, binary_filename, contact):
    """Remove a contact from both the text and binary files."""
    contacts = read_contacts(filename)
    if contact in contacts:
        contacts.remove(contact)
        write_contacts(filename, contacts)
    else:
        print(f"Contact {contact} not found in text file.")

    contacts_binary = load_contacts_binary(binary_filename)
    if contact in contacts_binary:
        contacts_binary.remove(contact)
        save_contacts_binary(binary_filename, contacts_binary)
    else:
        print(f"Contact {contact} not found in binary file.")

def display_contacts(filename):
    """Display all contacts stored in the text file."""
    contacts = read_contacts(filename)
    if contacts:
        print("\nContacts (Text File):")
        for contact in contacts:
            print(contact)
    else:
        print("No contacts available in text file.")

def display_contacts_binary(filename):
    """Display all contacts stored in the binary file."""
    contacts = load_contacts_binary(filename)
    if contacts:
        print("\nContacts (Binary File):")
        for contact in contacts:
            print(contact)
    else:
        print("No contacts available in binary file.")

def main():
    text_file = 'contacts.txt'
    binary_file = 'contacts.dat'

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts (Text File)")
        print("4. Display Contacts (Binary File)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            contact = input("Enter contact to add: ")
            add_contact(text_file, binary_file, contact)
        elif choice == '2':
            contact = input("Enter contact to remove: ")
            remove_contact(text_file, binary_file, contact)
        elif choice == '3':
            display_contacts(text_file)
        elif choice == '4':
            display_contacts_binary(binary_file)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
