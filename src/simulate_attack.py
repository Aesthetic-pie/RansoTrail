import os
import time

TEST_FOLDER = "../data/simulation"

# Create folder if it doesn't exist
os.makedirs(TEST_FOLDER, exist_ok=True)

print("Starting ransomware simulation...\n")

# Create files
for i in range(20):
    filename = os.path.join(TEST_FOLDER, f"file_{i}.txt")

    with open(filename, "w") as f:
        f.write("Original content")

    print(f"Created: {filename}")

    time.sleep(0.2)

# Modify files
for i in range(20):
    filename = os.path.join(TEST_FOLDER, f"file_{i}.txt")

    with open(filename, "a") as f:
        f.write("\nEncrypted content simulation")

    print(f"Modified: {filename}")

    time.sleep(0.2)

# Rename files
for i in range(20):
    old_name = os.path.join(TEST_FOLDER, f"file_{i}.txt")
    new_name = os.path.join(TEST_FOLDER, f"file_{i}.locked")

    os.rename(old_name, new_name)

    print(f"Renamed: {new_name}")

    time.sleep(0.2)

print("\nSimulation complete.")