from datetime import datetime


def generate_report(
    threat_level,
    risk_score,
    file_events,
    registry_changes,
    powershell_detected,
    privilege_escalation,
    time_to_compromise,
    financial_impact
):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    report_name = f"incident_{timestamp}.txt"

    with open(report_name, "w") as report:

        report.write("==================================================\n")
        report.write("RANSOMWARE INCIDENT REPORT\n")
        report.write("==================================================\n\n")

        report.write(f"Date: {current_date}\n")
        report.write(f"Time: {current_time}\n")
        report.write(f"Threat Level: {threat_level}\n")
        report.write(f"Risk Score: {risk_score}\n\n")

        report.write("DETECTION SUMMARY\n")
        report.write("-----------------------------\n")

        report.write(f"File Events: {file_events}\n")
        report.write(f"Registry Changes: {registry_changes}\n")
        report.write(f"PowerShell Activity: {powershell_detected}\n")
        report.write(f"Privilege Escalation: {privilege_escalation}\n\n")

        report.write("PREDICTION ENGINE\n")
        report.write("-----------------------------\n")

        report.write(
            f"Time-to-Compromise Estimate: {time_to_compromise}\n"
        )

        report.write(
            f"Financial Impact Estimate: {financial_impact}\n\n"
        )

    print(f"\n📄 Incident report created: {report_name}")


generate_report(
    "HIGH",
    75,
    35,
    2,
    True,
    False,
    "5.4 minutes",
    "R50,000"
)