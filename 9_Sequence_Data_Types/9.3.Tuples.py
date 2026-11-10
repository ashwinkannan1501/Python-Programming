"""
Tuples : 
A tuple data type is an immutable ordered collection
Once created , elements can't be added , removed or re-assigned
Tuple data type can be created using either () symbol or tuple() object conversion 
"""
# Syntax and Declaration : 
empty_tuple = tuple() # Declaring empty tuple
print(f"Empty tuple : {empty_tuple}")
print(f'Type of {empty_tuple} is : {type(empty_tuple)}')
no_paranthesis = 1, 4, 6 # Paranthesis is optional
print(f'No Paranthesis Tuple : {no_paranthesis}')
print(f'Data Type of {no_paranthesis} is : {type(no_paranthesis)}')
item = (56) # Since there is no comma on end , python will treat as expression , not as tuple (even though paranthesis are present)
print(f'Value : {item} - Data Type of {item} : {type(item)}')
single_item = (56,) 
print(f'Value : {single_item} - Data Type of {single_item} : {type(single_item)}') # Since comma is presented at trial end , python will treat as tuple , not as expression

# Tuple Unpacking 
packed_tuple = (89, 78, 65, 88, 65)
print(f'Packed Tuple : {packed_tuple}')
print(f'Type of {packed_tuple} is : {type(packed_tuple)}')
(x, y, z, a, b) = packed_tuple # unpacking the packed tuple and assigns to 3 different variable
print(f"Value : {(x, y, z)} , Type : {type((x, y, z))} ") # Data Type : tuple
print(f'x : {x}, y : {y} , z : {z}')
print(f"Type of {x} : {type(x)} , Type of {y} : {type(y)} , Type of {z} is : {type(z)}")

# Starred Expression (*) for remaining items 
x, *y, z = (67, 89, 78, 234.67, "Ashwin Kannan", 56+90J) # the starred expression stored multiple items as lists
print(f'X : {x} , y : {y}, z : {z}')
print(f'Type of {x} is : {type(x)}')
print(f'Type of {y} is : {type(y)}')
print(f'Type of {z} is : {type(z)}')

# Tuple Methods
# 1. count(x) method : It counts the no of same item provided in the argument,  presented in the tuple
print(f'No of times 65 appears : {packed_tuple.count(65)}')
print(f'Index of 65 is : {packed_tuple.index(65)}') # Returns the 1st index of the arg in tuple elementsf


