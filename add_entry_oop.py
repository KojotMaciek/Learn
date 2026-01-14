from common.db_manager import Person

# This is the main function where the program's execution starts.
def add_new_entry(db):

    # Get user input from the terminal, just like in the previous script.
    name = input("Enter NAME (first name only): ")
    while True:
        try:
            age = int(input("Enter AGE: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for age.")
            
    gender = input("Enter GENDER (Male/Female): ")
    job_position = input("Enter JOB POSITION: ")

    # Create a new Person object using the data the user provided.
    new_id = db.get_next_id()
    new_person = Person(new_id, name, age, gender, job_position)
    
    # Tell our database object to add the new person.
    db.add_entry(new_person)
