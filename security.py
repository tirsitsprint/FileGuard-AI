
import json
import os
from datetime import datetime


LOG_FILE = "logs.json"


def load_logs():

    if not os.path.exists(LOG_FILE):
        return {"events": []}

    if os.path.getsize(LOG_FILE) == 0:
        return {"events": []}

    with open(LOG_FILE, "r") as file:
        return json.load(file)


def save_logs(logs):

    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)


def record_event(file_path, event_type, risk_level):

    logs = load_logs()

    new_event = {
        "file": file_path,
        "event": event_type,
        "risk": risk_level,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    logs["events"].append(new_event)

    save_logs(logs)

    print("\nSecurity event recorded!")
if __name__ == "__main__":

    record_event(
        "test.txt",
        "MODIFIED",
        "HIGH"
    )

def view_events():

    logs = load_logs()

    if not logs["events"]:
        print("\nNo security events recorded yet.")
        return

    print("\n========== SECURITY EVENT HISTORY ==========")

    for index, event in enumerate(logs["events"], start=1):

        print(f"\nEvent #{index}")
        print("File:", event["file"])
        print("Event:", event["event"])
        print("Risk:", event["risk"])
        print("Time:", event["timestamp"])

    print("\n============================================")
def get_risk_level(event_type):

    if event_type == "DELETED":
        return "HIGH"

    elif event_type == "MODIFIED":
        return "MEDIUM"

    else:
        return "LOW"