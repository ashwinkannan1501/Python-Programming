"""
Dictionary Data Type : 
------------------------
A Dictionary data type is a mapping object
A Mapping Object in python maps hashable values (keys) to arbitary objects (values)
Python has 1 primary built-in mapping type : 'dict' - Dictionary

Dictionaries are : 
1. Key - Value Pairs : Each and every entry associates with a key and a value pair separated by : (key:value)
2. Mutable : Keys can be added, updated or removed in place.
3. Insertion Ordered: Since Python 3.7+, dictionaries guarantee the preservation of insertion order.
4. Fast Lookups: Implemented using open-addressing hash tables, providing average-case O(1) time complexity for lookup, insertion, and deletion.

1. Key Rule : keys must be hashable 
------------------------------------
For an object to be a dictionary key , it must be hashable
-> Its hash value must never change during its lifetime (implements __hash__()).
-> It can be compared to other objects (implements __eq__()).
-> Valid keys (Immutable): int, float, str, tuple (only if all elements within the tuple are also hashable), frozenset, bool.
-> Invalid keys (Mutable): list, dict, set.
"""

# Valid Dictionary Keys : 
data_type_items = {
    1 : "Integer Key",
    5.78 : "Floating Key",
    3+7J : "Complex Key",
    "Ashwin Kannan" : "String Key",
    (2345, 7890, 567) : "Tuple Key",
    #{345, 678, 345} : "set key" # TypeError : set is not hashable and also mutable 

}

print(f'The Valid Dictionary Keys are : \n {data_type_items}')
print(f'Data Type : {type(data_type_items)}')

# Syntax and Declaration : 
# 1. Creating using {} (most common)
candidate = {
    "Name" : "Ashwin Kannan",
    "Age" : 25,
    "Gender" : "Male",
    "Role" : "Software Engineer"
}
# 2. using dict() method : 
url_config = dict(host="localhost",
                  port=8000,
                  debug=True)
print(f'URL Information : \n{url_config}')
print(f'Data Type : {type(url_config)}')

# 3. creating dictionary using a list of key-value tuples
key_value_pair = [(1, "One"), (2, "Two"), (3, "Three")]
dictionary = dict(key_value_pair)
print(f'Dictionary Items : \n{dictionary}')

# 4. Dictionary Comprehension
squares = {x:x**2 for x in range(1,11,1)}
print(f'Squares : \n{squares}')

# 5. Empty Dictionary
empty1 = {}
empty2 = dict()
print(f'Empty Dict 1 : {empty1}\nEmpty Dict 2 : {empty2}')

# Accessing and Modifying Elements : 
1. 
