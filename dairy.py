import os
import datetime

def greeting():
    print("Hello again!")
    print("Welcome to your diary program. What would you like to do?")
    print("1. Write your to-do list in your diary.")
    print("2. Check your diary.")
    print("3. Create your own diary.")
    print("4. List all diaries.")
    print("5. Modify a diary.")
    print("6. Delete a diary.")
    print("7. Create a new diary by date.")
    print("8. Exit program.")

def write_on(filename, s):
    with open(filename, "a") as f:
        f.write(s + '\n')

def check(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"Diary '{filename}' not found.")

def create_diary():
    diary_name = input("Enter the name for your new diary (e.g., 'my_diary.txt'): ")
    try:
        with open(diary_name, "x"):  # Use "x" to create the file
            print(f"Diary '{diary_name}' created successfully!")
    except FileExistsError:
        print(f"Diary '{diary_name}' already exists.")

def create_diary_by_date():
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    diary_name = input(f"Enter the name for your new diary for today ({date_str}.txt): ")
    try:
        with open(diary_name, "x"):  # Use "x" to create the file
            print(f"Diary '{diary_name}' created successfully!")
    except FileExistsError:
        print(f"Diary '{diary_name}' already exists.")

def list_all_diaries():
    diaries = [file for file in os.listdir() if file.endswith(".txt")]
    if diaries:
        print("List of diaries:")
        for diary in diaries:
            print(diary)
    else:
        print("No diaries found.")

def modify_diary(filename):
    print(f"Modifying diary '{filename}':")
    check(filename)
    line_number = int(input("Enter the line number to modify: ")) - 1
    new_entry = input("Enter the new entry: ")
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        lines[line_number] = new_entry + '\n'
        with open(filename, "w") as f:
            f.writelines(lines)
        print("Diary modified successfully!")
    except FileNotFoundError:
        print(f"Diary '{filename}' not found.")

def delete_diary(filename):
    try:
        os.remove(filename)
        print(f"Diary '{filename}' deleted successfully!")
    except FileNotFoundError:
        print(f"Diary '{filename}' not found.")

# Example usage:
greeting()

# Ask the user whether they want to write to an existing file or create a new one
user_choice = input("Do you want to write to an existing file (enter 'existing') or create a new one (enter 'new')? ").lower()

diary_filename = ""

if user_choice == 'existing':
    diary_filename = input("Enter the name of the existing diary file: ")
    if not os.path.isfile(diary_filename):
        print(f"Diary '{diary_filename}' not found.")
        user_choice = 'new'

if user_choice == 'new':
    diary_filename = input("Enter the name for your new diary file: ")
    create_diary()

# Let the user enter their own tasks
while True:
    task = input("Enter a task for your to-do list (press Enter to finish): ")
    if not task:
        break
    write_on(diary_filename, task)

while True:
    user_input = input("Enter the number corresponding to your choice: ")

    if user_input == '1':
        # Write to-do list
        user_input = input("Enter a to-do item: ")
        write_on(diary_filename, user_input)
    elif user_input == '2':
        # Check diary
        check(diary_filename)
    elif user_input == '3':
        # Create diary
        diary_filename = input("Enter the name for your new diary file: ")
        create_diary()
    elif user_input == '4':
        # List all diaries
        list_all_diaries()
    elif user_input == '5':
        # Modify a diary
        diary_filename = input("Enter the name of the diary to modify: ")
        modify_diary(diary_filename)
    elif user_input == '6':
        # Delete a diary
        diary_filename = input("Enter the name of the diary to delete: ")
        delete_diary(diary_filename)
    elif user_input == '7':
        # Create a new diary by date
        create_diary_by_date()
    elif user_input == '8':
        # Exit program
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")

print("Program finished.")
