"""
Boolean Data Type : 
-------------------
In python , the boolean data type (bool) represents truth values and can hold one of the 2 built-in constants 
1. True (or)
2. False
Booleans are the foundations of decision making, control flow (if/while) and logical reasoning in python

Syntax & Internal Architecture : 
---------------------------------
In Python , 'True' and 'False' are case sensitive keywords
Means , True and False are technically specialixed integers where True == 1 & False == 0
"""

is_valid = True
is_empty = False
print(is_valid , is_empty)
print(type(is_valid), type(is_empty))
print(f'True = 1 : {True == 1}')
print(f'False = 0 {False == 0}')
print(f'True = 0 : {True == 0}')

# Arithmentic Oprations with Booleans
print(f'True + True = {True + True}') # Output 2 (1+1 = 2)
print(f'False + False = {False + False}') # Output : 0 (0+0=0)
print(f'True + False = {True + False}') # Output : 1 (1+0=1)

"""
2. bool() function (truth and False):
Every object ion python can be evaluated for truth value testing in an if/while condition or explicitly converted using the built-in bool() constructor

Falsy Values : Evaluated to False:
----------------------------------
By default , an object is considered as falsy if it represents no value or 0 value or null value
-> Constants : False , NULL
-> Numeric ZEROS : 0 , 0.0, 0J, Decimal(0)
-> Empty Sequences : [], "", (), set(), {}, range(0)
"""
# Falsy Examples
print(bool(0)) # Output : False
print(bool("")) # Output : False
print(bool([])) # Output : False
print(bool(())) # Output : False
print(bool(set())) # Output : False
print(bool({})) # Output : False
print(bool(None)) # Output : False

"""
Truth Value : Evaluates to true : 
----------------------------------
-> Non-zero numbers (1, -5, 0.001)
-> Non-empty sequences/collections ("False", [0], {"a": None})
-> Custom objects (unless their __bool__() or __len__() method returns False or 0)
"""

# Truth Examples
print(bool(1)) # Output : True
print(bool(-8.9)) # Output : True
print(bool(" ")) # Output : True
print(bool([""])) # Output : True
print(bool(("",))) # Output : True
print(bool({"":""})) # Output : True
print(bool(set(" "))) # Output : True

# Comparison Operators : compared the given 2 or more values and either returns True or false
print({45 == 67})
print(67 != 67)
print(45 > 89)
print(34 < 10)
print(34 >= 23)
print(45 <= 67)
print(45 is 45)
print(34 is not 45)
string = "python"
print('p' in string)
print('q' not in string)
print(5 < 8 < 123) # True (Chained Comparison)

print(True and False) # Output : False
print(True or False) # Output : True

print(any([45, '', 78])) # any() method is like 'or' operator in iterables
print(all([45, '', 78])) # all() method is like 'and' operator in iterables