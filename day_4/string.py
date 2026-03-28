# Task 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python'.
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# Task 2 Concatenate the string 'Coding', 'For' , 'All'.
print('Coding' + ' ' + 'For' + ' ' + 'All')

# Task 3 Variable declaration
company = "Coding For All"

# Task 4 printing variable with print()
print(company)
print(f"{company}")

# Task 5 Print the length of the company string.
print(len(company))

# Task 6 Change all the characters to uppercase.
print(company.upper())

# Task 7 Change all the characters to lowercase.
print(company.lower())

# Task 8 Using capitalize(), title(), swapcase() methods
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Task 9 Cut(slice) out the first word.
first_word = company.split()[0]
print(first_word)

# Task 10 Checking if Coding For All string contains a word Coding.
print(company.find('Coding'))

# Task 11 Word replacement
print(company.replace('Coding','Python'))

# Task 12 Sentence replacement
python_everyone = "Python for Everyone"
python_for_all = python_everyone.replace('Everyone', 'All')
print(python_for_all)

# Task 13 Spliting string using space as the separator.
print(company.split())

# Task 14 Spliting string. 
companies_name = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies_name.split(','))

# Task 15 Checking the character at index 0.
print(company[0])

# Task 16 Checking the index of the last character.
print(company[-1])

# Task 17 Checking the character at index 10.
print(company[10])

# Task 18 Create an acronym or an abbreviation for a string.
python_everyone_acronym = ''.join([word[0] for word in 'Python For Everyone'.split()])
print(python_everyone_acronym)  

# Task 19 Create an acronym or an abbreviation for a string.
coding_for_all_acronym = ''.join([word[0] for word in 'Coding For All'.split()]) 
print(coding_for_all_acronym)

# Task 20 Using index to determine the position of first character in a string.
sub_string = 'C'
print(company.index(sub_string))  

# Task 21 Using index to determine the position of a character in a string.
sub_string = 'F'
print(company.index(sub_string))  

# Task 22 Using rfind to determine the position of occurence of a character in a string.
sub_string = 'l'
print(company.rfind(sub_string))  

# Task 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence.
because_sentence =  'You cannot end a sentence with because because because is a conjunction'
sub_string = 'because'
print(because_sentence.find(sub_string))  

# Task 24 Use rindex or find to find the position of the first occurrence of the word 'because' in the following sentence.
because_sentence =  'You cannot end a sentence with because because because is a conjunction'
sub_string = 'because'
print(because_sentence.rindex(sub_string))  

# Task 25 Slicing out 'because' in the following sentence.
because_sentence =  'You cannot end a sentence with because because because is a conjunction'
print(because_sentence[31:55])

# Task 26 Use index  to find the position of the first occurrence of the word 'because' in the following sentence.
because_sentence =  'You cannot end a sentence with because because because is a conjunction'
sub_string = 'because'
print(because_sentence.index(sub_string))  

# Task 27 Slicing out 'because' in the following sentence.
because_sentence =  'You cannot end a sentence with because because because is a conjunction'
print(because_sentence[31:55])

# Task 28 Checking if a string start with a specific substring.
sub_string = 'Coding'
print(company.startswith(sub_string))  

# Task 29 Checking if a string ends with a specific substring.
sub_string = 'coding'
print(company.endswith(sub_string))  

# Task 30 remove the left and right trailing spaces in the given string.
coding = '   Coding For All      '
print(coding.strip(' '))  

# Task 31 Check valid identifiers.
print('30DaysOfPython'.isidentifier())     
print('thirty_days_of_python'.isidentifier()) 

# Task 32  Joining a list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(python_libraries)
print(result)

# Task 33 Using the new line escape sequence to separate two sentences.
print('I am enjoying this challenge.\nI just wonder what is next.')

# Task 34 Using the tab escape.
header = 'Name\tAge\tCountry\tCity'
content = 'Ola\t30\tNigeria\tIwo'
print(header.expandtabs())
print(content.expandtabs())

# Task 35 Using the string formatting method.
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
# Task 36 Use the string formatting method.
num1 = 8
num2 = 6
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
