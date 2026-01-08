import json
from faker import Faker
import random

fake = Faker()

def create_person(person_id):
    gender = random.choice(['Male', 'Female'])
    return {
        "ID": person_id,
        "NAME": fake.first_name(),
        "AGE": random.randint(18, 65),
        "GENDER": gender,
        "JOB POSITION": fake.job()
    }

def generate_database(entries):
    database = []
    for i in range(1, entries + 1):
        database.append(create_person(i))
    return database

if __name__ == "__main__":
    num_entries = 100
    db_data = generate_database(num_entries)
    
    with open('database.json', 'w') as f:
        json.dump(db_data, f, indent=4)
    
    print(f"Successfully generated database.json with {num_entries} entries.")
