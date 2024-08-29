# Day 22 Python Programming
# August 22, 2024

# Initial lists setup
num_1L = [2, 1, 26, 39, 78, 90]
num_2L = [0.1, 0.15, 0.26]

# Element-wise operations
num_1L[0] += 5   # Increment first element by 5
print(num_1L)

num_1L[5] -= 15  # Decrement last element by 15
print(num_1L)

num_1L[1] *= 4   # Multiply second element by 4
print(num_1L)

num_1L[2] /= 13  # Divide third element by 13
print(num_1L)

num_1L[3] %= 2   # Modulus operation on fourth element
print(num_1L)

# List concatenation and multiplication
num_1L += num_2L  # Concatenate num_1L and num_2L
print(num_1L)

num_2L *= 3  # Repeat num_2L three times
print(num_2L)

# Invalid operations
# num_1L -= num_2L  # This is not valid
# num_1L -= 3       # This is not valid

