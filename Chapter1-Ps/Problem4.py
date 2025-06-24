import os

directory = "/Riot Games/Riot Client"

print(f"Contents of directory '{directory}':")
for item in os.listdir(directory):
    print(item)
