"""
Conditional Statements : 
-------------------------
The Conditional Statement in python , controls the flow of execution by evaluating boolean expression (True or False) and running specific block of code based on the outcome

Unlike other langugaes suvch as C, Java, C++ or JS that uses {} & (), python relies strictly on colon(:) & Indentation (standardly 4 spaces to define code blocks)
"""

"""
1) The if statemennt : 
-----------------------
The if statement is the most fundamental decision making structure. It executes a block of code only if the spoecified conditions evalautes to True (or a Truthy value). If False , the block is skipped entirely

SYNTAX : 
---------
if condition:
    # Code block executed if condition is True
"""
# Example of if Statement : 
temperature = int(input("Enter the temperature (in degree celsius) : "))
if (temperature >= 40): # Checks if the boolean expression is True or False . 
    # If True , executes the intended block of the code , else ignores it
    print(f"Current Temperature is : {temperature}degree celsius")
    print("Stay Hydrated")
print("Weather Checks Completed :) ")

"""
if-else statement : 
--------------------
The if-else statement provides a binary branch; One block of code executes when the condition is True and the 'else' block of code executes when the condition is False

SYNTAX : 
--------
if condition:
    # Code block executed if condition is True
else:
    # Code block executed if condition is False
"""

# Example of if-else statement
age = int(input("Enter your Age : "))
if (age >= 18):
    print(f'Since you are above 18 years old , you are eligible to vote')
else:
    print(f'Since you are below 18 years old! You are not eligible to vote')


"""
if-elif-else ladder : 
---------------------
When you need to evaluate mulytiple mutually exclusive conditions sequentially use 'elif' (short for else if)
Python checks the condition from top to bottom and executes the block for the 1st condition that evaluates to True, skipping the rest of the ladder
The trailing 'else' block is optional and acts as a catch-all default

Syntax : 
---------
if condition_1:
    # Executed if condition_1 is True
elif condition_2:
    # Executed if condition_1 is False and condition_2 is True
elif condition_3:
    # Executed if previous conditions are False and condition_3 is True
else:
    # Executed if all conditions above are False
"""

# if-elif-else ladder
mark = int(input("Enter your mark : "))
if (mark >= 90):
    print(f'Grade : O')
elif (mark >= 80 and mark <=89):
    print(f'Grade : A+')
elif (mark >= 70 and mark <=79):
    print(f'Grade : A')
elif (mark >= 60 and mark <= 69):
    print(f'Grade : B+')
elif (mark >=50 and mark <= 59):
    print(f'Grade : B')
else : 
    print('Since your mark is less than 50 , You are failed')

"""
Nested If-Else Statements : 
---------------------------
You can place an if, if-else, if-elif-else blocks inside another conditional blocks to test dependent , multi-layer conditions

SYNTAX :
----------
if outer_condition:
    if inner_condition:
        # Executed if both outer_condition and inner_condition are True
    else:
        # Executed if outer_condition is True, but inner_condition is False
else:
    # Executed if outer_condition is False
"""

# Nested IF case
age_eligibility = int(input(f'Enter your Age : '))
has_voter_id = input(f'Whether you had voter id : (y/n)')

if (has_voter_id == 'y'):
    has_voter_id = True
elif (has_voter_id == 'n'):
    has_voter_id = False
else:
    print(f'Enter either y or n')

if (age_eligibility >= 18):
    if (has_voter_id):
        print(f'Since you are above 18 and you have Voter ID , you are eligible to vote!')
    else:
        print("Vote Permission Denied!. Please bring or apply your Voter ID card")
else:
    print('Since you are below 18 years old , you are not eligible to vote')


"""
Ternary Conditional Expression (One Line if-else) : 
----------------------------------------------------
Python supports a compact single-line conditional expression-often called as ternary operator-used to assign values based on conditions

SYNTAX : 
---------
value_if_true if condition else value_if_false

(Note: Unlike C/Java's condition ? true_val : false_val, Python places the true outcome first).
"""

# Ternary Conditions : One-Line If-Else Statements
number = int(input("Enter a number : "))
print(f"{number} is even number" if number % 2 == 0 else f"{number} is odd number")


"""
Structural Pattern Matching (Match-Case) : 
------------------------------------------
Introduced in Python 3.10, match-case is Python's Modern, far more powerful counterpart to traditional switch-case statements. It matches values, sequence, types and dictionary structures against patterns

SYNTAX : 
---------
match subject:
    case pattern_1:
        # Action for pattern_1
    case pattern_2 | pattern_3:
        # Action if subject matches pattern_2 OR pattern_3
    case pattern_4 if guard_condition:
        # Action if pattern_4 matches AND guard_condition is True
    case _:
        # Wildcard default case (matches anything)
"""

# Match Case
http_status_code = int(input("Enter the http status code : "))
match http_status_code:
    case 200:
        print("Status OK")
    case 400:
        print("Authentication or Permission Error")
    case 403:
        print("Forbidden Error")
    case 404:
        print("Page Not Found")
    case 500:
        print("Internal Server Error")
    case default:
        print(f'Unhandled Status Code')

# Combining Conditions and Python's best practices : 
# Logical Operators (AND, OR, NOT)
age = int(input("Enter your age : "))
had_license = input('Whether you had License ? : (y/n) : ')

if (age >= 18) and (had_license == 'y'):
    print(f'Allowed to drive on road')
else:
    print(f'You are not allowed to drive on road')
