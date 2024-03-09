# variables_data_types.py
# This file contains examples of variables and data types in Python.

# Python is a dynamically typed language, which means that you do not have to declare the type of a variable when you create one.
# Python automatically assigns the data type to a variable when a value is assigned to it.
# Python has several built-in data types, which are used to store different types of data.
# The most common data types are:
# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview

# example for string
name = "John"
print(name)

# example for numeric Types: integer, float, complex
age = 30
height = 5.5
complex_number = 1j
print('age:', age, 'height:', height, 'complex_number:', complex_number)

# you can check the type of the variable using type() function
print(type(name)) # example for string

# example for boolean type
is_true = True
print(is_true)

# example for sequence types: list, tuple, range
## list is a collection which is ordered and changeable. 
my_list = [1, 2, 3]
print(my_list)
## you can change the value of the list
my_list[1] = 4
print(my_list)

## tuple is a collection which is ordered and unchangeable. 
my_tuple = (1, 2, 3)
print(my_tuple)
## you cannot change the value of the tuple
my_tuple[1] = 4 # this will give an error

## range is a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
my_range = range(6)
print(my_range) # it will print range(0, 6), which means it will start from 0 and end at 5


# example for mapping type: dict
## dictionary is a collection which is unordered, changeable and indexed.
my_dict = {"name": "John", "age": 30}
print(my_dict)
## you can change the value of the dictionary
my_dict["name"] = "David"
print(my_dict)

# example for set types: set, frozenset
## set is a collection which is unordered and unindexed.
my_set = {1, 2, 3}
print(my_set)
## you can add an item to the set
my_set.add(4)
print(my_set)

## frozenset is a collection which is unordered and unindexed. It is immutable, which means you cannot change its value.
my_frozenset = frozenset({1, 2, 3})
print(my_frozenset)
## you cannot add an item to the frozenset
my_frozenset.add(4) # this will give an error