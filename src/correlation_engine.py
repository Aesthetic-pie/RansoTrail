import prediction_engine as pe
import threat_logger as logger

# Intergrating all 3 monitors in the correlation
# correlation_engine.py

file_events = 0
powershell_detected = False
registry_changes = 0
privilege_escalation_detected = False

risk_score = 0
privilege_threat_level = "NONE"

def evaluate_threat():

    global risk_score

    risk_score = 0

    # File Activity
    if file_events >= 20:
        risk_score += 30

    # PowerShell Activity
    if powershell_detected:
        risk_score += 20

    # Registry Activity
    if registry_changes >= 1:
        risk_score += 25

    # Privilege Escalation
    if privilege_escalation_detected:
        risk_score += 40

    global previous_threat_level

    # Threat Classification
    if risk_score >= 80:
        threat_level = "CRITICAL"

    elif risk_score >= 50:
        threat_level = "HIGH"

    elif risk_score >= 20:
        threat_level = "MEDIUM"

    else:
        threat_level = "LOW"

    # Basic Summary

    print("\n========== THREAT ANALYSIS ==========")
    print(f"File Events: {file_events}")
    print(f"PowerShell Detected: {powershell_detected}")
    print(f"Registry Changes: {registry_changes}")
    print(f"Privilege Escalation: {privilege_escalation_detected}")
    print(f"Risk Score: {risk_score}")
    print(f"Threat Level: {threat_level}")
    print("=====================================\n")

    # ONLY ALERT WHEN NECESSARY
    if threat_level != privilege_threat_level:
        print("🚨 STATE CHANGE DETECTED 🚨")
        print(f"Previous: {privilege_threat_level}")
        print(f"Current: {threat_level}")

        if threat_level in ["HIGH", "CRITICAL"]:
            print("\n🚨 CORRELATED THREST DETECTED 🚨")
            print(f"Threat Level: {threat_level}")
            print("⚠ Possible ransomware behavior!\n")

    previous_threat_level = threat_level

    time_estimate = pe.estimate_time_to_compromise(file_events)
    financial_estimate = pe.estimate_financial_impact(threat_level)

    if threat_level in ["HIGH", "CRITICAL"]:
        rg.generate_report(
            threat_level,
            risk_score,
            file_events,
            registry_changes,
            powershell_detected,
            privilege_escalation,
            time_estimate,
            financial_estimate
    )
    
        logger.log_threat( 
           risk_score,
           threat_level,
           file_events,
           registry_changes,
           powershell_detected,
           privilege_escalation
   )