from common.db_manager import Database

def main():
    """Main function to list all entries."""
    db = Database()

    if not db.entries:
        print("The database is currently empty.")
        return

    print("--- All Database Entries ---")
    # Loop through each Person object in the database and print it.
    # The __str__ method in the Person class is automatically used here.
    for person in db.entries:
        print(person)
    print("----------------------------")
    print(f"Total entries: {len(db.entries)}")


# This standard entry point ensures that the main() function is called
# only when the script is executed directly.
if __name__ == "__main__":
    main()
