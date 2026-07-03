# Importing libraries
import correlation_engine as ce
import psutil
import time

print("PowerShell Monitor Started...\n")

# This while loop ensures that for any suspicious execution on Powershell, it immediately triggers off to alert the user

while True:

    for process in psutil.process_iter(['pid', 'name']):

        try:

            process_name = process.info['name']

            if process_name:

                if (
                    "powershell" in process_name.lower()
                    or
                    "pwsh" in process_name.lower()
                ):
                    ce.powershell_detected = True
                    ce.evaluate_threat()

                    print(
                        f"⚠ PowerShell Detected | "
                        f"PID: {process.info['pid']} | "
                        f"Name: {process_name}"
                    )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    time.sleep(5)