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
# 1. Reading Values 
print(f'The candidate mapping value are : {candidate}')
# using square bracket lookup
print(f'Name of the Candidate : {candidate["Name"]}')
# Using .get() method [Safe to use to handle exceptions]
print(f'Age of Candidate : {candidate.get("Age")}')
print(f'Candidate Email Address : {candidate.get("Email", "Email ID not found in candidate dictionary")}') # Instead of throwing 'KeyError', it provides the default value
print(f'Email Information of the candidate : {candidate.get("Email")}') # Result : None , due to "Email" key not present
# print(f'Company Name : {candidate["company"]}') # Throws KeyError since the key 'company' not present in 'candidate' dictionary

# 2. Adding & Updating Entries (key-value pair)
candidate["Email"] = "ashwin.kannan.tech@gmail.com" # Adds new key-value pair to the end of the dictionary
candidate["Role"] = "DevOps Engineer" # Update the new value in the existing key
print(f'Updated Candidate Information : {candidate}') # Prints the updated candidate information

# Built-in dictionary methods : 
# 1. To Inspect and View Objects
keys = url_config.keys() # returns the keys of the  dictionary
print(f'Displaying all keys of URL Config : {keys}') 
print(f'Data Type : {type(keys)}') # dict_keys
values = url_config.values() # Returns the values of the dictionary
print(f'Displaying all assigned values of URL Config : {values}')
print(f'Data Type : {type(values)}') # dict_values
items = url_config.items() # Returns the items (key-value pair) of the dictionary
print(f'Displaying all the items present in URL Config : {items}')
print(f'Data Type : {type(items)}') # dict_items

# iterating the individual key-value pair using for loop
print(f'The Candidate Information is given below')
for (key, value) in candidate.items():
    print(f'{key} : {value}')

# Mutation and Extraction methods
tuple_key = (2345, 7890, 567)
# pop(key, [default]) : 'default' is optional. the 'pop()' method removes the key and returns it's value. Returns 'KeyError' if key is not found and no default is provided
popped_value = data_type_items.pop(tuple_key, str(tuple_key)+"not in dictionary") 
print(f'The Popped Element is : {popped_value}')
print(f'Updated Data Type Items : {data_type_items}')

#popitem() method : Removes and returns the last inserted item (key-value pair) in LIFO order. Raises 'KeyError' on an empty dictionary
data_type_items.popitem()
print(f'Updated Data Type Item is : {data_type_items.items()}')
# empty1.popitem() # Throws KeyError since they are no items to pop out

# clear() method : Removes all elements from the dictionary
data_type_items.clear()
print(f'Data Type Item elements : {data_type_items}')
# Removing specific item Using del keyword
del url_config["debug"]
print(f'Updated URL Config : {url_config}')

del empty1 # deletes the specific key or an entire dictionary
# print(empty1) # Throws NameError due to deletion of varible

# Updating & Merging Methods : 
default_settings = {'theme':'light', 'notification':True}
user_settings = {'theme':'dark', 'volume':90}
default_settings.update(user_settings) # The update() method updates the dictionary with elements from another dictionaryor iterable of key/value pairs. It Overwrites any existing keys
print(f'The Base Setting is : {default_settings}')
print(f'User Settings is : {user_settings}')

# | -> Merge Operator : Creates a new dictionary. It is used for merging dictionaries cleanly. Introduced in Python 3.9
merged_settings = default_settings | user_settings
print(f'Merged Setting is : {merged_settings}')
# Another way of utilizing 'update()' method using merge (|) operator
default_settings |= user_settings
print(f'Default Settings : {default_settings}')
print(f'User Settings : {user_settings}')

# Initialization & Default Handling
triathlon_tracker = {'swim(in km)' : 3, 'cycling (in km)' : 40, 'running (in km)' : 21}
print(f'Triathlon tracker : {triathlon_tracker}')
# setdefault(key, [default]) : Returns the 'key' if it's exists. If not , inserts key with provided defualt value and returns the default value 
swim_record = triathlon_tracker.setdefault('swim(in km)', 0)
cycling_record = triathlon_tracker.setdefault('cycling (in km)', 0)
running_record = triathlon_tracker.setdefault('running (in km)', 0)
jogging_record = triathlon_tracker.setdefault('jogging (in km)', 0)
print(f'Swim Record : {swim_record}\nCycling Record : {cycling_record}\nRunning Record : {running_record}\nJogging Record : {jogging_record}')

#fromkeys(iterable , [value]) method : It creates new dictionary with keys from an iterable and values set to 'values' (Defualts to None)
user_status = {'Ashwin':'offline', 'Kannan':'offline', 'Sandeep':'offline'}
presence = user_settings.fromkeys(user_status.keys(), 'Online')
print(f'New User Status : {presence}')

