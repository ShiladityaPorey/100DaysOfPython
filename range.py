#Day 8 of python programming
#August 8, 2024
 
# Example: range(start, stop, step)
print("Syntax rule: range(start, stop, step.)")
print("also: range(stop), range(start, stop)")


print("Example 1:")
for i in range(20, 1, -4):
    print(i)  # Output: 2 4 6 8

print("Example 2:")
for i in range(6):
    print(i)  # Output:0 1 2 3 4 5; 6 is excluded


print("application: print list of students' name")

# List of strings
string_list = ["Name_1", "Name_2", "Name_3"]

# Iterate over the list directly
for fruit in string_list:
    print(fruit)
    

