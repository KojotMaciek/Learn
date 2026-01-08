# Python CRUD Application Learning Project

This project is a simple, command-line based CRUD (Create, Read, Update, Delete) application for managing a database of people stored in a JSON file. It was developed as a learning exercise to demonstrate fundamental Python concepts, including Object-Oriented Programming (OOP), file I/O, project structure, and automated testing with pytest.

## Features

- **Create**: Add new people to the database.
- **Read**: List all entries currently in the database.
- **Delete**: Find and remove entries from the database.
- **Menu-Driven Interface**: A user-friendly main script to access all functionalities.
- **JSON Database**: Uses a simple `database.json` file as a data store.
- **Unit Tests**: Includes a suite of tests using `pytest` to ensure core logic is working correctly.
- **Structured Code**: The project is organized into modules for better maintainability.

## Project Structure

The project is organized into the following files and directories:

```
Learn/
│
├── common/
│   └── db_manager.py       # Core module with Person and Database classes.
│
├── tests/
│   └── test_db_manager.py  # Unit tests for the db_manager module.
│
├── .gitignore              # (Optional) To ignore files like __pycache__.
├── add_entry.py            # Original procedural script to add entries.
├── add_entry_oop.py        # OOP script to add entries (now legacy).
├── database.json           # The JSON file used as a database.
├── delete_entry_oop.py     # OOP script to delete entries (now legacy).
├── generate_data.py        # Script to generate initial dummy data.
├── list_entries_oop.py     # OOP script to list entries (now legacy).
├── main.py                 # The main, menu-driven application to run.
├── pytest.ini              # Configuration file for pytest.
└── README.md               # This file.
```

- **`main.py`**: This is the main entry point of the application. Run this file to use the interactive menu.
- **`common/db_manager.py`**: This is the heart of the application. It contains the `Person` class (the blueprint for a person object) and the `Database` class, which handles all the logic for reading, writing, and modifying the `database.json` file.
- **`tests/`**: This directory contains all the automated tests.
- **`pytest.ini`**: This configuration file tells `pytest` how to find the project's source files (`common/`).

## Setup and Installation

1.  **Clone the repository** or download the files to a directory on your computer.

2.  **Install dependencies**. The project requires `Faker` (for generating initial data) and `pytest` (for running tests). You can install them using pip:

    ```bash
    pip install faker pytest
    ```

## Usage

### Running the Main Application

To use the application, run the `main.py` script from the root `Learn` directory.

```bash
python main.py
```

This will launch an interactive menu where you can choose to list, add, or delete entries from the database.

### Generating Initial Data

If your `database.json` is empty or does not exist, you can generate 100 sample entries by running the `generate_data.py` script:

```bash
python generate_data.py
```

## Running Tests

To ensure that all the core database functionalities are working as expected, you can run the suite of unit tests.

From the root `Learn` directory, run the following command:

```bash
pytest
```

`pytest` will automatically discover and run all the tests in the `tests` directory and provide a report of the results. This is a great way to verify your code's integrity after making changes.
