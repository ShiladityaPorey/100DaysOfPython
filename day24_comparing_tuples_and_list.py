# Day 24 Python Programming
# August 24, 2024

# additional reading:
#https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/


#tupple
tupple_data = ('PY-23', 'PY-45','PY-16', 'PY-50', 'PY-39', 'PY-65')

#list
list_data=['PY-23', 'PY-45','PY-16', 'PY-50', 'PY-39', 'PY-65']

print(tupple_data)
print(list_data)

# Input and validation
ID=input("Enter the ID of the student to check:")


# Check in tuple
if ID in tupple_data:
    print(f"This ID is valid.")

else:
    print(f"This ID is not valid.")


# Check in list
if ID in list_data:
    print(f"This ID is valid.")

else:
    print(f"This ID is not valid.")



# Accessing and modifying elements
print(list_data[1])
print(tupple_data[1])


# List modification - no error
list_data[1]=90
print(list_data[1])

# Tuple modification - raises error
tupple_data[1]=90
