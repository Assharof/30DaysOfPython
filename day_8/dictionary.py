# 30 days of python

# Task 1 Create an empty dictionary called dog.
dog = {}

# Task 2 Add name, color, breed, legs, age to the dog dictionary. 

dog = {
	'name' : 'biggy',
	'color' : 'brown',
	'breed' : 'bororo',
	'legs' : 4,
	'age' : 3
	}

# Task 3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary.

student = {
    'first_name':'Assharof',
    'last_name':'Olamide',
    'age':150,
    'country':'Nigeria',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
       'street':'Testing ground street',
        'zipcode':'02416'
              },
	'city':'Iwo'
    }

# Task 4 Get the length of the student dictionary.
print(len(student))

# Task 5 Get the value of skills and check the data type, it should be a list.
print(student['skills'])
print(type('skills'))

# Task 6 Modify the skills values by adding one or two skills.
student['skills'].append('HTML')
student['skills'].append('CSS')
print(student)

# Task 7 Get the dictionary keys as a list.
keys = student.keys()
print(keys)

# Task 8 Get the dictionary values as a list.
keys = student.values()
print(keys)

# Task 9 Change the dictionary to a list of tuples using items() method.
print(student.items())

# Task 10 Delete one of the items in the dictionary.
student.pop('first_name')
print(student)

# task 11 Delete one of the dictionaries.
del student
