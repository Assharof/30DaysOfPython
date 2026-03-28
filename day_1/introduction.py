import sys
import math
# 30 Days of python

# Level 1

# 1. Python version
print(sys.version)

# 2. Working with operators
print("Addition:", 3 + 4) # Addition operator
print("Subtraction:", 3 - 4) # Subtraction operator
print("Multiplication:", 3 * 4) # Multiplication operator
print("Division:", 3 / 4) # Division operator
print("Modulus:", 3 % 4) # Modulus operator
print("Exponent:", 3 ** 4) # Exponent operator
print("Floor division:", 3 // 4) # Floor division operator

# 3. Working with string
print("Olamide Sherif")
print("Muraina")
print("Nigeria")
print("I am enjoying 30 days of python")

# 4. Checking Data type
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Assharof', 'Python', 'Nigera']))
print(type('Olamide'))
print(type('Muraina'))
print(type('Nigeria'))

# Level 2 

# 1. Example of Data types 

# Number 
int_number = 2
float_number = 2.2
complex_number = 2-2j

# String
name = "Assharof"

# Boolean
is_married = True

# List
skills = ["C","HTML","CSS"]

# Dictionary
person_info = {
	"name": "Assharof", 
	"hobby": "Codding", 
	"age": 30 
	}

# tuple
grade = (40, 60, 70, 79)

# set
unique_number = {1, 2, 3, 4}

print(int_number, float_number, complex_number)
print(name)
print(is_married)
print(skills)
print(person_info)
print(grade)
print(unique_number)

# 2. Euclidean distance

x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Euclidean distance:", distance)

