"""
db_creator.py

create a new db file
"""

import sys
import os
import sqlite3


def create_db(path, name):
    """
    create a new db file

    path: path to the db file
    name: name of the db file
    
    return: None
    """
    path = path + '/' + name + '.db'

    # check if file exists
    if os.path.exists(path):
        print(f"Database '{name}' already exists at '{path}'")
        sys.exit(1)
    # try to import sqlite3
    try:
        # create db file
        conn = sqlite3.connect(path)
        cursor = conn.cursor()

        # create tables
        # names
        cursor.execute("""CREATE TABLE names (
                        uid INTEGER PRIMARY KEY,
                        name TEXT,
                        source TEXT)
                        """)
        
        # emails
        cursor.execute("""CREATE TABLE emails (
                        uid INTEGER,
                        row_value TEXT,
                        source TEXT,
                        FOREIGN KEY (uid) REFERENCES names(uid))
                        """)
        
        # passwords
        cursor.execute("""CREATE TABLE passwords (
                        uid INTEGER,
                        row_value TEXT,
                        source TEXT,
                        FOREIGN KEY (uid) REFERENCES names(uid))
                        """)

        # usernames
        cursor.execute("""CREATE TABLE usernames (
                        uid INTEGER,
                        row_value TEXT,
                        source TEXT,
                        FOREIGN KEY (uid) REFERENCES names(uid))
                        """)
        
        # phones
        cursor.execute("""CREATE TABLE phones (
                        uid INTEGER PRIMARY KEY,
                        row_value TEXT,
                        source TEXT,
                        FOREIGN KEY (uid) REFERENCES names(uid))
                        """)
        
        # addresses
        cursor.execute("""CREATE TABLE addresses (
                        uid INTEGER PRIMARY KEY,
                        row_value TEXT,
                        source TEXT,
                        FOREIGN KEY (uid) REFERENCES names(uid))
                        """)

        # social media urls
        cursor.execute("""CREATE TABLE sm_urls (
                        uid INTEGER PRIMARY KEY,
                        row_value TEXT,
                        source TEXT,
                        FOREIGN KEY (uid) REFERENCES names(uid))
                        """)
        
        # close connection
        conn.commit()
        conn.close()
        print(f"Database '{name}' created at '{path}'")
        return
    except Exception as e:
        print(e)
        sys.exit(1) 

    return path
        