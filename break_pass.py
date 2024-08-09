#Day 9 of python coding
#August 9, 2024

roll=int(input("enter roll number:",))

for i in range(10):
    if i == roll:
        pass  # To do something later
    else:
        print(i)

roll2=int(input("enter second roll number:",))

for i in range(10):
    if i == roll2:
        break  # To do something later
    else:
        print(i)
