from common.db_manager import Database

def main():
    """Main function to run the delete entry process."""
    db = Database()

    # 1. Ask the user for a name.
    name_to_find = input("Enter the name of the person to find: ")
    
    # 2. Use our new method to find all people with that name.
    found_people = db.find_by_name(name_to_find)

    # If the list of found people is empty, tell the user and stop.
    if not found_people:
        print(f"No entries found with the name '{name_to_find}'.")
        return

    # 3. If people were found, display them to the user.
    # This is where our new __str__ method is automatically used by print()!
    print("\nFound the following entries:")
    for person in found_people:
        print(person)
    
    # 4. Ask the user for the ID of the person they want to delete.
    while True: # This loop will continue until a valid ID is entered.
        try:
            id_to_delete_str = input("\nEnter the ID of the entry you want to delete: ")
            id_to_delete = int(id_to_delete_str) # Convert the input string to a number.
            
            # This is a clever check. 'any(...)' returns True if at least one item in the list meets the condition.
            # We check if any person 'p' in our 'found_people' list has an ID that matches the user's input.
            # This ensures the user can only delete an ID that was actually displayed.
            if any(p.id == id_to_delete for p in found_people):
                db.delete_entry_by_id(id_to_delete) # If the ID is valid, call the delete method.
                break # Exit the 'while' loop.
            else:
                print("Invalid ID. Please enter an ID from the list shown above.")
        except ValueError:
            print("Invalid input. Please enter a number for the ID.")

if __name__ == "__main__":
    main()
