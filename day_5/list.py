#30 Days of python

# Level 1
# Task 1 Declaration of empty list.
lst = []

# Task 2 Declaratio of a list with more than 5 itmes
names = ["Assharof", "Olamide", "Sherif", "Mariam", "Adesewa", "Musharrof", "Hanan,"]

# Task 3 Finding length of a list.
print(len(names))

# Task 4 Getting the first item, the middle item and the last item of the list.
print(names[0])
print(names[2:4])
print(names[6])

# Task 5 Declaring a list called mixed_data_types.
mixed_data_types = ['Olamide', 30, 40.4, 'Married', 'Osun State']
print(mixed_data_types)

# Task 6 Declaring a list variable named it_companies.
companies = ['Facebook','Google','Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Task 7 Printing companies variable.
print(companies)

# Task 8 Printing the number of companies in the list.
print(len(companies))

# Task 9 Printing the first, middle and last company.
print(companies[0])
print(companies[2:4])
print(companies[-1])

# Task 10 Printing the list after modifying one of the companies.
companies[0] = 'Assharof'
print(companies)

# Task 11 Adding an IT company to it_companies.
companies.append('Olamide IT company')
print(companies)

# Task 12 Inserting an IT company in the middle of the companies list.
companies.insert(4, 'Muraina IT company')
print(companies)

# Task 13 Changing one of the it_companies names to uppercase (IBM excluded!).
companies[1] = companies[1].upper()
print(companies)

# Task 14 Joining the it_companies with a string '#;  '.
print("#; ".join(companies))

# Task 15 Checking if a certain company exists in the it_companies list.
does_exist = 'Oracle' in companies
print(does_exist)
does_exist = 'oracle' in companies
print(does_exist)

# Task 16 Sorting the list using sort() method.
companies.sort()
print(companies)

# Task 17 Reversing the list in descending order using reverse() method.
companies.sort(reverse=True)
print(companies)

# Task 18 Slicing out the first 3 companies from the list. 
print(companies[3:])

# Task 19 Slicing out the last 3 companies from the list. 
print(companies[-9:-4])

# Task 20 Slicing out the middle company of companies from the list. 
print(companies[5])

# Task 21 Removing the first IT company from the list.
companies.pop(0)
print(companies)

# Task 22 Removing the middle IT company from the list.
companies.pop(5)
print(companies)

# Task 23 Removing the last IT company from the list.
companies.pop()
print(companies)

# Task 24 Removing all IT company from the list.
companies.clear()
print(companies)

# Task 25 Destroying the IT companies list.
del companies

# Task 26 Joining the following lists.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
front_end.extend(back_end)
print(front_end)

# Task 27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

front_end.append("Python")
front_end.append("SQL")
front_end.append("Redux")
print(front_end)

# Level 2

# Task 1 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print('ages:',ages)
min_age = min(ages)
max_age = max(ages)
print('min age:',min_age)
print('max age:',max_age)
ages.append(19)
ages.append(26)
avg = sum(ages) / len(ages)
print(avg)
range = max_age - min_age
print(range)
compare = abs(min(ages) - avg), abs(max(ages) - avg)
print(compare)

countries_list = countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
middle_country = len(countries_list) // 2
print(middle_country)
print(countries_list[middle_country])
first_half = countries_list[:98]
second_half = countries_list[98:]
#first_half = countries_list[:middle_country]
#second_half = countries_list[middle_country:]
print(first_half)
print(second_half)

['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *rest = countries_list
print(first_country)
print(second_country)
print(countries_list)
