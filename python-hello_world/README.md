
# Python Basics Project

## Overview

This project includes a series of Python scripts demonstrating fundamental Python concepts such as string manipulation, formatted printing, and using libraries. Each script showcases a different aspect of the Python language.

## Scripts Overview

### 1. Simple Print Statement
- **Filename**: `01_print_statement.py`
- **Description**: Prints a statement about programming.
- **Code**:
  ```python
  print("Programming is like building a multilingual puzzle")
  ```

### 2. Formatted String with Variable
- **Filename**: `02_formatted_string.py`
- **Description**: Uses a variable in a formatted string to print a sentence.
- **Code**:
  ```python
  number = 98
  print(f"{number} Battery street")
  ```

### 3. Floating Point Precision
- **Filename**: `03_float_precision.py`
- **Description**: Demonstrates formatting a floating-point number to two decimal places.
- **Code**:
  ```python
  number = 3.14159
  print(f"Float: {number:.2f}")
  ```

### 4. String Concatenation
- **Filename**: `04_string_concatenation.py`
- **Description**: Concatenates two strings and prints them.
- **Code**:
  ```python
  str1 = "Holberton"
  str2 = "School"
  HS = str1 + str2
  print(f"Welcome to {HS}!")
  ```

### 5. String Slicing
- **Filename**: `05_string_slicing.py`
- **Description**: Illustrates string slicing to extract different parts of a string.
- **Code**:
  ```python
  word = "Holberton"
  word_first = word[:3]
  word_last = word[-2:]
  middle_word = word[1:-1]
  print(f"First 3 letters: {word_first}")
  print(f"Last 2 letters: {word_last}")
  print(f"Middle word: {middle_word}")
  ```

### 6. String Replacement
- **Filename**: `06_string_replacement.py`
- **Description**: Demonstrates string replacement.
- **Code**:
  ```python
  str = "Python is an interpreted, interactive, object-oriented programming  language that combines remarkable power with very clear syntax"
  NewStr = str.replace(f"{str}", "object-oriented programming with Python",)
  print(NewStr)
  ```

### 7. Zen of Python
- **Filename**: `07_zen_of_python.py`
- **Description**: Imports and prints the Zen of Python.
- **Code**:
  ```python
  import this
  ```
