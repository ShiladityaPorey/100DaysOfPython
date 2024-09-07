#𝐏𝐲𝐭𝐡𝐨𝐧 𝐉𝐨𝐮𝐫𝐧𝐞𝐲 𝐑𝐞𝐜𝐚𝐩 (Recap-2: Post-5)
#Day38 of 100 Days of Python Coding Challenge
#September07, 2024



variable_set1 = {1, 2, 3, 4, 6}
print(f"{variable_set1} is {type(variable_set1)}")  # Correctly identified as a set



# 1. Accessing Elements
my_tuple = (1, 2, 3, 4, 5)
print("1. Accessing Elements:", my_tuple[1])  # Output: 2

# 2. Slicing
print("2. Slicing:", my_tuple[1:3])  # Output: (2, 3)

# 3. Unpacking
a, b, c, d, e = my_tuple
print("3. Unpacking:", a, b, c, d, e)  # Output: 1 2 3 4 5

# 4. Concatenation
tuple1 = (6, 7)
result_concat = my_tuple + tuple1
print("4. Concatenation:", result_concat)  # Output: (1, 2, 3, 4, 5, 6, 7)

# 5. Repetition
result_repeat = my_tuple * 2
print("5. Repetition:", result_repeat)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# 6. Checking Membership
print("6. Checking Membership:", 3 in my_tuple)  # Output: True

# 7. Counting Occurrences
print("7. Counting Occurrences:", my_tuple.count(2))  # Output: 1

# 8. Finding the Index
print("8. Finding the Index:", my_tuple.index(4))  # Output: 3

# 9. Length of Tuple
print("9. Length of Tuple:", len(my_tuple))  # Output: 5

# 10. Nested Tuples
nested_tuple = (8, 9, (10, 11))
print("10. Nested Tuples:", nested_tuple[2][0])  # Output: 10

# 11. Iterating Over Tuples
print("11. Iterating Over Tuples:")
for item in my_tuple:
    print(item, end=" ")  # Output: 1 2 3 4 5
