#Day15 python coding
#August 15, 2024


# Step 1: Define the global variable
balance = 100000

min_balance=1000

# Step 2: Define the function to deposit money
def deposit(amount):
    global balance  # Access the global variable
    balance += amount
    print(f"${amount} deposited. New balance: ${balance}")

# Step 3: Define the function to withdraw money
def withdraw(amount):
    global balance  # Access the global variable
    if balance-amount >= min_balance:
        balance -= amount
        print(f"${amount} withdrawn. New balance: ${balance}")
    else:
        print("Insufficient funds.")

# Step 4: Define the function to check balance
def check_balance():
    print(f"Current balance: ${balance}")

# Example usage
deposit(500)
withdraw(99990)# This should trigger an insufficient funds message
withdraw(200)
check_balance()
withdraw(1500)  
