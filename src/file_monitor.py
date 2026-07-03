# Importing python libraries to work with

import correlation_engine as ce

high_activity_alerted = False
mass_rename_alerted = False
mass_delete_alerted = False
encryption_alerted = False

risk_score = 0
event_times = []
event_counts = {
    "CREATED": 0,
    "MODIFIED": 0,
    "RENAMED": 0,
    "DELETED": 0
}

from datetime import datetime, timedelta
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import csv
import os

# The folder that we are monitoring
WATCH_FOLDER = "../data"

# Log file to be generated in a csv format
LOG_FILE = "../logs/events.csv"


# Create log file if it doesn't exist
os.makedirs("../logs", exist_ok=True)

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "event_type", "file_path", "risk_score"])


class RansomwareMonitor(FileSystemEventHandler):
# Log() function

    def log(self, event_type, path):
        global risk_score
        global event_times
        global event_counts
        current_time = datetime.now()
        event_times.append(current_time)
        event_counts[event_type] += 1
        ce.file_events += 1
        ce.evaluate_threat()

        event_times = [
	    t for t in event_times
	    if current_time - t <= timedelta(seconds=10)
	]
        recent_events = len(event_times)

        # Assign risk points
        if event_type == "CREATED":
               risk_score += 2
        elif event_type == "MODIFIED":
        	risk_score += 5
        elif event_type == "RENAMED":
        	risk_score += 8
        elif event_type == "DELETED":
        	risk_score += 10

    	# Log to CSV
        with open(LOG_FILE, "a", newline="") as f:
        	writer = csv.writer(f)
        	writer.writerow([time.ctime(), event_type, path, risk_score])

    	# Console output
        print(f"[{event_type}] {path} → Risk Score: {risk_score}")

    	# Warning trigger (alert)
        if risk_score > 50:
        	print("⚠ WARNING: Suspicious ransomware-like activity detected!")
        global high_activity_alerted

        if recent_events >= 20 and not high_activity_alerted:
            print("\n🚨 HIGH ACTIVITY DETECTED")
            print(f"Events in last 10 seconds: {recent_events}")

            print("\n Activity Breakdown:")
            print(f"CREATED: {event_counts['CREATED']}")
            print(f"MODIFIED: {event_counts['MODIFIED']}")
            print(f"RENAMED: {event_counts['RENAMED']}")
            print(f"DELETED: {event_counts['DELETED']}")

            print("\n⚠ Possible ransomware behavior!\n")
            high_activity_alerted = True

        global mass_rename_alerted
        if event_counts["RENAMED"] >= 10 and not mass_rename_alerted:
            print("🚨 MASS FILE RENAMING DETECTED")
            mass_rename_alerted = True

        global mass_delete_alerted
        if event_counts["DELETED"] >= 10 and not mass_delete_alerted:
            print("🚨 MASS FILE DELETION DETECTED")
            mass_delete_alerted = True

        global encryption_alerted           
        if (
            event_counts["MODIFIED"] >= 20
            and event_counts["RENAMED"] >= 10
            and not encryption_alerted
        ):
            print("\n🔒 MASS ENCRYPTION BEHAVIOR DETECTED")
            print(f"Modified Files: {event_counts['MODIFIED']}")
            print(f"Renamed Files: {event_counts['RENAMED']}")
            print("⚠ Possible ransomware encryption activity!\n")
        encryption_alerted = True
        high_activity_alerted = True

    def on_created(self, event):
        self.log("CREATED", event.src_path)

    def on_deleted(self, event):
        self.log("DELETED", event.src_path)

    def on_modified(self, event):
        self.log("MODIFIED", event.src_path)

    def on_moved(self, event):
        self.log("RENAMED", event.dest_path)

# Adding correlation logic function
def check_correlation():
    global risk_score

    import correlation_engine as ce

    if ce.file_events >=20 and ce.powershell_detected:
        print("\n🚨CORRELATED THREAT DETECTED 🚨")
        print("Reason:")
        print("- High file activity detected")
        print("- PowerShell process running")
        print(f"- File events: {ce.file_events}")
        print(f"- Risk Score: {risk_score}")
        print("/n⚠ High confidence ransomware behaviour!\n")


if __name__ == "__main__":
    print(f"Monitoring started on: {WATCH_FOLDER}")

    observer = Observer()
    observer.schedule(RansomwareMonitor(), WATCH_FOLDER, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()