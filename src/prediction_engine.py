TOTAL_FILES_TARGET = 1000

# Time-to-compromise function
def estimate_time_to_compromise(file_events):

    if file_events == 0:
        return "Unknown"

    estimated_seconds = 1000 / file_events

    estimated_minutes = estimated_seconds / 60

    print("\n           PREDICTION ENGINE           ")
    print(f"Current File Events: {file_events}")
    print(f"Estimated Time to Compromise: {estimated_minutes:.2f} minutes")
    print("                                         \n")

# Financial Impact function
def estimate_financial_impact(threat_level):

    if threat_level == "LOW":
        return "R1,000"

    elif threat_level == "MEDIUM":
        return "R10,000"

    elif threat_level == "HIGH":
        return "R50,000"

    elif threat_level == "CRITICAL":
        return "R250,000"

    else:
        return "Unknown"

    print(f"Estimated Financial Impact: {impact}")