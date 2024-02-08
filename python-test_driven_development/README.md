# Python Test Cases and Functions

## Overview

This document outlines a series of Python functions along with their test cases. The functions cover various basic operations, and the test cases demonstrate their expected usage and error handling capabilities.

### 1. Addition of Integers

- **Function**: `add_integer(a, b=98)`
- **Description**: Adds two integers or floats. Floats are converted to integers before addition.
- **Test Cases**:
  - `add_integer(10, 20)` returns `30`
  - `add_integer(-10, -20)` returns `-30`
  - `add_integer(10, 20.5)` returns `30`
  - `add_integer(10)` returns `108`
  - `add_integer(10.5, 20.5)` returns `30`
  - `add_integer("ten", 20)` raises `TypeError`
  - `add_integer(10, "twenty")` raises `TypeError`
  - `add_integer("ten", "twenty")` raises `TypeError`

### 2. Matrix Division

- **Function**: `matrix_divided(matrix, div)`
- **Description**: Divides all elements of a matrix by a divisor.
- **Test Cases**:
  - Dividing a matrix by `2` and `2.5`
  - Dividing by `0` raises `ZeroDivisionError`
  - Passing a non-number as divisor raises `TypeError`
  - Divisor less than `0` raises `ValueError`

### 3. Say My Name

- **Function**: `say_my_name(first_name, last_name="")`
- **Description**: Prints a full name.
- **Test Cases**:
  - `say_my_name("Bob")` and `say_my_name("Bob", "Smith")`
  - Passing non-strings as names raises `TypeError`

### 4. Print Square

- **Function**: `print_square(size)`
- **Description**: Prints a square of a given size using `#`.
- **Test Cases**:
  - `print_square(5)` prints a 5x5 square
  - Negative or non-integer size raises `ValueError` or `TypeError`

### 5. Text Indentation

- **Function**: `text_indentation(text)`
- **Description**: Prints text with two new lines after `.`, `?`, and `:`.
- **Test Cases**:
  - Various strings tested for proper indentation
  - Non-string input raises `TypeError`

### 6. Max Integer [Unittest]

- **Module**: `6-max_integer`
- **Description**: Unittest for the `max_integer` function to find the max integer in a list.
- **Test Scenarios**:
  - Lists with positive numbers, negative numbers, and mixed
  - Testing with no arguments, non-list arguments, and invalid list contents

## Implementation

The Python scripts implement basic functionality, error handling, and edge cases. The unittest module is used for testing the `max_integer` function, ensuring robustness against various inputs.

## Conclusion

This collection of Python functions and their test cases demonstrates fundamental programming concepts, error handling, and testing practices in Python.
