"""
This file controls the user interface via command line
"""

from art import *
from db_creator import create_db
from db_inserter import insert_data
from support_methods import verify_path


def start_menu():
    """
    Display welcome screen
    Have user choose to create a new DB 
    or insert data to an existing DB
    """

    # print open screen
    print(text2art('PersonalData\nImporter', font='smslant'))

    # print menu options
    print('Welcome to the PersonalDataImporter')
    print('Please choose one of the following options:')
    print('1. New DB')
    print('2. Existing DB')
    print('3. Exit')

    # execute users choice
    execution = [new_db_menu, existing_db_menu, exit]
    try:
        execution[int(input('Your choice: ')) - 1]()
    except IndexError:
        print('Invalid choice')
        start_menu()
    except ValueError:
        print('Invalid choice')
        start_menu()


def new_db_menu():
    """
    Get target path and new DB name.
    Run new DB code.
    """

    # get db name and path
    target_path = input('Please enter the target path: ')
    db_name = input('Please enter the new DB name: ')

    # create new db
    try:
        verify_path(target_path)
        path = create_db(target_path, db_name)
        print('Your new DB was created successfully')
        print('What would you like to do now?')
        print('1. Import data')
        print('2. Exit')
        choice = int(input('Your choice: '))
        if (choice-1):
            print('Thank you for using PersonalDataImporter')
            exit()
        else:
            existing_db_menu(path)
    except Exception as e:
        print(e)
        new_db_menu()


def existing_db_menu(db_path=None):
    """
    Get path for target DB and path for source CSV.
    Run datat insertion methods
    """

    # get db path
    if not db_path:
        db_path = input('Enter the target path (including db name): ')
    
    # get source csv path
    csv_path = input('Enter the source csv path (including file name): ')

    # run insert methods
    try:
        verify_path(db_path)
        verify_path(csv_path)
        insert_data(db_path, csv_path)
        start_menu()
    except Exception as e:
        print(e)
        existing_db_menu()
        