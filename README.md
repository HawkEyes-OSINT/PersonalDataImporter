Personal Data Importer

Welcome to Personal Data Importer, a program designed to transfer personal user data from CSV files to SQLite databases. This tool allows you to seamlessly import data into SQLite databases with a predefined table structure.
Supported Tables

The program supports the following tables in the SQLite databases:

    names:
        UID
        First Middle Last
    emails
    passwords
    usernames
    phones
    addresses
    sm_urls (Social Media URLs)

The names table is required, and the IDs from the other tables will correspond to the ID of the relevant name.
Getting Started

To use the Personal Data Importer program, follow these steps:

    Clone the Repository: Start by cloning the repository to your local machine using the following command:

    bash

git clone https://github.com/HawkEyes-OSINT/PersonalDataImporter.git

Install Dependencies: Navigate to the project directory and install the required dependencies by running the following command:

pip install -r requirements.txt

This will ensure that you have all the necessary packages installed to run the program.

Run the Program: Execute the program by running the following command:

css

    python main.py

    This will launch the Personal Data Importer.

Usage

Upon running the program, you will have two options:

    Create a New Database: Select this option if you want to create a new SQLite database with the predefined table structure mentioned above. You will be prompted to provide the relevant column names for each table.

    Import Data to an Existing Database: If you already have an SQLite database with a compatible table structure, choose this option to import data from a CSV file. The program will prompt you to map the CSV columns to the corresponding table columns. You will also have the opportunity to merge or separate columns as needed.

Follow the on-screen instructions and provide the necessary inputs to complete the data import process.

Feel free to explore the program's features and customize it to suit your needs.

If you encounter any issues or have questions, please don't hesitate to open an issue on the repository page.

Happy data importing with Personal Data Importer!

Note: Make sure you have a backup of your data before performing any database operations.
