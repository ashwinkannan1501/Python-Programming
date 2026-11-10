"""
Numeric Data Types : 
---------------------
Python has 3 built-in numeric data types
1) Integer (int)
2) Floating Point (float)
3) Complex Number (complex)
Additionally , the standard library provides specialized numeric types like 'Decimal' and 'Fractions' for high precision arithmetic

All numeric types in python are immutable , i.e not changable post creation of object / variable. 
"""

"""
1) Integer (int) : 
Integers are whole numbers (positive , negative or zero) with no decimal points or fractions.
a) arbitary precisions : python integers have unlimited precision, bounded only by available system memory.
b) Radix/Base Support : Can be written in binary, octal, and hexadecimal literals.
c) Readability: Underscores (_) can be used as visual digit separators.
"""

# Standard Integers
num1 = 34
num2 = -78
num3 = 0
print(342_364)
print(num1)
print(num2)
print(num3)

# Large Integers (no overflow limit)
large_number = 14239489280940920394882720491293842938029349234882746726348236474
print(large_number)
print(type(large_number))

# Base Notation conversion
print(f'Binary value of 2387 : {bin(2387)}')
print(f'Octal Value of 2387 : {oct(2387)}')
print(f'Hexadecimal value of 2387 : {hex(2387)}')

"""
2) Floating Point Numbers : 
A floating point is a decimal numbers 
a) Precision: Typically around 15-17 decimal digits of precision.
b) Scientific Notation: Exponential syntax with e or E is natively supported.
c) Special Values: Includes positive/negative infinity (inf, -inf) and Not-a-Number (nan).


"""
# standard floating point numbers 
positive_float = 567.89657889798797098097875764453469880 # output : 567.896578897
negative_float = -567.23590
print(f"Positive Float : {positive_float}")
print(f'Negative Float : {negative_float}')
print(f'data type of {negative_float} : {type(negative_float)}')

# Scientific (Exponential) notation
speed_of_light = 3.0e8   # 3.0 * 10^8 = 300000000.0
small_value = 1.5e-4       # 1.5 * 10^-4 = 0.00015
print(f"Speed of Light : {speed_of_light}")
print(f"Small Value : {small_value}")

# Speacial Float Values : 
infinity_number = float('inf')
negative_infinity_number = float('-inf')
not_a_number = float('nan')
#printing each value and it's data type
print(f'Infinity Number : {infinity_number}')
print(f'Data Type of {infinity_number} is : {type(infinity_number)}')

print(f'Negative Infinity Number : {negative_infinity_number}')
print(f'Data Type of {negative_infinity_number} is : {type(negative_infinity_number)}')

print(f'Not a number : {not_a_number}')
print(f'Data Type of {not_a_number} is : {type(not_a_number)}')


"""
3) Complex Numbers : 
Complex numbers represent numbers with a real part and an imaginary part, written in the mathematical form a+bj, where j denotes the imaginary unit

The Real and Imaginary numbers are internally stored as floating point numbers 
Attributes such as 'real' & 'imag' returns the real and imaginary parts of a complex number separately
The method 'conugate()' returns the complex number's conjugate  
"""
complex_num1 = 45+78j
complex_num2 = 67-34j
complex_num3 = -456+90J
complex_num4 = -345-90J

print(f"Complex Number 1 : {complex_num1}")
print(f"Complex Number 2 : {complex_num2}")
print(f'Complex Number 3 : {complex_num3}')
print(f'Complex Number 4 : {complex_num4}')

print(f'Data Type of {complex_num4} is : {type(complex_num4)}')

print(f"Complex Number of 67 as real number & 89 as imaginary number is : {complex(67, 89)}")
print(f'Real part of {complex_num4} is : {complex_num4.real}')
print(f'Imaginary part of {complex_num4} is : {complex_num4.imag}')
print(f'Conjugate of {complex_num2} is : {complex_num2.conjugate()}')

complex_addition = complex_num1 + complex_num2
print(f"{complex_num1} + {complex_num2} = {complex_addition}")

complex_subtraction = complex_num2 - complex_num1
print(f"{complex_num2} - {complex_num1} = {complex_subtraction}")

complex_multiplication = complex_num3 * complex_num4
print(f'{complex_num3} x {complex_num4} = {complex_multiplication}')

complex_division = complex_num4 / complex_num3
print(f'{complex_num4} / {complex_num3} = {complex_division}')

# Specialized Numeric Types
import decimal
decimal1 = decimal.Decimal('0.1')
decimal2 = decimal.Decimal('0.2')
print(f'Addition of {decimal1} + {decimal2} is : {decimal1 + decimal2}')
print(f'{decimal1 + decimal2 == decimal.Decimal('0.3')}') # True

import fractions
fraction1 = fractions.Fraction(56, 78)
print(fraction1)
print(type(fraction1))

