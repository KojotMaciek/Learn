import json
import os # The 'os' module lets us interact with the operating system, which is great for working with file paths.

# --- The Person Class ---
# This class has not changed. It is the blueprint for a single person.
# By having it here, every script that imports it will use the exact same blueprint.
class Person:
    def __init__(self, person_id, name, age, gender, job_position):
        self.id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self.job_position = job_position

    # Converts the Person object to a dictionary so it can be written to JSON.
    def to_dict(self):
        return {
            "ID": self.id,
            "NAME": self.name,
            "AGE": self.age,
            "GENDER": self.gender,
            "JOB POSITION": self.job_position
        }

    # Creates the nice, readable string when we print a Person object.
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Job: {self.job_position}"


# --- The Database Class ---
# This is the complete version of our Database class, containing all the methods
# we've created so far. It's the single point of control for our database file.
class Database:
    # The constructor for the class.
    def __init__(self, filepath='database.json'):
        # --- Important Path Logic ---
        # This is a new, more robust way to handle the file path.
        # The problem: This script is in the 'common' folder, but 'database.json' is in the parent 'Learn' folder.
        # We need to make sure the script can always find the JSON file, no matter where we run it from.
        
        # os.path.dirname(__file__) gets the directory of the current file (e.g., 'c:\\Learn\\common').
        # os.path.join(...) is a smart way to build file paths that works on any OS.
        # '..' is a special symbol that means "go up one directory".
        # So, this line builds a path that goes from 'c:\\Learn\\common', up to 'c:\\Learn', and then points to 'database.json'.
        self.filepath = os.path.join(os.path.dirname(__file__), '..', filepath)
        
        # Now, we load the entries using this correct path.
        self.entries = self.load_entries()

    # Loads entries from the JSON file. No changes here.
    def load_entries(self):
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
                return [Person(p['ID'], p['NAME'], p['AGE'], p['GENDER'], p['JOB POSITION']) for p in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    # Saves entries back to the JSON file. No changes here.
    def save_entries(self):
        with open(self.filepath, 'w') as f:
            json.dump([p.to_dict() for p in self.entries], f, indent=4)

    # Gets the next available ID. No changes here.
    def get_next_id(self):
        if not self.entries:
            return 1
        return max(p.id for p in self.entries) + 1

    # Adds a new person and saves. We updated the print message to be more general.
    def add_entry(self, person):
        self.entries.append(person)
        self.save_entries()
        print(f"Successfully added new entry with ID {person.id}.")

    # Finds people by name. No changes here.
    def find_by_name(self, name):
        return [p for p in self.entries if p.name.lower() == name.lower()]

    # Deletes a person by their ID. No changes here.
    def delete_entry_by_id(self, person_id):
        initial_count = len(self.entries)
        self.entries = [entry for entry in self.entries if entry.id != person_id]
        
        if len(self.entries) < initial_count:
            self.save_entries()
            print(f"Successfully deleted entry with ID {person_id}.")
            return True
        else:
            print(f"Error: No entry found with ID {person_id}.")
            return False
