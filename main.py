# We start by importing the Person and Database classes from our central "toolbox".
# This is the only import we need to handle all database operations.
from common.db_manager import Database
from add_entry_oop import *
from list_entries_oop import *
from delete_entry_oop import *

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