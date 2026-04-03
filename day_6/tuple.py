# 30 days of python

# Exsercise: Level 1

# Task 1 Creating an empty tuple.
tpl = ()

# Task 2 Creating a tuple containing names of your sisters and your brothers.
brother = ('Assharof', 'Olamide', 'Musharrof', 'Akanji')
sister = ('Mariam', 'Hanan')
print(brother)
print(sister)

# Task 3 Join brothers and sisters tuples and assign it to siblings. 
siblings = (brother + sister)
print(siblings)

# Task 4 How many siblings do you have?.
siblings_len = len(siblings)
print(siblings_len)

# Task 5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members.
siblings = list(siblings)
siblings[0] = 'Mr Muraina'
siblings[1] = 'Mrs Muraina'
siblings = tuple(siblings)
family_members = siblings
print(family_members)

# Exercise Level 2

# Task 1 Unpack siblings and parents from family_members.
siblings = ('Assharof', 'Olamide', 'Musharrof', 'Akanji', 'Mariam', 'Hanan')
siblings = tuple(siblings)
first, second, *rest = siblings
print(first)
print(second)
print(*rest)

family_member = ('Mr Muraina', 'Mrs Muraina', 'Musharrof', 'Akanji', 'Mariam', 'Hanan')
first_family_member, second_family_member, *family_member_rest = family_member
print(first_family_member)
print(second_family_member)
print(*family_member_rest)

# Task 2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('apple', 'orange', 'banana')
vegetables = ('milk', 'egg', 'meat')
food_stuff_tp = fruits + vegetables
print(food_stuff_tp)

# Task 3 Change the about food_stuff_tp tuple to a food_stuff_lt list.

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Task 4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item_index = len(food_stuff_lt)//2
middle_item = food_stuff_lt[middle_item_index]
print(middle_item)

# Task 5 Slice out the first three items and the last three items from food_stuff_lt list.
print(food_stuff_tp[0:3])
print(food_stuff_tp[:-3])

# Task 6 Delete the food_stuff_tp tuple completely.
del food_stuff_tp

# Task 7 Check if an item exists in tuple.
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print("Iceland" in nordic_countries)
