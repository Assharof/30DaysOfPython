# 30 days of python

# Exercises: Level 1

# Task 1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.

user_input = int(input("Enter your age: "))
default_age = 18
user_access_age = default_age - user_input
if user_input >= default_age:
    print("You are old enough to drive.")
else:
	print(f"You are too young to drive, kindly wait for {user_access_age} years.")

# Task 2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.


user_age = int(input("Enter your age: "))
my_age = 18
age_diff = abs(my_age - user_age)
age_word = 'year'
if user_age > my_age:
    if age_diff == 1:
        age_word = 'year'
    else:
	    age_word = 'years'
    print(f"You are {age_diff} {age_word} older than me")
elif user_age == my_age:
    print(f"I am 18 years old and you are also 18 years old, so we are age mate!")
else:
    if age_diff == 1:
        age_word = 'year'
    else:
	    age_word = 'years'
    print(f"I am {age_diff} {age_word} older than you")

# Task 3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

user_input1 = int(input("Enter number 1: "))
user_input2 = int(input("Enter number 2: "))
if user_input1 > user_input2:
	print('number 1 is greater than number 2')
elif user_input1 < user_input2:
    print('number 1 is smaller than number 2')
else:
	print('number 1 is equal to number 2')


# Exercises: Level 2
# Task 1 Write a code which gives grade to students according to theirs scores:
student_score = int(input("Enter your score: "))
if student_score >= 90:
	print('Your grade is A')
elif student_score >= 80:
	print('Your grade is B')
elif student_score >= 70:
	print('Your grade is C')
elif student_score >= 60:
	print('Your grade is D')
else:
    print('Your grade is F')

# Task 2 Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = input("Enter the month: ").strip().capitalize()
if month in ['September', 'October', 'November']:
    season = 'Autumn'
elif month in ['December', 'January', 'February']:
    season = 'Winter'
elif month in ['March', 'April', 'May']:
    season = 'Spring'
elif month in ('June', 'July', 'August'):
    season = 'Summer'
else:
    season = 'Unknown month'
print(f"The season is {season}")


# Task 3 The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
new_fruit = input("Enter a name of a fruit: ").strip().lower()
add_fruit = fruits.append(new_fruit)
if add_fruit in fruits:
   	print('That fruit already exist in the list')
else:
	print('list modified',fruits)
	
#Exercises: Level 3

# Task Check :
#if the person dictionary has skills key, if so print out the middle skill in the skills list.
#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#if a person skills has only JavaScript and React, print('He is a front end developer')
#if the person skills has Node, Python, MongoDB, print('He is a backend developer')
#if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#If the person is married and if he lives in Finland.

person={
    'first_name': 'Assharof',
    'last_name': 'Olamide',
    'age': 50,
    'country': 'Nigeria',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Testing groung street',
        'zipcode': '02230'
    }
    }
if 'skills' in person:
    skills = person['skills']
    mid_index = len(skills) // 2
    print("Middle skill:", skills[mid_index])
# 2. Check if Python skill exists
print("Has Python skill:", 'Python' in skills)

# 3. Developer title
if set(skills) == {'JavaScript', 'React'}:
    print("He is a front end developer")
elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
    print("He is a backend developer")
elif set(['React', 'Node', 'MongoDB']).issubset(skills):
    print("He is a fullstack developer")
else:
    print("Unknown title")

# 4. Married and living in Nigeria.
if person['is_married'] and person['country'] == 'Nigeria':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
