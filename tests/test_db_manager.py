import pytest
import os
import json
from common.db_manager import Person, Database

# This is a pytest "fixture". A fixture is a function that sets up a consistent
# environment for your tests. This one creates a temporary database file for each test.
@pytest.fixture
def temp_db(tmp_path):
    """
    Creates a temporary database file and a Database instance for testing.
    'tmp_path' is a special fixture provided by pytest that creates a temporary directory.
    """
    # Create a temporary file path for our test database
    temp_db_path = tmp_path / "test_database.json"
    
    # Create a Database instance pointing to this temporary file
    db = Database(filepath=str(temp_db_path))
    
    # 'yield' is like 'return', but it allows the code after it to run after the test is finished.
    # This is our "teardown" phase, where we clean up.
    yield db
    
    # After the test runs, we ensure the temporary file is gone if it exists.
    if os.path.exists(temp_db_path):
        os.remove(temp_db_path)

# --- Test Functions ---
# Each function starts with 'test_' which is how pytest discovers them.
# We pass our 'temp_db' fixture as an argument, so each test gets a fresh, empty database.

def test_add_entry(temp_db):
    """Tests adding a single entry to the database."""
    # ARRANGE: The fixture has already arranged an empty db.
    # ACT: Create a person and add them to the database.
    person = Person(1, "John", 30, "Male", "Engineer")
    temp_db.add_entry(person)
    
    # ASSERT: Check if the outcome is what we expected.
    assert len(temp_db.entries) == 1
    assert temp_db.entries[0].name == "John"
    assert temp_db.entries[0].id == 1

def test_get_next_id(temp_db):
    """Tests the ID generation logic."""
    # ARRANGE: Empty database.
    # ACT & ASSERT: The next ID on an empty DB should be 1.
    assert temp_db.get_next_id() == 1
    
    # ARRANGE: Add an entry.
    temp_db.add_entry(Person(1, "Jane", 25, "Female", "Artist"))
    
    # ACT & ASSERT: The next ID should now be 2.
    assert temp_db.get_next_id() == 2

def test_delete_entry(temp_db):
    """Tests deleting an entry from the database."""
    # ARRANGE: Add two people to the database.
    person1 = Person(1, "Alice", 40, "Female", "Doctor")
    person2 = Person(2, "Bob", 50, "Male", "Manager")
    temp_db.add_entry(person1)
    temp_db.add_entry(person2)
    assert len(temp_db.entries) == 2
    
    # ACT: Delete one of them.
    result = temp_db.delete_entry_by_id(1)
    
    # ASSERT: Check that the deletion was successful and only one person remains.
    assert result is True
    assert len(temp_db.entries) == 1
    assert temp_db.entries[0].name == "Bob"

def test_delete_nonexistent_entry(temp_db):
    """Tests that attempting to delete a non-existent ID fails gracefully."""
    # ARRANGE: Add one person.
    temp_db.add_entry(Person(1, "Alice", 40, "Female", "Doctor"))
    
    # ACT: Try to delete an ID that doesn't exist.
    result = temp_db.delete_entry_by_id(99)
    
    # ASSERT: Check that the result is False and the db is unchanged.
    assert result is False
    assert len(temp_db.entries) == 1

def test_find_by_name(temp_db):
    """Tests finding entries by name."""
    # ARRANGE: Add several people, including two with the same name.
    temp_db.add_entry(Person(1, "Charlie", 35, "Male", "Chef"))
    temp_db.add_entry(Person(2, "Carol", 28, "Female", "Writer"))
    temp_db.add_entry(Person(3, "Charlie", 60, "Male", "Pilot"))
    
    # ACT: Find all people named "Charlie" (case-insensitive).
    found = temp_db.find_by_name("charlie")
    
    # ASSERT: Check that exactly two people were found.
    assert len(found) == 2
    
    # ACT: Find a person with a unique name.
    found_carol = temp_db.find_by_name("Carol")
    
    # ASSERT: Check that one person was found and it's the correct one.
    assert len(found_carol) == 1
    assert found_carol[0].id == 2

def test_save_and_load(temp_db):
    """Tests that saving to a file and loading from it works correctly."""
    # ARRANGE: Add an entry to the in-memory database.
    temp_db.add_entry(Person(1, "David", 45, "Male", "Scientist"))
    
    # ACT: The 'add_entry' method automatically saves. Now, create a *new*
    # Database instance pointing to the same temporary file to simulate reloading.
    new_db_instance = Database(filepath=temp_db.filepath)
    
    # ASSERT: Check that the new instance loaded the data correctly.
    assert len(new_db_instance.entries) == 1
    assert new_db_instance.entries[0].name == "David"
