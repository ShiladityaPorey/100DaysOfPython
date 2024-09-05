#𝐏𝐲𝐭𝐡𝐨𝐧 𝐉𝐨𝐮𝐫𝐧𝐞𝐲 𝐑𝐞𝐜𝐚𝐩: (Recap-2: Post-3)
#Day 36 of 100 Days of Python Coding Challenge
#September05, 2024

import numpy as np
import matplotlib.pyplot as plt  

# Initialize global variables to store credits and total grades
credit = 0
total_grade = 0

# Function to add points to the total grade
def add_score(points):
    global total_grade  # Use the global variable total_grade to modify it within the function
    total_grade += points
    print(f"Added {points} grades. Total score: {total_grade}")

# Function to simulate the completion of a semester with a certain credit and grade
def semester_completed(credit, grade):
    print(f"Credit {credit} completed!")
    add_score(grade)  # Add the grade points to the total score

# Simulate completing semesters with different credits and grades
semester_completed(6, 50)  # Completing 6 credits with 50 grade points
semester_completed(8, 30)  # Completing 8 credits with 30 grade points
semester_completed(10, 70)  # Completing 10 credits with 70 grade points

# Create an array of 100 values evenly spaced between 1 and 10
xs = np.linspace(1, 10, 100)

# Calculate the exponential of each value in xs
ys = np.exp(xs)

# Plot the exponential function
plt.plot(xs, ys)

# Label the x-axis as 'X'
plt.xlabel('X')

# Label the y-axis as 'exp(x)'
plt.ylabel('exp(x)')

# Add a title to the plot
plt.title('exp(x)')

# Display the plot (commented out in case you want to run this in a non-interactive environment)
plt.show()
