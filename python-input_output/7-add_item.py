#!/usr/bin/python3
"""Script to add all arguments to a Python list and save them to a file.

This script takes all command-line arguments provided to it, adds them to a
list, and then saves the list to a JSON file. If the JSON file does not exist,
it creates a new list; otherwise, it appends to the existing list.
"""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
file_name = "add_item.json"  # Define the name of the JSON file to use

try:
    json_file = load_from_json_file(file_name)
except FileNotFoundError:
    json_file = []

json_file.extend(sys.argv[1:])

save_to_json_file(json_file, file_name)
