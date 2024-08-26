# Day 19 Python Programming
# August 19, 2024

# Initialize an empty list to store student IDs
_data_of_students = []

# Use a while loop to repeatedly ask for student IDs
while True:
    # Prompt the user to enter the ID of the student
    print('Enter the ID of student', len(_data_of_students) + 1,
          ' (Or enter nothing to stop.):')
    
    # Get input from the user
    ID = input()
    
    # Break the loop if the user enters nothing (empty string)
    if ID == '':
        break
    
    # Add the entered ID to the list using list concatenation
    _data_of_students = _data_of_students + [ID]

# Print a message to indicate the data entered
print('Data entered are:')

# Use a for loop to print each ID in the list
for ID_list in _data_of_students:
    print('  ' + ID_list)
