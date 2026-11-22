"""
Set Data Type : 
----------------
A Set in python is a unique, unordered collection of hashable elements. Python provides 2 built-in set types

I. Set : Mutable : Elements can be added or removed after creation. Because it's mutable , the set is unhashable
II. Frozenset : Immutable : Elements cannot be changed after creation. Because it's immutable , frozenset is hashable
Internally both types are backed by hash tables

1. Core Rules and Hashability : 
No Duplicates : Duplicate values are automatically discarded upon creation or insertion
Unordered (No Indexing or Slicing) : Sets do not preserve insertion order and do not support positional access like 'sets[0]'
Elements must be hashable : Every item inside a set must be immutable/hashable . Mutable objects cannot be element of a set

"""

# Eliminates duplicates 
element = {23, 87623, 78.89, 90+56J, 23} # set automatically removes the duplicate values
print(f'Set Element : {element}')

# valid hashable items
sets = {"Ashwin", 67.89, 89-67J, 3342, ("Apple", "Mango", "Orange"), frozenset(["Push","Pull","Legs"])}
print(f'Set Values : {sets}')
print(f'Type : {type(sets)}')

# Invalid UnHashable Set Elements : 
# invalid = {34, 90, ["Ashwin", "Kannan"]} 

# Index will not work
# print(set[3]) # Since set are unordered , can't use indexing 

# Note : On 1, True, 0 , False . boolean is a subclass of int (1 == True , 0 == False) and they share identical hashes. A set treats 1 and True , 0 and False
boolean_set= {1, True, 0, False}
print(f'Set values : {boolean_set}')

# Set : Syntax and Creation : 
# 1. Curly Brace Literals ("{}") - Automatically removes the duplicate elements
unique_fruits = {"Apple", "Banana", "Orange", "Grapes", "Banana", "Kiwi", "Apple"}
print(f'Unique Fruits : {unique_fruits}')
print(f'Type of Unique Fruit : {type(unique_fruits)}')

# 2. Using 'set()' constructor from any iterable - Automatically removes the duplicate elements
phone_list = {"Apple", "Samsung", "Huawei", "Poco", "Google", "Apple", "Google", "Huawei"}
unique_phones = set(phone_list)
print(f'Unique Phones : {unique_phones}')
print(f'Type of Unique Phones : {type(unique_phones)}')

# 3. Empty Sets (Critical Pitfall)
empty_set = set() # Empty set can only be created using 'set()' constructor, not with '{}' -> It is the symbol for empty dictionary
# empty_set = {} -> Not a set , it is the syntax for empty dictionary

# Set Manipulation : Because set is mutable, it provides dedicated methods for adding, removing and copying elements
# Adding Elements 
# 1. add(element) - the add() method adds the single hashable elemnet to the set . Does nothing if the element already exists. It takes only one argument at a time at any hashable data type
unique_phones.add("Xiaomi")
element.add(92834759827345)
print(f'Modified Unique Phones : {unique_phones}')
print(f'Modified Element : {element}')
# 2. update(*elements) - Adds all element from one or more iterables(list, tuples, strings and other sets) into the sets in place
phone_brands1 = ["Motorola", "FreedomPhone1", "Honor", "Motorola"]
phone_brands2 = ["Lava", "Infinix", "Redmi", "OnePlus", "Oppo", "Vivo", "Oppo", "Samsung"]
unique_phones.update(phone_brands1, phone_brands2)
print(f'Unique Phopne Brands are : {unique_phones}')

# Removing Elements
unique_phones.remove("Motorola")
print(f'Modifed Phone Brands : {unique_phones}')
#unique_phones.remove("MyPhoneBrand")
#print(f'Modified Phone Brands : {unique_phones}') # Raise Key Error since the provided argument value doesn't proivided in sets
unique_phones.discard("FreedomPhone1") # It removes the element provided in the arguments if founds in set
print(f'Modifed Phone Brands : {unique_phones}')
unique_phones.discard("IQOO") # If the provided argument element not found , no erros will be raised and no modification of elements will be occurred. It is safe to use
print(f'Modifed Phone Brands : {unique_phones}')
popped_element = unique_phones.pop() # the 'pop()' method removes and returns the arbitaray/random element. Raise 'KeyError' if set ios empty
print(f'The Popped element is : {popped_element}')
print(f'Modifed Phone Brands : {unique_phones}')
copy_set = unique_phones.copy() # Returns the shallow copy of the set. Since the memory reference is not same for both . Modification of one set doesn't affect the other set
print(f'Phone Brands : {unique_phones}')
print(f'Memory Reference of Unique Phones : {id(unique_phones)}')
print(f'Set Copy : {copy_set}')
print(f'Memory Reference of Copy Set : {id(copy_set)}')
print(f'Popped Element : {copy_set.pop()}')
print(f'Shallow Copied Set : {copy_set}') # Modification of one set
print(f'Phone Brands : {unique_phones}') # Doesn't affect the other set

sets.clear()
print(f'Modified Elements of Sets : {sets}')

# Immutable Set : Frozen Set : A frozenset is the immutable counterpart to set. Once created it's content are locked for it's entire lifetime

# Syntax : created using 'frozenset()' constructor
company  = {"Google", "Microsoft", "Apple", "Salesforce", "Meta"}
immutable_set = frozenset(company)
empty_frozenset = frozenset()

# Frozenset are immutable . i.e not changable after creation
# empty_frozenset.add("Ashwin") # raises attribute error 

"""
Why We need to use frozensets : 
1 : As a Dictionary Key : 
2. Nested Sets
3. Write Safe Constants
"""
# 1. As a Dictionary Key
# Undirected edge weights: {A, B} is the same key as {B, A}
edge_weights = {
    frozenset({"Mumbai", "Pune"}): 150,
    frozenset({"Pune", "Nashik"}): 210
}
print('As a Dictionary key : ', edge_weights[frozenset({"Pune", "Mumbai"})])  # 150

# 2. Nested Sets
matrix_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print('Nested Sets : ', matrix_of_sets)  # {frozenset({1, 2}), frozenset({3, 4})}