from datetime import datetime
import csv
import os

def log_threat(
    risk_score,
    threat_level,
    file_events,
    registry_changes,
    powershell_detected,
    privilege_escalation
):

    print(" THREAT LOGGER CALLED")

    log_file = "../logs/threat_log.csv"

    file_exists = os.path.isfile(log_file)

    with open(log_file, "a", newline="") as csvfile:

        writer = csv.writer(csvfile)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Risk Score",
                "Threat Level",
                "File Events",
                "Registry Changes",
                "PowerShell Activity",
                "Privilege Escalation"
            ])

        writer.writerow([
            datetime.now(),
            risk_score,
            threat_level,
            file_events,
            registry_changes,
            powershell_detected,
            privilege_escalation
        ])