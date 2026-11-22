
import json
import os

DATABASE_FILE = "database.json"


def load_database():

    # Check whether database exists
    if not os.path.exists(DATABASE_FILE):
        return {"files": []}

    # Check whether database is empty
    if os.path.getsize(DATABASE_FILE) == 0:
        return {"files": []}

    # Load database contents
    try:
        with open(DATABASE_FILE, "r") as file:
            database = json.load(file)

        # Validate database structure
        if not isinstance(database, dict):
            raise ValueError("Invalid database structure")

        if not isinstance(database.get("files"), list):
            raise ValueError("Missing or invalid files list")

        return database

    except json.JSONDecodeError:
        print("Warning: Database contains invalid JSON.")
        return {"files": []}


def save_database(database):

    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file, indent=4)
