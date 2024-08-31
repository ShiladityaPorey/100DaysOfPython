# Day 26 Python Programming
# August 26, 2024

a1 = [23, 34, 43, 'ty', 78, 0.9, 300, 98, 287, 34, 2]
print(a1)

import copy

# Shallow copy of the entire list (single argument)
c1 = a1
print(c1)

# Shallow copy of a portion of the list (single argument)
c2 = a1[2:6]
print(c2)

# Creating deep copies (single argument)
b1 = copy.copy(a1)
print(b1)

# Copy a portion of the list (single argument)
b2 = copy.copy(a1[0:3])
print(b2)
