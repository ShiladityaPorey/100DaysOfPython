# Day 27 Python Programming
# August 27, 2024

a1 = [23, 34, 43, 'ty', 78, 0.9, 300, 98, 287, 34, 2]
print(a1)



# Check for an element and get its index
print('ty' in a1)  # Single-argument operation
print(a1.index('ty'))  # Single-argument operation

# Remove an element
a1.remove('ty')  # Single-argument operation
print(a1)

# Append a single element
a1.append(7.053)  # Single-argument operation
print(a1)

# Insert an element at a specific position
a1.insert(2, 10000)  # Two-argument operation
print(a1)

# Insert and delete operations
a1.insert(2, 1000.0007)  # Two-argument operation
print(a1)

del(a1[2])  # Single-argument operation
print(a1)


del a1[2:4]  # Deletes elements at index 2 and 3
print(a1)
