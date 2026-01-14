def list_all_entries(db):
    """Main function to list all entries."""

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
