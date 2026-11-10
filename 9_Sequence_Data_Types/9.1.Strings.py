"""
1. Strings : 
A string is an sequence of characters which are immutable object . Once created , it cannot be modified later
Doing so , will create a new string object in memory and the old string object will be discarded by the garbage collector.
String is represented by single , double or triple quotes.
"""

# Syntax and Declaration
s1 = 'This is a string , enclosed in single quotes'
s2 = "This is a string , enclosed in double quotes"
s3 = """This is a multi-line string
, enclosed in triple quotes"""
print(f"Single Quote String : {s1}")
print(f"Double Quote String : {s2}")
print(f"Multi Line - Triple Quote String : {s3}")

# Slicing Mechanics
print(f'Single Slicing : {s1[5]}')
print(f'Slicing with Start and End Index : {s2[4:14]}')
print(f'Slicing with Start , Stop and Step Index : {s3[4:40:4]}')
print(f"Slicing with start index : {s1[5:]}")  # Slicing with start index
print(f"Slicing with end index : {s2[:14]}")  # Slicing with end index
print(f"Slicing with Negattive Index : {s2[-10]}") # Single Negative Index Slicing
print(f'Slicing with negative start and stop index : {s2[-10:-7]}')
print(f"Slicing with negative start, stop and step Index : {s1[-4:-20:-3]}")
print(f"Reverse Printing of String : {s3[::-1]}")

# In-Depth String Methods
# Case Modification
upper_case = s1.upper() # Converts all characters to upper case or capital letters
print((f'Upper Case Letters : {upper_case}')) 
lower_case = s1.lower() # Converts all characters to lower case or small letters
print(f'Lower Case Letters : {lower_case}') 
title_case = s1.title() # Converts the 1st character of each word to upper case and rest to lower case
print(f'Title Case Letters : {title_case}') 
capitalize_case = s1.capitalize() # Converts the 1st character of string to upper case and rest to lower case
print(f'Capitalize Case Letters : {capitalize_case}') 
swap_case = s1.swapcase() # Converts all upper case characters to lower case and vice versa
print(f'Swap Case Letters : {swap_case}') 

# Searching and Inspecting : 
print(f'Find starting Index of substring "single" : {s1.find("single", 4, 344)}') # Returns the starting index of substring if founnd , else returns -1
# Output of above code : word "single" is found at starting index 31
print(f'Find starting Index of substring "single" in rfind() method : {s1.rfind("single")}') # Returns the highest index of substring if found , else returns -1
# Output of above code : only one occurrence of word "single" is found at starting index 31
print(f'Index of substring "double" : {s2.index('double')}' ) # Returns the starting index of substring if found, else raise ValueError: substring not found
# Output of above code : Word "double" is found at starting index : 31
print(f'Starts with "This" ? : {s2.startswith("This")}') # Returns True if string starts with given substring , else returns False
# Output of above Code : Returns True since the word "This" is starts in the string s2. It is case sensitive
print(f'Ends with "quotes" ? : {s2.endswith("quotes")}')# Returns True if substring ends with given string, else returns False
# Output of above code : Returns True since the word "quotes" ends in string s2. It is case sensitive
print(f'Count of substring "string" : {s3.count("string")}') # Returns the no of occurrences of substring in the string
# Output of above code : returns 1 since the word "string" is found only once in string s3

#Trimming and Cleaning : 
stripping_string = "      ##This is a string with leading and trailing spaces.##     "
print(f'String with leading and trailing spaces : {stripping_string}')
print(f'String without leading and trailing spaces : {stripping_string.strip()}') # Removes leading and trailing spaces from the string
print(f'String without leading and trailing spaces and # : {stripping_string.strip().strip("#")}')
print(f'Removing # and space with "lstrip()" method : {stripping_string.strip().lstrip("#")}')
print(f'Removing # and space with "rstrip()" method : {stripping_string.strip().rstrip("#")}')

# Splitting , Partioning & Joining : 
fruit_data= "Apple, Orange, Banana, Mango, Grapes, Pineapple, Watermelon, Strawberry"
print(f'The Fruits are : {fruit_data}')
print(f'Data Type : {type(fruit_data)}')
fruit_data = fruit_data.replace(",", "$") # replace() method replaces the old substring with the new substring and returns a new string object
print(f"New Fruit String : {fruit_data}")
fruit_lists = fruit_data.split("$") # split() method splits the string into a list of substrings based on the given separator and returns a list object
print(f'Fruit List , separated by $ symbol: {fruit_lists}')
joined_string = "|".join(fruit_lists) # join() method joins the separated indexed data in the lists into the string with the given separator and returns a new string object
print(f'Joined String with "|" symbol : {joined_string}')
partitioned_string = fruit_data.partition("Grapes") # partition() method splits the string into a tuple of 3 elements based on the given separator. The 1st element is the substring part before separator, the 2nd element is the separator and the 3rd element is the substring part after the separator. If the separator is not found, it returns a tuple with the original string and two empty strings.
print(f'Partitioned String with "Grapes" : {partitioned_string}')

# Content Validation : 
isalpha = s1.isalpha() # Returns true if all characters in the string are alphabetic , else returns false
print(f'Is the string "{s1}" is alphabetic ? : {isalpha}') # Output False , because the string contains spaces and punctuation marks
isdigit = s3.isdigit() # Returns True if all characters in the strings are digits, else returns False
print(f'Is the string "{s3}" is digit ? : {isdigit}') # Output False , because the string contains letters , spaces and punctuation marks, not digits
isalnum = s2.isalnum() # Returns True if all characters in the string are alphanumeric, else returns False
print(f'Is the string "{s2}" is alphanumeric ? : {isalnum}')# Output False , because the string contains letters, spaces and punctuation , not alphanumeric (letters & digits)
isspace = fruit_data.isspace() # Returns True if all characters in the string are whitespace, else returns False
print(f'Is the string "{fruit_data}" is whitespace ? : {isspace}') # Output False, because the string con≈tains letters , spaces and punctuations , not only whietspaces

print(f'islower() method : {lower_case.islower()}') # Output True , because the string contains all lower case letters
print(f'isupper() method : {upper_case.isupper()}') # Output True , because the string contains all upper case letters
print(f'istitle() method : {title_case.istitle()}') # Output True , because the string contains all title case letters
print(f'iscapitalize() method : {capitalize_case.isnumeric()}') # Output False, because the string contains all capitalized letters, not numeric

