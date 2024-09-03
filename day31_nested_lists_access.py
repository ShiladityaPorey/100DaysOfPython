# Day 31 Python Programming
# August 31, 2024

# Nested list
lb = [
    [['a', 'b', 'c', 'd'], ['g', 'h', 'j', 'k'], ['n*m', 'p', 'q', 'z']],
    [[1, 3, 5, 7], [7, 9.0, 4.6, 3.0007], [34.09, 45.987, 32.98, 1], [23.98, 12.4, 34.09, 100]]
]

# Accessing specific elements
# Find 'j'
element_j = lb[0][1][2]
print(f"'j' is found: {element_j}")

# Find 'm' (part of 'n*m')
element_m = lb[0][2][0][2]
print(f"'m' is found in: {element_m}")

# Find 3.0007
element_30007 = lb[1][1][3]
print(f"3.0007 is found: {element_30007}")

# Find 100
element_100 = lb[1][3][3]
print(f"100 is found: {element_100}")
