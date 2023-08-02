"""
Inserts data from CSV file to SQLite3 DB
"""

import sqlite3
import csv
import re
from support_methods import request_column, format_lower, format_phone, format_title, detect_csv_delimiter


def insert_data(db_path, csv_path):
    """
    Inserts data from CSV file to SQLite3 DB
    """

    # cursor prep
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    qname = 'INSERT INTO names (name) VALUES (?)'
    qtable = 'INSERT INTO {} (uid, row_value, source) VALUES (?, ?, ?)'
    name_id = 0

    # variables
    tables = ['names', 'emails', 'passwords', 'usernames', 'phones', 'addresses', 'sm_urls']
    source = csv_path.split('/')[-1]

    # get csv map instructions
    instructions = []
    for table in tables:
        columns, ignore = request_column(table)
        instructions.append([table, columns, ignore])

    # open csv file
    print('[-] Inserting data to DB')
    with open(csv_path) as file:
        reader = csv.reader(file, delimiter=detect_csv_delimiter(csv_path))
        next(reader) # skip first line
        line_nm = 0
        for line in reader:
            line_nm += 1
            try:
                for instuction in instructions:
                    # get istructions
                    table, columns, strip_char = instuction

                    # get data from csv
                    values = [line[col[0]:col[len(col)-1]+1] for col in columns]
                    if table == 'names' and not values:
                        # names is a required table
                        print('Must provide a name value')
                        return

                    # format values
                    formated_values = []
                    tmp_values = []
                    if strip_char != '':
                        for value in values:
                            # create sublist
                            merged = ''
                            for v in value:
                                merged += v
                            value = merged
                            for char in strip_char:
                                value = value.replace(char, '')
                            words = value.split()
                            [tmp_values.append([word]) for word in words if word]
                        values = tmp_values
                    for value in values:
                        if table == 'names' or table == 'addresses':
                            formated_values.append(format_title(value))
                        elif table == 'emails':
                            formated_values.append(format_lower(value[0]))
                        elif table == 'phones':
                            formated_values.append(format_phone(value[0]))
                        else:
                            formated_values.append(value[0])

                    # insert data to DB
                    if table == 'names':
                        cur.execute(qname, (formated_values[0],))
                        name_id = cur.lastrowid
                    else:
                        [cur.execute(qtable.format(table), (name_id, value, source)) for value in formated_values if value]
            except Exception as e:
                print(f'[!] {line_nm}', e)

        conn.commit()
        conn.close()
    print('[+] Data inserted to DB')
    