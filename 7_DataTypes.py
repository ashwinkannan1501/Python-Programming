"""
Data Types : 
In python , every value has a data type, which tells the interpreter how the data is intended to be used, how it is stored in memory and what operations can be performed on it.

Python is dynamically typed, means that you don't need to declare variable types explicitly.
Python Infers the data type automatically at runtime based on assigned values

1. Python Data Types in brief : 
Python's built in data types are categorized into 7 main types :
i. Numeric Data Type:
ii. Sequence Data Type:
iii. Mapping Data Type:
iv. Set Data Type
v. Boolean Data Type : 
vi. Binary Data Type 
vii None Type 


                          ┌───────────────────────────┐
                          │     Python Data Types     │
                          └─────────────┬─────────────┘
                                        │
     ┌──────────┬──────────┬────────────┼────────────┬──────────┬──────────┐
     ▼          ▼          ▼            ▼            ▼          ▼          ▼
  Numeric    Sequence   Mapping        Set        Boolean    Binary     NoneType
  ├── int    ├── str    └── dict     ├── set      └── bool   ├── bytes     └── None
  ├── float  ├── list                └── frozenset           ├── bytearray
  └── complex├── tuple                                       └── memoryview
             └── range

Classification by Mutability : 
-------------------------------
Data Types are fundamentally categorized into 2 operational behaviours
i. Mutable : Can be classified in place after creation : Eg. list, set, dict, bytearray
ii. Immutable : Cannot be modified after creation. It will create a new object : eg. int, float, complex, str, tuple, range, frozenset, bool, bytes, NoneType
"""


# Detailed Breakdown of Python Data Types : 
# -----------------------------------------
# A. Numeric Data Type :
# Used to hold numeric values. Python automatically handles precisionn for large numbers

# Integer : whole numbers without decimnal points (Positive, negative or Zero). Python Integers have arbitary precision (unlimited length). 
whole_number = 28
print(f"Whole Nummber : {whole_number}")
print(f"Type of {whole_number} : {type(whole_number)}")

negative_whole_number  = -789
print(f"Negative Whole Nummber : {negative_whole_number}")
print(f"Type of {negative_whole_number} : {type(negative_whole_number)}")

large_whole_number = 12345678901234567890
print(f"Large Whole Nummber : {large_whole_number}")
print(f"Type of {large_whole_number} : {type(large_whole_number)}")

#Floating number (float) : Real Numbers containing a decimal point or representing using a exponential notation.
# The Exponential notation is used to represent very large or very small numbers. It is represented as a number followed by 'e' or 'E' and an integer exponent.  
decimal_number = 89.567
print(f"Decimal Number : {decimal_number}")
print(f"Type of {decimal_number} : {type(decimal_number)}")
exponential_notation = 67.67e4 # 67.67 * 10^4 = 676700.0
print(f"Exponential Notation : {exponential_notation}")
print(f"Type of {exponential_notation}: {type(exponential_notation)}")

# Complex Number (complex) : Numbers with real part and imaginary part.
# The Imaginary part is represented using 'j' or 'J' after the number.
complex_number = 89 + 789j
print(f"Complex Number : {complex_number}")
print(f"Type of {complex_number} : {type(complex_number)}")
print(f"Real part of {complex_number} : {complex_number.real}")
print(f"Imaginary part of {complex_number} : {complex_number.imag}")

# B. Sequence Data Type :
# It's a ordered collection of items , where each individual item can be accessed using its index (Starting from 0 to n-1).
# 1. String :
# A string , referrred as 'str' , an immutable sequence of unicode characters, enclosed in '', "", """""" quotes
# 
single_line_str = "Hello There!. I'm Ashwin Kannan, Software Engineer & DevOps Engineer 😀"
multi_line_str = """
Hello There!
I'm Ashwin Kannan, Software Engineer & DevOps Engineer 😀
Nice to meet you all. 
Have a great day ahead.
""" 
print(f"Single Line String : {single_line_str}")
print(f"Type of single_line_str : {type(single_line_str)}")
print(f"Multi Line String : {multi_line_str}")
print(f"Type of multi_line_str : {type(multi_line_str)}")

print(f"3rd charcter of single_line_str : {single_line_str[2]}")
print(f"5th index character of multi_line_str : {multi_line_str[5]}")
print(f"1 to 6 index characters of single_line_str : {single_line_str[1:7]}")

# single_line_str [8] = "T" # Returns an Error
#print(f"Modified single_line_str : {single_line_str}")

# 2. List : A Mutable , ordered collection of heterogeneous items (can hold mixed data typpes), enclosed in [] brackets.
lists = [234, 67.89, "Ashwin Kannan", False, None, 678+89j, ["Apple", "Orange"], {"Apple", "Banana", "Orange"},   {"Name" : "Ashwin kannan", "Age" : 25, "Occupation" : "Software Engineer"}]
print(f"List : {lists}")
lists[1] = 34.678 # Lists are mutable, so we can modify the values in place
print(f"Modified List : {lists}")
print("Type of lists : ", type(lists))
print(f"3rd item of lists : {lists[2]}")
print(f"1 to 4 index items of lists : {lists[1:5]}")
print(f"Last item of lists : {lists[-1]}")
print(f"8th element of lists :{lists[7]}")
print(f"Type of 8th element of lists : {type(lists[7])}")

# 3. Tuple : An Immutable , ordered collection of heterogeneous items (can hold mixed data types), enclosed in () brackets. 
# once created , the elements cannoty be added , removed or changed.
tuples = (67, 890.67, "Ashwin Kannan", True)
print(f'Tuple Items : {tuples}')
print(f'Type of {tuples} : type(tuples)')

# tuples[2] = "Kannan Arumugam" # Returns an Error
# print(f'Modified Typle Items : {tuples}')

# Range : An immutable sequence of numbers commonly used for looping a specific number of times in for loops. It is represented using the range() function.
# Syntax : range(start , [stop] , [step])
numbers = range(1, 20, 3)
print(f"Range of Numbers : {list(numbers)}")

# C. Boolean Data Type :
# 1. boolean : 'bool' data type represents one of two values. 
# Internally in python, 'bool' is a sub-class of int where True = 1 and False = 0.
is_active = True
has_permission = False
print(f"Is Active : {is_active}") # returns True
print(f"Has Permission : {has_permission}") # Returns False
print(5 > 3) # Returns True
print(10 < 10) # Returns False
print(bool("")) # Returns False (Empty string evaluates to False)
print(bool(765)) # Returns True (Non-zero numbers evaluates to True)
# print(100) # Returns 100

# D. None Type : None : It represents the intentional absence of a value
# Returned by functions that do not explicitly returns a value. 
none_value = None
print(f"None Value : {none_value}")
print(f"Type of {none_value} : {type(none_value)}")

# E. Mapping Type : 
# 1. Dictionary : 'dict' kewyword , A mutable collection of key-value pairs, enclosed in {} brackets
# Keys must be unique and immutable , while values can be of any type
staff = {
    "Name" : "Ashwin Kannan",
    "Age" : 25,
    "Degree" : "B.E CSE",
    "College" : "Panimalar Engineering College",
    "Skills" : ["Python", "Java", "Data Science" , "DevOps", "Cloud Computing"],
    "Experience" : 3,
    "Occupation" : "Software Engineer"

}
print(f"Staff Dictionary : {staff}")
print(f"Data Type : {type(staff)}") # Prints the Data Type of Staff Dictionary
staff["Experience"] = 2.9 # modify the existing key-value pair
staff["CGPA"] = 9.9 # Add a new key-value pair to the end of dictionary
print(f"Staff Details : {staff}")
print(f'staff name : {staff["Name"]}') # Prints the value of the key "Name" in the dictionary

# F. Set Types : Unordered collections of unique elements. Sets automatically eliminate duplicates
# 1. Set : 'set' keyword. Unordered collection of unique mutable elements, enclosed in {} brackets.
# Automatically eliminates duplicate values and does not maintain the order of elements.
language_set = {"Python", "Java", "C++", "JavaScript", "Python", "C++"}
print(f"Language Set : {language_set}")
print(f"Type of language_set : {type(language_set)}")
language_set.add("Go") # Add a new element to the set
print(f"Modified Language Set : {language_set}")
#print(f"{language_set[1]}") # returns Error 
#language_set[2] = "Rust" # returns Error, as sets are unordered and do not support indexing

# 2. Frozen Set : 
# An immutable version of a set. 
# Because it is immutable , a frozenset can be used as a dictionary key or an element inside another element.
name_list = ["Ashwin", "Kannan", "Amutha"]
immutable_set = frozenset(name_list)
print(f'Frozen Set : {immutable_set}')
print(f'Type of immutable set : {type(immutable_set)}')
# immutable_set.remove("Ashwin") # returns an attribute Error

# G. Binary Types : 
# Used to handle raw binary data (like images, sound files, network sockets, or crypto operations).
# 1. Bytes : An immutable sequence of single bytes (integers from 0–255).
binary_data = b"Hello"
print(binary_data[0])  # Output: 72 (ASCII code for 'H')

# 2. bytearray : A mutable sequence of bytes
mutable_bytes = bytearray(b"Hello")
mutable_bytes[0] = 74  # Replace 'H' with 'J' (ASCII 74)
print(mutable_bytes)   # bytearray(b'Jello')

# 3. memory view : A buffer protocol object that allows python code to access the internal data of an object that supports the buffer protocol without making a copy.
data = bytearray(b"Python")
view = memoryview(data)
print(view[0])  # 80 ('P')
