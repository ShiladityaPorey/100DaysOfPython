# Day 18 Python Programming
# August 18, 2024


# Define a mixed-type list with integers, a float, and a string
array_2 = [1, -2, 0.009, 3, 23.9, 'b']
print(array_2)  # Output: [1, -2, 0.009, 3, 23.9, 'b']



# Slicing the list
print(f"Slicing [0:3]: {array_2[0:3]}")  # Output: [1, -2, 0.009]
print(f"Slicing [2:-1]: {array_2[2:-1]}")  # Output: [0.009, 3, 23.9]
print(f"Slicing [-2:1]: {array_2[-2:1]}")  # Output: []

# Using default slicing
print(f"Slicing [:3]: {array_2[:3]}")  # Output: [1, -2, 0.009]
print(f"Slicing [4:]: {array_2[4:]}")  # Output: [23.9, 'b']

# Length of the list
print(f"Length : {len(array_2)}")  # Output: 6

# Modifying the list
array_2[3] = 0.000005
print(f"Modified list: {array_2}")  # Output: [1, -2, 0.009, 0.000005, 23.9, 'b']

# Deleting an element
del array_2[-3]
print(f"After deletion: {array_2}")  # Output: [1, -2, 0.009, 23.9, 'b']
