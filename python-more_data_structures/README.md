
# Python Higher-level Programming Project

## Overview

This project consists of Python scripts that demonstrate the use of higher-level programming techniques, including list comprehensions, map, lambda functions, set operations, and dictionary manipulations.

## Scripts Description

### 1. Square Matrix Simple

- **Filename**: `0-square_matrix_simple.py`
- **Description**: Computes the square value of all integers of a matrix using list comprehension.
- **Code Snippet**:

  ```python
  def square_matrix_simple(matrix=[]):
      return [list(map(lambda element: element**2, row)) for row in matrix]
  ```

### 2. Search and Replace

- **Filename**: `1-search_replace.py`
- **Description**: Replaces all occurrences of an element by another in a new list.
- **Code Snippet**:

  ```python
  def search_replace(my_list, search, replace):
      return list(map(lambda elm: replace if elm == search else elm, my_list))
  ```

### 3. Unique Addition

- **Filename**: `2-uniq_add.py`
- **Description**: Adds all unique integers in a list (only once for each integer).
- **Code Snippet**:

  ```python
  def uniq_add(my_list=[]):
      return sum(set(my_list))
  ```

### 4. Common Elements

- **Filename**: `3-common_elements.py`
- **Description**: Returns a set of common elements in two sets.
- **Code Snippet**:

  ```python
  def common_elements(set_1, set_2):
      return set([element for element in set_1 if element in set_2])
  ```

### 5. Only Different Elements

- **Filename**: `4-only_diff_elements.py`
- **Description**: Returns a set of all elements present in only one set.
- **Code Snippet**:

  ```python
  def only_diff_elements(set_1, set_2):
      return set_1 ^ set_2
  ```

### 6. Number of Keys

- **Filename**: `5-number_keys.py`
- **Description**: Returns the number of keys in a dictionary.
- **Code Snippet**:

  ```python
  def number_keys(a_dictionary):
      return len(a_dictionary)
  ```

### 7. Print Sorted Dictionary

- **Filename**: `6-print_sorted_dictionary.py`
- **Description**: Prints a dictionary by ordered keys.
- **Code Snippet**:

  ```python
  def print_sorted_dictionary(a_dictionary):
      # ... function logic ...
  ```

### 8. Update Dictionary

- **Filename**: `7-update_dictionary.py`
- **Description**: Replaces or adds key/value in a dictionary.
- **Code Snippet**:

  ```python
  def update_dictionary(a_dictionary, key, value):
      # ... function logic ...
  ```

### 9. Simple Delete by Key

- **Filename**: `8-simple_delete.py`
- **Description**: Deletes a key in a dictionary.
- **Code Snippet**:

  ```python
  def simple_delete(a_dictionary, key=""):
      # ... function logic ...
  ```

### 10. Multiply by 2

- **Filename**: `9-multiply_by_2.py`
- **Description**: Returns a new dictionary with all values multiplied by 2.
- **Code Snippet**:

  ```python
  def multiply_by_2(a_dictionary):
      # ... function logic ...
  ```

### 11. Best Score

- **Filename**: `10-best_score.py`
- **Description**: Returns a key with the biggest integer value.
- **Code Snippet**:

  ```python
  def best_score(a_dictionary):
      # ... function logic ...
  ```

### 12. Multiply List Map

- **Filename**: `11-multiply_list_map.py`
- **Description**: Returns a list with all values multiplied by a number without using any loops.
- **Code Snippet**:

  ```python
  def multiply_list_map(my_list=[], number=0):
      return list(map(lambda mult: mult * number, my_list))
  ```

## Contributing

Contributions, suggestions, and improvements are welcome to enhance the functionality of these scripts.

## License

[Specify License Here]

## Authors

- [Your Name]

---
For more information or questions, contact [Your Contact Information].
