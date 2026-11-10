"""
Lists : 
A List is an ordered collection of items , which are mutable objects.
It can contain elements of different data types like integers, strings, floats, etc.
A lists is enclosed within "[]" or lists() data type converter.
"""

# Syntax & Declaration : 
empty_lists = []
integer_lists = [10, 67, 9, 0, 789]
mixed_lists = [10, 45,89, -67, -45.67, False, "Ashwin Kannan", (67, 90), ["Apple", "Banana", "Mango"], {567, 890, 567, 23}, {"Name" : "Ashwin Kannan", "Age": 25, "Gender": "Male"}, None, 67+89j]
print(f'Empty Lists : {empty_lists}')
print(f'Type of Empty Lists : {type(empty_lists)}')
print(f'Integer Lists : {integer_lists}')
print(f'Mixed Lists : {mixed_lists}')

# Mutability of Lists :
print(f'Before Modification : {integer_lists}')
# integer_lists[5] = 10000 # Throws IndexError : List assignment index out of range since the index 5 is not present in the list
# integer_lists[7] = 0000 # Throws IndexError : List assignment index out of range since the index 7 is not present in the list
integer_lists[3] = 656765
print(f'After Modification : {integer_lists}')
print(f"Before Modification of mixed lists: {mixed_lists}")
mixed_lists[3:5] = [True, False, "Index Slicing Modification", "Day in the life of a Software Engineer in Apple", "Banana"]
print(f'After Modification of Mixed Lists : {mixed_lists}')
mixed_lists[5:8] = [] # removes the element from index 5, 6, 7 : not 8≈
print(f"New Mixed Lists after deletion of elements from [5:8] index : {mixed_lists}")


# Indepth Lists Methods : 
cars = []

# 1. Adding Elements : 
print(f'List before adding elements : {cars}')
# append() method : It adds new item to the end of the lists. It takes only one argument
cars.append("Ferrari") 
print(f'Lists After appending new element : {cars}')
# extend() method : It appends the n number of elements in the lists arguments in unpacking method in OG lists
#empty_lists.extend("BMW", "Audi") # the extend() methods takes exactly one argument
cars.extend(["BMW", "Audi", "Mercedes"])
print(f'Modified Car lists using extend() method : {cars}')
# insert(index, element) - It inserts the specific element at the specified index location
cars.insert(0, "Porsche")
print(f'After Inserting an elemnt at specified index : {cars}')

# 2. Removing Elements : 
print(f'Cars Lists : {cars}')

# pop([index]) = The pop() method generally removed the last element of the lists. Optionally we can use index argument to remove the exact element
cars.pop()
print(f'after popping last element : {cars}')
cars.pop(0)
print(f'After popping index 0 element : {cars}')

cars.append("BMW") # Appending BMW at end 
print(f'Car Lists : {cars}') # Output : Car Lists : ['Ferrari', 'BMW', 'Audi', 'BMW']
# remove(element) method : it removes the element from the lists starts from left to right. Not removed the duplicate element
cars.remove("BMW") # Removes 1st indexed element of BMW , not also 3rd indexed element
print(f'After Removing "BMW" car from the lists (not removal of duplicate element) : {cars}')

# clear() method : the clear method clears all the elements from the lists and makes it a empty lists
cars.clear()
print(f'cars lists : {cars}')

cars.extend(["Ferrari", "BMW", "Audi", "Porsche", "Tesla"])
print(f'New Car collection : {cars}')
# del keyword - Total deletion of an object
del cars[1:3] # deleting slicing index car from index 1 : 3 (exclusive of 3)
print(f'Modified Car collection : {cars}') # Output : Ferrari, Porsche, tesla
del cars # Deletes the entire car object from the memory
# print(cars) # Output : Throws Name Error

# Reordering & Sorting : 
print(f'Integer Lists : {integer_lists}')
integer_lists.reverse() # the reverse() method reverses the lists item from right to left
print(f'After Reversing the lists : {integer_lists}')
integer_lists.sort() # By Default , the sort() method , sorts the element in ascending order (lowest to highest)
print(f'After Sorting (in ascending order): {integer_lists}')
integer_lists.sort(reverse=True) # sort(reverse=True) . By turning on the reverse=True argument , it sorts the element in descending order (from highest to lowest)
print(f'After Sorting (in descending order) : {integer_lists}')

# Copying & Pitfalls
# Assigning a list variables , copies it's reference , not it's contents
bike_lists = ["KTM", "Yamaha", "Honda", "Hero", "Aprilla"]
print(f'OG bike Lists : {bike_lists}')
alias_bike_lists = bike_lists # Copying not only contents also it's memory reference (Both variables point to the same object)
print(f'Alias Bike Lists : {alias_bike_lists}')
# Changing an element in "bike_lists" (reflects in both lists)
bike_lists.remove("Yamaha")
print(f'OG Bike Lists : {bike_lists}')
print(f'Memory Locaton of "OG Bike Lists" : {id(bike_lists)}')
print(f'Copied Bike Lists : {alias_bike_lists}')
print(f'Memory location of "Alias Bike Lists " : {id(alias_bike_lists)}')

# Copying only the elements , not the memory address object
alias_copy2 = bike_lists.copy() # The copy() method , copies only the contents of the lists element , not points to same memory address
print(f'OG Bike Lists : {bike_lists}')
print(f"Memory Address of OG Bike Lists : {id(bike_lists)}")
print(f'Copy Bike Lists : {alias_copy2}')
print(f'Memory Address of Copy Bike Lists : {id(alias_copy2)}') # The 2 memory address location are different
#Changing an element in alias copy bike lists
alias_copy2[3:5] = ["Royal Enfield", "Bajaj", "BMW", "TVS"]
print(f'OG Bike Lists : {bike_lists}')
print(f'Alias Copy Bike Lists : {alias_copy2}')
