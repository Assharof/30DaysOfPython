# Day 2: 30 Days of python programming

# level 1

first_name = "Assharof"
last_name = "Olamide"
full_name = first_name + " " + last_name
country = "Nigeria"
city = "Iwo"
age = 30
year = 2026

is_married = True
is_true = True
is_light_on = True

# Multiple variables in a line

a, b, c = 20, 45, 50

# level 2

# 1. check data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a), type(b), type(c))

# 2. Length of first name
print(len(first_name))

# 3. Compare first name and second name
print(len(first_name) > len(last_name))

# 4. Declare numbers
num_one = 5
num_two = 4

# 5. Addition
total = num_one + num_two

# 6. Subtraction
diff = num_two - num_one

# 7. Multiplication
product = num_one * num_two

# 8. Division
division = num_one / num_two

# 9. Modulus
remainder = num_two % num_one

# 10. Exponent
exp = num_one ** num_two

# 11. Floor division
floor_division = num_one // num_two

# 12. Circle calculation
radius = 30
pi = 3.14

area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print("Area:", area_of_circle)
print("Circumference:", circum_of_circle)

# Take radius as input
user_radius = float(input("Enter radius: "))
user_area = pi * user_radius ** 2
print("Area from user input:",user_area)

# 13 User input
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country name: ")
user_age = input("Enter your age: ")
age = int(age)

print(user_first_name, user_last_name, user_country, user_age)

# 14. python keyword
help('keywords')
