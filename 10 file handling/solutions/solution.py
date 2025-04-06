import os
import zipfile

def search_files(directory, keywords):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if all(keyword in file for keyword in keywords):
                results.append(os.path.join(root, file))
    return results

def list_zip_contents(zip_file_name):
    if os.path.exists(zip_file_name):
        with zipfile.ZipFile(zip_file_name, 'r') as zip_file:
            print(f"Contents of {zip_file_name}:")
            for file in zip_file.namelist():
                print(f"- {file}")
    else:
        print(f"No zip file named {zip_file_name} exists.")

def add_files_to_zip(zip_file_name, files):
    with zipfile.ZipFile(zip_file_name, 'a') as zip_file:
        for file in files:
            zip_file.write(file, arcname=os.path.basename(file))
            print(f"Added {os.path.basename(file)} to {zip_file_name}")

def display_credits():
    print("File Search and Zip Tool")
    print("Developed by: Tabitha")

def main_menu():
    zip_file_name = "results.zip"
    while True:
        print("\nMenu:")
        print("1. Search and add files to zip")
        print("2. List files in zip")
        print("3. Credits")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            directory = input("Enter the directory to search: ")
            keywords = input("Enter keywords separated by commas: ").split(',')
            keywords = [keyword.strip() for keyword in keywords]
            results = search_files(directory, keywords)
            if results:
                print("Found files:")
                for file in results:
                    print(f"- {file}")
                add_to_zip = input("Do you want to add these files to the zip? (yes/no): ").strip().lower()
                if add_to_zip == 'yes':
                    add_files_to_zip(zip_file_name, results)
            else:
                print("No files found matching the keywords.")
        elif choice == '2':
            list_zip_contents(zip_file_name)
        elif choice == '3':
            display_credits()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
