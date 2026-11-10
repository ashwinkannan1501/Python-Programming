#input() function :

"""
Getting input from the user
---------------------------
The input() function is used to get the input from the user and continue executes the remaining program
It pauses the program execution and waits for the user to type the text into the terminal / console. After user types the input and press the "enter" button, the rest of the program continue execution

SYNTAX : 
--------
---------------------------------
| user_response = input(prompt) |
---------------------------------

'prompt' - This is optional. It is the string displayed to the user before waiting for the input
Eg. "Enter your name : "

Key Rule : It always returns a string value
	   Regardless of what user types (numbers, letters, symbols), the input() function always returns a string


Type casting : 
---------------
Since input() function returns a string, we must explicitly converts (typecast) the input, specifically if you want to perform math, comparison or logical operations.

Eg. age = int(input("Enter your age : ")) # gets the user age as input and converts into integer data type and store the value into the "age" variable
"""

# Basic Details getting from user
print("------------------ Getting Basic Information from User ------------------")

first_name = input("Enter your first name : ")
print(f'Data Type of first_name : {type(first_name)}')

last_name = input("Enter your last name : ")

age = int(input("Enter your age : "))
print("Data Type of age : {type(age)}")

dob = input("Enter your Date of Birth : ")
designation = input("Enter your designation : ")
country = input("Enter your country name : ")
state = input(f"Which state of {country} you're from ? : ")
city = input(f"Which city of {state}, {country} you're from ? : ")

# Printing details , entered by the user , onto the screen
print("\n------------------ Printing user Details-----------------------")
print(f"First Name : {first_name}")
print(f"Last Name : {last_name}")
print(f"Age : {age}")
print(f"Date of Birth : {dob}")
print(f"Designation : {designation}")
print(f"Your're coming from {country}, {state}, {city}")


"""
Tricks for handling multiple inputs : 
------------------------------------
Often, we want users to enter multiple data points on a single line (like entering co-ordinates or sequence of numbers)
"""

print("\n -------------------- Handling Multiple Inputs-----------------")
x, y = map(float, input("Enter the X, Y coordinates : ").split(","))
print(f'Points of Interaction Coordinates of {x}, {y} is : {x * y}')


 
