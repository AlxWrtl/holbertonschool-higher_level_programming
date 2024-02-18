readme_content = """

# Python Utility Functions

This repository contains a collection of Python scripts designed to facilitate various common tasks, including file operations, JSON data manipulation, and generating Pascal's triangle. Each script is standalone and designed to be easily integrated into larger projects.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [File Operations](#file-operations)
  - [JSON Data Handling](#json-data-handling)
  - [Pascal's Triangle](#pascals-triangle)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributors](#contributors)
- [License](#license)

## Installation

No installation is required, as each script is executed directly by a Python interpreter. Ensure you have Python 3 installed on your system.

## Usage

### File Operations

- **Reading Files**: `0-read_file.py` allows reading from a file and printing its contents to the console.
- **Writing Files**: `1-write_file.py` enables writing text to a file, creating or overwriting as necessary.
- **Appending to Files**: `2-append_write.py` supports appending text to the end of a file.

### JSON Data Handling

- **Converting to JSON**: `3-to_json_string.py` and `5-save_to_json_file.py` provide functionality to convert Python objects to JSON strings and save them to a file, respectively.
- **Converting from JSON**: `4-from_json_string.py` and `6-load_from_json_file.py` are used to parse JSON strings into Python objects and load Python objects from a JSON file, respectively.
- **Class Serialization**: `8-class_to_json.py`, `9-student.py`, `10-student.py`, and `11-student.py` demonstrate how to serialize and deserialize custom Python class instances.
- **List Serialization**: `7-add_item.py` illustrates adding command-line arguments to a list and saving them to a JSON file.

### Pascal's Triangle

- **Generating Pascal's Triangle**: `12-pascal_triangle.py` provides a function to generate Pascal's triangle up to a specified number of rows.

## Features

- Easy-to-use functions for file reading, writing, and appending.
- Simple JSON serialization and deserialization for Python objects.
- Utility for generating Pascal's triangle.

## Dependencies

- Python 3.6 or later
- No external libraries are required beyond the standard Python libraries.