
# Python OOP Projects

This collection of Python files demonstrates various object-oriented programming concepts, ranging from basic class definitions to inheritance and polymorphism. Each file serves a specific purpose, as detailed below.

## Files Description

- **0-lookup.py**: Defines a function `lookup(obj)` that returns the list of available attributes and methods of an object.
- **1-my_list.py**: Contains a class `MyList` that inherits from `list` and has a method `print_sorted()` to print the list in ascending order.
- **2-is_same_class.py**: Defines a function `is_same_class(obj, a_class)` to check if an object is exactly an instance of a specified class.
- **3-is_kind_of_class.py**: Implements `is_kind_of_class(obj, a_class)`, determining if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class.
- **4-inherits_from.py**: Contains `inherits_from(obj, a_class)`, checking if an object is an instance of a class that inherited (directly or indirectly) from the specified class.
- **5-base_geometry.py**: Introduces an empty class `BaseGeometry`.
- **6-base_geometry.py**: Enhances `BaseGeometry` by adding a method `area()` that raises an exception with the message `area() is not implemented`.
- **7-base_geometry.py**: Extends `BaseGeometry` with `integer_validator(self, name, value)`, validating `value` as an integer greater than 0.
- **8-rectangle.py**: Defines a class `Rectangle` that inherits from `BaseGeometry` with `width` and `height` validated by `integer_validator`.
- **9-rectangle.py**: Enhances the `Rectangle` class to implement the `area()` method and `__str__` method, providing a string representation.
- **10-square.py**: Introduces a `Square` class that inherits from `Rectangle`, with a `size` attribute that's validated and used to calculate the area.
- **11-square.py**: Further refines the `Square` class to adjust its string representation format.

## Usage

Each Python file can be executed separately to test the functionalities they provide. They demonstrate fundamental and advanced concepts in object-oriented programming within Python, making them excellent resources for learning and reference.

```bash
python3 <filename>.py
```

Replace `<filename>` with the actual name of the Python file you wish to run.
