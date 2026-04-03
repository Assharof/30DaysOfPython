# 30 day of python 

# Exercises: Level 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(it_companies)
# Task 1 Find the length of the set it_companies.
print(len(it_companies))

# Task 2 Add 'Twitter' to it_companies.
it_companies.add('Twitter')
print(it_companies)

# Task 3 Insert multiple IT companies at once to the set it_companies.
it_companies.update(['Tiktok', 'Instagram', 'Momo'])
print(it_companies)

# Task 4 Remove one of the companies from the set it_companies
it_companies.remove("Facebook")

# Task 5 What is the difference between remove and discard.
print("We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.")

# Exercises: Level 2

# Task 1 Join A and B.
print(A.union(B))

# Task 2 Find A intersection B
print(A.intersection(B))

# Task 3 Is A subset of B
print(A.issubset(B))

# Task 4 Are A and B disjoint sets
print(A.isdisjoint(B))

# Task 5 Join A with B and B with A
print(A.update(B))
print(A | B)

# Task 6 What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Task 7 Delete the sets completely
del A
del B

# Exercises: Level 3

# Task 1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
new_age = set(age)
print(len(age))
print(len(new_age))

# Task 2 Explain the difference between the following data types: string, list, tuple and set
print('string is a sequence of characters', 'list and A tuple is a collection of different data types which is ordered and unchangeable (immutable).', 'Set is a collection of items')

# Task 3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()

unique_words = set(words)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
