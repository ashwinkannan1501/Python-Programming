"""
None Data Type : 
In Python , None is a built-in constant representing an intentional absence of a value or a null value. It is a sole instance of it's own dedicated data type 'NoneType'

Unlike 0, False or "" - which all represents concrete value of their respective types - None explicitly signifies that no values has been assigned or returned

Syntax : 
None is reserved and case sensitive keyword in python
None is implemented as a Singleton in python. Only one None Object exists in memory throughout execution of program
Every variable assigned None , points to the same memory address 
"""
none1 = None
none2 = None

print(f'Value of None 1 : {none1}')
print(f'Value of None 2 : {none2}')

print(f'memory of none1 : {id(none1)}')
print(f'memory of none2 : {id(none2)}')

# is keyword is safer for comparison instead of == operator
print(f'Is none1 and none2 are same : {none1 is none2}')

# None is always expressed as Falsy value
print(bool(none2)) # False

if (None is None):
    print(True)
else:
    print(False)