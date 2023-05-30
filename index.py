import os
import getpass
from cryptography.fernet import Fernet

# Set up encryption key
key = Fernet.generate_key()
fernet = Fernet(key)

# Define file directory and name
directory = "notes"
if not os.path.exists(directory):
    os.makedirs(directory)

# Functions for adding, editing, viewing, and deleting notes
def add_note():
    subject = input("Enter note subject: ")
    note = input("Enter note text: ")
    filename = os.path.join(directory, subject + ".txt")
    with open(filename, "w") as f:
        encrypted_note = fernet.encrypt(note.encode())
        f.write(encrypted_note.decode())
    print("Note added.")

def edit_note():
    subject = input("Enter note subject: ")
    filename = os.path.join(directory, subject + ".txt")
    if not os.path.exists(filename):
        print("Note does not exist.")
        return
    with open(filename, "r") as f:
        encrypted_note = f.read()
        note = fernet.decrypt(encrypted_note.encode()).decode()
    print("Current note text:")
    print(note)
    new_note = input("Enter new note text: ")
    with open(filename, "w") as f:
        encrypted_note = fernet.encrypt(new_note.encode())
        f.write(encrypted_note.decode())
    print("Note edited.")

def view_note():
    subject = input("Enter note subject: ")
    filename = os.path.join(directory, subject + ".txt")
    if not os.path.exists(filename):
        print("Note does not exist.")
        return
    with open(filename, "r") as f:
        encrypted_note = f.read()
        note = fernet.decrypt(encrypted_note.encode()).decode()
    print("Note text:")
    print(note)

def delete_note():
    subject = input("Enter note subject: ")
    filename = os.path.join(directory, subject + ".txt")
    if not os.path.exists(filename):
        print("Note does not exist.")
        return
    os.remove(filename)
    print("Note deleted.")

# Function for prompting user for password and verifying
def check_password():
    password = getpass.getpass("Enter password to access notes: ")
    if password == "1447":
        return True
    else:
        print("Incorrect password.")
        return False

# Main loop for running notes application
while True:
    if check_password():
        print("1. Add note")
        print("2. Edit note")
        print("3. View note")
        print("4. Delete note")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            view_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
