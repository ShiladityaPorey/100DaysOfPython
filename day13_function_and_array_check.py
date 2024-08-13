# Day 13 Python coding
# 100 days Python challenge
# August 13, 2024

def you_are_student(student_name):
    print(f"Welcome {student_name}!")
    print(f"You are a Python coding student.")

def you_are_not_student():
    print("You are not a student.")

# Define a list of valid student names
valid_students = ["P1", "P2", "P3"]

NAME = input("Enter your roll number: ")
print(NAME)

if NAME in valid_students:
    you_are_student(NAME)
else:
    you_are_not_student()
