import os

from integrity import calculate_file_hash
from storage import load_database, save_database
from security import record_event, view_events, get_risk_level
from ai_analyzer import analyze_latest_event
def register_file():
    print("\n--- REGISTER A FILE ---")

    file_path = input("Enter file path: ").strip().strip('"')

    if not os.path.isfile(file_path):
        print("Error: File does not exist!")
        return

    file_path = os.path.abspath(file_path)

    database = load_database()

    for record in database["files"]:
        if record["path"] == file_path:
            print("This file is already registered!")
            return

    file_hash = calculate_file_hash(file_path)

    new_record = {
        "path": file_path,
        "sha256": file_hash,
        "status": "registered"
    }

    database["files"].append(new_record)

    save_database(database)

    print("\nFile registered successfully!")
    print("File:", file_path)
    print("SHA-256:", file_hash)


def verify_file():
    print("\n--- VERIFY FILE INTEGRITY ---")

    file_path = input("Enter registered file path: ").strip().strip('"')
    file_path = os.path.abspath(file_path)

    database = load_database()

    record = None

    for item in database["files"]:
        if item["path"] == file_path:
            record = item
            break

    if record is None:
        print("This file is not registered!")
        return
    if not os.path.isfile(file_path):

        print("\nWARNING: Registered file has been deleted!")

        record_event(
            file_path,
            "DELETED",
            get_risk_level("DELETED")
        )

        return

       
    current_hash = calculate_file_hash(file_path)

    original_hash = record["sha256"]

    if original_hash == current_hash:
        print("\nFILE STATUS: UNCHANGED")
        print("The file matches its registered fingerprint.")

    else:
        print("\nFILE STATUS: MODIFIED")
        print("WARNING: The file content has changed!")

        print("\nOriginal hash:", original_hash)
        print("Current hash:", current_hash)

        record_event(
            file_path,
            "MODIFIED",
            get_risk_level("MODIFIED")
        )

def show_menu():

    while True:

        print("\n==============================")
        print("         FILEGUARD AI")
        print("  Intelligent File Monitoring")
        print("==============================")

        print("1. Register a file")
        print("2. Verify file integrity")
        print("3. View security event history")
        print("4. AI security analysis")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            register_file()

        elif choice == "2":
            verify_file()

        elif choice == "3":
            view_events()

        elif choice == "4":
            analyze_latest_event()

        elif choice == "5":
            print("\nThank you for using FileGuard AI!")
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    show_menu()