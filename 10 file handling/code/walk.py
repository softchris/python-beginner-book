import os

search_for = "log"
app_name = "SCANNER 1.0"

# current directory
current_directory = os.getcwd()
print(f"## Running {app_name}  ##")
print(".............")
print(f"Searching for <<{search_for}>> in \"{current_directory}\"")


for root, dirs, files in os.walk('logs'):
    current_dir = ""
    for file in files:
        if current_dir != root:
            current_dir = root
            print(f"[DIRECTORY]: {root}")

        print(f"  [FILE]: {file}")
        if 'log' in file:
            print(f"Found <<{search_for}>> in \"{file}\"")
            print(file)