"""
Escape Sequence in Python : 

An Escape Sequence , that usually starts with a backslash (\\) symbol, followed by a specific character or a symbol.
They are used to represent special or non-printable characters inside string literals, such as newlines , tabs or quotes

Why do we need Escape Sequence :

Sometimes , string contains characters that conflicts with python's syntax.
Eg. print('my name is 'Ashwin Kannan'') # Generates Syntax Error 
Escape Sequences allows us to escape the special meaning of characters.

Common Python Escape Sequences : 

1) \n : New Line (Insets a line break and move the cursor to the next line)
2) \t : HorizontalTab (Inserts a tab space)
3) \' : Prints single quote
4) \" : Prints double quote
5) \\ : Prints backslash
6) \b : Backspace (Deletes the character before the cursor)
7) \\r : Carriage Return (Moves the cursor to the beginning of the line)
"""
print("Topic : Escape Sequence in Python")
print("Hello my name is : \"Ashwin Kannan\" \nI am working ina \"Jio Platforms Limited \" Organization as a \"DevOps Engineer\" \n\t - Best Regards \n\t\t Ashwin Kannan")

print("\n")

# The above print statement can also be re-written as below way : Personally below codes are much more readable
print("Hello my name is : 'Ashwin Kannan'")
print("I am working in a 'Jio Platforms Limited' Organization as a 'DevOps Engineer'")
print("\t - Best Regards")
print("\t\t Ashwin Kannan")

# Without Escape Sequence : 
# print("Hello my name is : "Ashwin Kannan""
#       I am working in a "Jio Platforms Limited" Organization as a "DevOps Engineer"
#       - Best Regards
#       Ashwin Kannan") # Generates Syntax Error : Unterminated String Literal


print("\n")

# // - Double Backslash character escape sequence is used to print the actual (\) symbol in the string character
print("Path Location : C:\\Users\\Ashwin Kannan\\Documents\\Python_Practice\\4_Escape_Sequence.py")
print("Path Location : /Users/Ashwin Kannan/Documents/Python_Practice/4_Escape_Sequence.py") # This is also valid way to print the path location
# print("Path Location : C:\Users\Ashwin Kannan\Documents\Python_Practice\4_Escape_Sequence.py") # Generates Syntax Error : Unicode Error

# Raw Strings : 
# 'r' stands for carriage return, which is used to ignore the escape sequence entirely (eg. File Path or Regex)
# Prefix a string with 'r' to create a raw string, which treats backslashes as literal characters rather than escape characters.
print(r"Path Location : C:\Users\Ashwin Kannan\Documents\Python_Practice\4_Escape_Sequence.py") # This is also valid way to print the path location

