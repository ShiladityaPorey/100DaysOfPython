# Day 20 Python Programming
# August 20, 2024

_data_of_students = ['PY-23', 'PY-45', 'PY-16', 'PY-50', 'PY-39', 'PY-65']

print(_data_of_students)

ID = input("Enter the ID of the student to check:")

print("This ID is valid." if ID in _data_of_students else "This ID is not valid.")