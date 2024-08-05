# Example of mathematical operation precedence in Python

# Define variables
a = 5
b = 3
c = 2
print("we are considering three numbers:", a,",", b,",", c)

# Operations with parentheses
result1 = (a + b) * c
print(f"(a + b) * c = {result1}")  # Output: (5 + 3) * 2 = 16

# Exponentiation
result2 = a ** b ** c
print(f"a ** b ** c = {result2}")  # Output: 5 ** (3 ** 2) = 5 ** 9 = 1953125

# Multiplication, Division, and Modulus
result3 = a * b / c
print(f"a * b / c = {result3}")  # Output: 5 * 3 / 2 = 7.5

# Addition and Subtraction
result4 = a + b - c
print(f"a + b - c = {result4}")  # Output: 5 + 3 - 2 = 6

# Combined operations to show precedence
result5 = a + b * c / a ** b
print(f"a + b * c / a ** b = {result5}")  # Output: 5 + (3 * 2 / (5 ** 3)) = 5 + (6 / 125) = 5.048

# Show that exponentiation is right-to-left
result6 = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result6}")  # Output: 2 ** (3 ** 2) = 2 ** 9 = 512

# Show precedence of all operators together
result7 = (a + b) * c / a ** b - c
print(f"(a + b) * c / a ** b - c = {result7}")  # Output: (5 + 3) * 2 / (5 ** 3) - 2 = 16 / 125 - 2 = -1.984
