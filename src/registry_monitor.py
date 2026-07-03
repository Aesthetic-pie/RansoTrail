# Importing libraries

import correlation_engine as ce
import winreg
import time

REG_PATH = r"Software"

# Defining a registry function that will be used

def get_registry_entries():
    entries = {}

    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            REG_PATH
        )

        index = 0

        while True:
            try:
                name, value, reg_type = winreg.EnumValue(key, index)
                entries[name] = value
                index += 1

            except OSError:
                break

        winreg.CloseKey(key)

    except Exception as e:
        print(f"Error reading registry: {e}")
    return entries


print("Registry Monitor Started...\n")

previous_entries = get_registry_entries()

while True:

    current_entries = get_registry_entries()
  
    # NEW entries
    for name, value in current_entries.items():
        if name not in previous_entries:
            print("\n🚨 NEW REGISTRY ENTRY DETECTED")
            print(f"Name: {name}")
            print(f"Value: {value}")
            ce.registry_changes += 1
            ce.evaluate_threat()

        elif previous_entries[name] != value:
            print("/n⚡ REGISTRY VALUE CHANGED")
            print(f"Name: {name}, Old Value: {previous_entries[name]}, New Value: {value}")
            ce.registry_changes += 1
            ce.evaluate_threat()

# REMOVED entries
    for name in previous_entries:
        if name not in current_entries:
            print("\n🚨 REGISTRY ENTRY DETECTED")
            print(f"Name: {name}")
            ce.registry_changes += 1
            ce.evaluate_threat()


    previous_entries = current_entries
    time.sleep(5)