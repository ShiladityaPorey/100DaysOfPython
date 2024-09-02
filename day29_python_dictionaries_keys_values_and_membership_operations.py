#Day29 of Python Programming
#August29, 2024


# Define a string variable for the name
AD = 'Jhonathon'

# Create a dictionary with keys: 'name', 'ID', and 'SUB'
sd = {'name': AD, 'ID': 123, 'SUB': 'Python'}

# Loop through and print all the keys in the dictionary
for i in sd.keys():
    print(i)

# Loop through and print all the values in the dictionary
for i in sd.values():
    print(i)

# Print the keys of the dictionary
print(sd.keys())

# Print the values of the dictionary
print(sd.values())

# Convert the dictionary keys to a list and print it
print(list(sd.keys()))

# Convert the dictionary keys to a tuple and print it
print(tuple(sd.keys()))

# Check if 'name' is a key in the dictionary and print the result
print('name' in sd.keys())

# Check if 'name' is NOT a value in the dictionary and print the result
print('name' not in sd.values())

# Check if 'Python' is a value in the dictionary and print the result
print('Python' in sd.values())

