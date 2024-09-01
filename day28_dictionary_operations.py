# Day 28 of Python Programming
# August 28, 2024

# Creating a dictionary with student data
s_data = {'name': 'AB', 'ID number': 112, 'university': 'A University'}
print(s_data)  # Print the entire dictionary

# Accessing a value using a key
print(s_data['name'])  # Output: 'AB'

# Dictionaries can use non-zero numbers as keys
s_data = {1: 'AB', 'ID number': 112, 'university': 'A University'}
print(s_data[1])  # Output: 'AB'

# Dictionaries can also use floating-point numbers as keys
s_data = {1.9: 'AB', 'ID number': 112, 'university': 'A University'}
print(s_data[1.9])  # Output: 'AB'
