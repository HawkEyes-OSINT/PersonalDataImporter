"""
Methods to support the program
"""

import os
import csv
from unidecode import unidecode


def verify_path(path):
    """
    Verify that the path exists
    """
    if not os.path.exists(path):
        raise ValueError("Path does not exist")


def request_column(table_name):
    """
    Get column numbers and serperator characters

    :input table_name: name of the table
    :return columns: list of column numbers
    :return to_ignore: list of characters to ignore in the row
    :rtype columns: list
    :rtype to_ignore: list
    """

    columns = []
    to_ignore = []

    # isntructions
    column_instuction = f"""
        Insert the column number for "{table_name}" insertion where the first column is number 0.
        If there are multiple columns than write all the column numbers with each number seprated by a comma,
            For example, if you need to enter columns A, C and D, write: 0,2,3.
        If there are columns that need to be merged, seperate the column numbers with a dash.
            For example, if column A is 'First name' and column B is 'Last name', write 0-1
        If there are no columns for this table, click 'enter'.

        Enter column numbers here:
        """
    seperator_instruction = """
        If there are multiple values in a row or if rows contain characters that should be ignored,
        enter the seperation character or to-ignore character with each character seperated by single quotations
        and seperated by a comma.
        For example, if a row is formatted as follows, [value, value, value], enter '[',']',','
        If there are no such characters, click 'enter'.

        Enter characters here:
        """
    
    # get column numbers
    columns_list = input(column_instuction)
    if not columns_list:
        return columns, to_ignore
    try:
        # check columns and insert into column list
        columns_list = columns_list.split(',')
        for column in columns_list:
            col_range = [int(col) for col in column.split('-') if col.isdigit()]
            if col_range:
                columns.append(col_range)
            else:
                raise ValueError
    except ValueError:
        print("Invalid column number")
        return request_column(table_name)
    
    # get seperater characters
    seperators = input(seperator_instruction)
    try:
        # check input format
        seperators = seperators.split(',')
        [to_ignore.append(seperator.split("\'")[1]) for seperator in seperators if "\'" in seperator]
    except ValueError:
        print("Invalid input")
        return request_column(table_name)
    
    return columns, to_ignore


def format_title(values):
    """
    Format the title of the table
    :input values: list of values
    :return name: formatted name
    :rtype name: str
    """

    name = ' '.join([value.strip() for value in values])
    name = unidecode(name.title())
    return name

def format_lower(value):
    return value.strip().lower()

def format_phone(value):
    """
    Format the phone number
    :input value: phone number
    :return phone_number: formatted phone number
    :rtype phone_number: str
    """

    phone_number = ''
    for char in value:
        if char.isdigit():
            phone_number += char
    return phone_number

def detect_csv_delimiter(filename):
    with open(filename, 'r') as file:
        sample = file.read(4096)  # Read a sample of the file
        
    sniffer = csv.Sniffer()
    delimiter = sniffer.sniff(sample).delimiter
    return delimiter