# We start by importing the Person and Database classes from our central "toolbox".
# This is the only import we need to handle all database operations.
from common.db_manager import Person, Database

# --- Function for Listing Entries ---
# This function contains the exact same logic as our old 'list_entries_oop.py' script.
# We pass 'db' (the database object) into it so it has access to the entries.
def list_all_entries(db):
    if not db.entries:
        print("\nThe database is currently empty.")
        return

    print("\n--- All Database Entries ---")
    for person in db.entries:
        print(person)
    print("----------------------------")
    print(f"Total entries: {len(db.entries)}")

# --- Function for Adding an Entry ---
# This function contains the logic from 'add_entry_oop.py'.
# It takes the 'db' object so it can call the 'get_next_id' and 'add_entry' methods.
def add_new_entry(db):
    print("\n--- Add New Entry ---")
    name = input("Enter NAME (first name only): ")
    while True:
        try:
            # Added a check to make sure age is not empty.
            age_str = input("Enter AGE: ")
            if not age_str:
                print("Age cannot be empty.")
                continue
            age = int(age_str)
            break
        except ValueError:
            print("Invalid input. Please enter a number for age.")
            
    gender = input("Enter GENDER (Male/Female): ")
    job_position = input("Enter JOB POSITION: ")

    new_id = db.get_next_id()
    new_person = Person(new_id, name, age, gender, job_position)
    db.add_entry(new_person)

# --- Function for Deleting an Entry ---
# This function contains the logic from 'delete_entry_oop.py'.
def delete_entry(db):
    print("\n--- Delete Entry ---")
    if not db.entries:
        print("The database is empty. Nothing to delete.")
        return

    name_to_find = input("Enter the name of the person to find: ")
    found_people = db.find_by_name(name_to_find)

    if not found_people:
        print(f"No entries found with the name '{name_to_find}'.")
        return

    print("\nFound the following entries:")
    for person in found_people:
        print(person)
    
    while True:
        try:
            # Added a small feature to allow the user to cancel the delete operation.
            id_to_delete_str = input("\nEnter the ID of the entry you want to delete (or press Enter to cancel): ")
            if not id_to_delete_str:
                print("Delete operation cancelled.")
                return
            id_to_delete = int(id_to_delete_str)
            
            if any(p.id == id_to_delete for p in found_people):
                db.delete_entry_by_id(id_to_delete)
                break
            else:
                print("Invalid ID. Please enter an ID from the list shown above.")
        except ValueError:
            print("Invalid input. Please enter a number for the ID.")

# --- A Simple Function to Show the Menu ---
# The only job of this function is to print the options for the user.
# This keeps the main loop cleaner.
def show_menu():
    print("\n--- Database Management Menu ---")
    print("1. List all entries")
    print("2. Add a new entry")
    print("3. Delete an entry")
    print("4. Exit")
    print("--------------------------------")

# --- The Main Program Controller ---
def main():
    # 1. Create ONE instance of the Database. This is important.
    # We create it once and then pass it to the other functions.
    # This way, it loads the file once and keeps all changes in memory until the program exits.
    db = Database()

    # 2. The Main Loop. 'while True:' creates a loop that runs forever until we explicitly 'break' out of it.
    while True:
        # 3. Show the user their options.
        show_menu()
        
        # 4. Get the user's choice.
        choice = input("Please enter your choice (1-4): ")

        # 5. The 'if/elif/else' block acts as a router. It checks the user's
        #    choice and calls the corresponding function.
        if choice == '1':
            list_all_entries(db)
        elif choice == '2':
            add_new_entry(db)
        elif choice == '3':
            delete_entry(db)
        elif choice == '4':
            # If the user chooses '4', we print a goodbye message and 'break' the loop.
            print("Exiting the program. Goodbye!")
            break
        else:
            # If the user enters anything else, we show an error message.
            print("Invalid choice. Please enter a number between 1 and 4.")

# The standard entry point that kicks off the whole program by calling main().
if __name__ == "__main__":
    main()