# Global variable
x = 10

def demonstrate_local_global():
    # Local variable
    x = 5
    print(f"Inside function - Local variable x: {x}")

# Call the function
demonstrate_local_global()

# Print the global variable
print(f"Outside function - Global variable x: {x}")
