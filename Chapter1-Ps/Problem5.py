import os

#Specify the directory path
directory = "/Riot Games/Riot Client"

#Print the contents of a directory
print(f"Contents of directory '{directory}':")
for item in os.listdir(directory):
    print(item)
