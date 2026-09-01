import json
import os

from subjects import subjects

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(BASE_DIR, "users.json")
USERS_FOLDER = os.path.join(BASE_DIR, "users")


def create_user():
    username = input("Create username: ")
    password = input("Create password: ")

    try:
        with open(USERS_FILE, "r") as file:
            users = json.load(file)

    except FileNotFoundError:
        users = {}

    if username in users:
        print("Username already exists.")
        return None

    users[username] = password

    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

    save_progress(subjects, username)

    print("User created.")
    return username


def login():
    try:
        with open(USERS_FILE, "r") as file:
            users = json.load(file)

    except FileNotFoundError:
        print("\nNo users have been created.")
        return None

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == password:
            print(f"Welcome, {username}!")
            return username

        print("\nIncorrect username or password.")

        choice = input(
            "Press Enter to try again, or enter 0 to go back: "
        ).strip()

        if choice == "0":
            return None


def get_user():
    while True:
        print("\n===== STUDENT PROGRESS TRACKER =====")
        print("1. Login")
        print("2. Create Account")
        print("0. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            username = login()

            if username is not None:
                return username

        elif choice == "2":
            username = create_user()

            if username is not None:
                return username

        elif choice == "0":
            return None

        else:
            print("Invalid option.")


def load_progress(username):
    filename = os.path.join(USERS_FOLDER, f"{username}.json")

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Progress file not found.")
        return None


def save_progress(subjects, username):
    os.makedirs(USERS_FOLDER, exist_ok=True)

    filename = os.path.join(USERS_FOLDER, f"{username}.json")

    with open(filename, "w") as file:
        json.dump(subjects, file, indent=4)
