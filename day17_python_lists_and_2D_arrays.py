# Day 17 Python Programming
# August 17, 2024

# Define a simple list with integers
array_1 = [1, 2, 7]
print(array_1)  # Output: [1, 2, 7]

# Define a mixed-type list with integers, a float, and a string
a = 23.9
array_2 = [1, -2, 0.009, 3, a, 'b']
print(array_2)  # Output: [1, -2, 0.009, 3, 23.9, 'b']

# Access elements from the list using indexing
print(array_2[0])  # Output: 1
print(array_2[2])  # Output: 0.009
print(array_2[-2])  # Output: 23.9 (second-to-last element)

# Define a 2D list (list of lists)
array_2D = [['PHY1', 'PHY2'], ['CH1', 'CH2', 'CH3', 'CH4', 'CH5', 'CH6', 'CH7']]

# Access elements from the 2D list using double indexing
print(f"{array_2D[1][0]}, {array_2D[1][5]}")  # Output: CH1, CH6
print(array_2D[0][1])  # Output: PHY2
