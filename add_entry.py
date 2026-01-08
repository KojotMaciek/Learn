import json

def add_entry_manually():
    try:
        with open('database.json', 'r') as f:
            database = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        database = []

    # Find the highest existing ID to generate a new one
    if database:
        new_id = max(entry.get('ID', 0) for entry in database) + 1
    else:
        new_id = 1

    # Get user input
    name = input("Enter NAME (first name only): ")
    while True:
        try:
            age = int(input("Enter AGE: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for age.")
            
    gender = input("Enter GENDER (Male/Female): ")
    job_position = input("Enter JOB POSITION: ")

    # Create new entry
    new_entry = {
        "ID": new_id,
        "NAME": name,
        "AGE": age,
        "GENDER": gender,
        "JOB POSITION": job_position
    }

    # Add to database and save
    database.append(new_entry)
    with open('database.json', 'w') as f:
        json.dump(database, f, indent=4)

    print(f"Successfully added new entry with ID {new_id} to database.json.")

if __name__ == "__main__":
    add_entry_manually()
