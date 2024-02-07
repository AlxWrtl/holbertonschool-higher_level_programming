
# Python Rectangle Class Project

## Overview

This project involves the development of a `Rectangle` class in Python, introduced and expanded through a series of enhancements across multiple script files. Starting with a basic class definition, the project iteratively adds functionality, including dimensions management, area and perimeter calculations, string representation for printing, and more advanced features like class methods and special methods.

## Files Description

- **0-rectangle.py**: Introduces the `Rectangle` class with no properties or methods.
- **1-rectangle.py**: Adds private instance attributes `width` and `height` with basic setters and getters.
- **2-rectangle.py**: Enhances the class with methods to calculate the area and perimeter.
- **3-rectangle.py**: Implements the `__str__` method for a string representation of the rectangle using "#" symbols.
- **4-rectangle.py**: Introduces the `__repr__` method for an official string representation capable of recreating a `Rectangle` instance.
- **5-rectangle.py**: Adds a custom destructor method that prints a message upon an instance's deletion.
- **6-rectangle.py**: Tracks the number of `Rectangle` instances and updates this count appropriately.
- **7-rectangle.py**: Allows customization of the string representation symbol through a class variable `print_symbol`.
- **8-rectangle.py**: Introduces a static method `bigger_or_equal` to compare the area of two rectangles.
- **9-rectangle.py**: Adds a class method `square` that returns a new `Rectangle` instance with equal width and height, representing a square.

## Key Concepts

- **Encapsulation**: The use of private attributes and property decorators to control access to `width` and `height`.
- **Data Validation**: Ensuring `width` and `height` are non-negative integers through setters.
- **Special Methods**: Utilizing `__str__`, `__repr__`, and `__del__` for string representation, instance recreation, and custom deletion behavior.
- **Class Methods and Static Methods**: Leveraging class-level operations to manipulate class variables and provide utility functions.

## Usage

To use the `Rectangle` class, create an instance by specifying the `width` and `height`:

```python
my_rectangle = Rectangle(2, 4)
```

You can then access its properties, calculate the area and perimeter, and print the rectangle:

```python
print(f"Area: {my_rectangle.area()}")
print(f"Perimeter: {my_rectangle.perimeter()}")
print(my_rectangle)
```

## Enhancements

Future enhancements could include methods for collision detection between rectangles, integration with graphical libraries for drawing rectangles on a screen, and performance optimizations for large-scale geometric computations.
