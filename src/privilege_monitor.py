# Importing libraries
import ctypes
import time
import correlation_engine as ce

# Defining a privilege function

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


print("Privilege Monitor Running...\n")

was_admin = is_admin()

while True:

    current_admin = is_admin()

    if current_admin:
        print("\n🚨 PRIVILEGE ESCALATION DETECTED")
        ce.privilege_escalation_detected = True
        ce.evaluate_threat()

    if current_admin:
        print("⚠ Running with Administrator privileges")

    was_admin = current_admin

    time.sleep(5)