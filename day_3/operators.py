# 30 Days of coding

# variable declaration

# Task 1 Variable declaration.
age = 30

# Task 2.
height = 7.89

# Task 3.
complex_number = 5 + 2j

# Task 4 Triangle area.
user_base = float(input("Enter base: "))
user_height = float(input("Enter height: "))
area_of_triangle = 0.5 * user_base * user_height
print(f"The area of the triangle is {area_of_triangle}\n")

# Task 5 Triangle perimeter.
user_side_a = int(input("Enter side a: "))
user_side_b = int(input("Enter side b: "))
user_side_c = int(input("Enter side c: "))
perimeter_of_triangle = user_side_a + user_side_b + user_side_c
print(f"The perimeter of the triangle is {perimeter_of_triangle}\n")

# Task 6 Rectangle.
length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}\n")

# Task 7 Circle.
radius = float(input("Enter a radius: "))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print(f"The area of a circle is {area}")
print(f"The circumference of a circle is {circumference}\n")

# Task 8 Slope and intercept.
slope_8 = 2
x_intercept = 1
y_intercept = -2
print(f"Slope:{slope_8}, X intercept:{x_intercept}, Y intercept:{y_intercept}\n")

# Task 9 Slope and Euclidean distance.
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_9 = (y2 - y1)/(x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 # sqrt via **0.5
print(f"Slope: {slope_9}")
print(f"Euclidean distance: {distance}\n")

# Task 10 Slope.
print(slope_8 is slope_9)

# Task 11 Factoring.
# factoring: (x + 3)^2 = 0    x = -3
x = -3
y = x ** 2 + 6 * x + 9
print(f"When x = {x}, y = {y}\n") # y = 0

# Task 12 Length + falsy comparision.
print(len("python"))
print(len("dragon"))
print(len("python") != len("dragon"))

# Task 13 'on' in both.
print("on in python:", "on" in "python" and "on in dragon:", "on" in "dragon\n") 

# Task 14 'jargon' in sentence.
print("I hope this course is not full of jargon:", "jargon" in "I hope this course is not full of jargon\n") 
# Task 15 No 'on' in both.
print("on not in python:", "on" not in "python" and "on not in dragon:", "on" not in "dragon\n")

# Task 16 Len, Float and String.
length = len("python")
as_float = float(length)
as_string = str(as_float)
print(type(as_string), as_string)

# Task 17 Even number check.
number = int(input("Enter a number:"))
print(f"The input number is {number} and is even number {number % 2 == 0} ")

# Task 18 Floor division check.
print((7 // 3) == int(2.7)) 

# Task 19 Type conversion.
num1 = "10"
num2 = 10
print(type(num1) == type(num2))

# Task 20 Trap - int('9.8') raises a valueError.
# int() can't convert a float-formatted string
# You must go through float first
print(int(float('9.8')) == 10)

# Task 21 Weekly pay.
hours = int(input("Enter hours:"))
hour_rate = int(input("Enter rate per hour:"))
weekly_earning = hours * hour_rate
print(f"Your weekly earning is {weekly_earning}")

# Task 22 Seconds in lifetime.
year = int(input("Enter number of year you have lived:"))
seconds = year * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds")

# Task 23 Table.
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
