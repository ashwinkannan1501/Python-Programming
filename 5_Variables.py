"""
Variables : 
The variable is basically a strorage box, used to store value(s), which can refer it later (or) change it's data as prefer
Unlike statically typed languages like C++, Java, etc., here in python , there is no need to specify the type of the variable before assigning a value to it.

Eg. name = "Ashwin"

Conventions : 
1) Use Snake Cases (Eg. first_name)
2) Use descriptive variable names (Eg. first_name instead of fn)

How Python manages variables : 
Eg. first_name = "Ashwin"
Description : Python creates object names "Ashwin" in memory and points the variable name "first_name" into it.

Garbage Collection :
Python has an automatic garbage collection mechanism that manages memory allocation and deallocation for variables. 
Python automatically frees up memory when an object reference counts drops to 0.
"""

# Storing User Information : 
first_name = "Ashwin"
last_name = "Kannan"
age = 24
organization = "Jio Platforms Limited"
designation = "DevOps Engineer"
years_of_service = 3
date_of_joining = '2023-12-05'


# Printing the stored user information : 
print("----------------------- User DB Information -----------------------  ")
print("First Name : ", first_name)
print("Last Name : ", last_name)
print("Age : ", age)
print("Organization : ", organization)
print("Designation : ", designation)
print("Years of Service : ", years_of_service)
print("Date of Joining : ", date_of_joining)


"""
id() function : 
The id() function is used to return an object (or) reference number in memory location
Eg. id(first_name) -> Returns a long integer memory storage value
"""

# Printing the memory value 
print(f"\nMemory Value of {first_name} is : {id(first_name)}")
print(f"memory Value of {last_name} is : {id(last_name)}")

# Constants :
# Python doesn't enforce constants programatically , but use of ALL_CAPS naming conventions, to denote the values that shouldn't alter
PI = 3.1415
print(f"\nThe value of PI is : {PI}")

