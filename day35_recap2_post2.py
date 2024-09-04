#𝐏𝐲𝐭𝐡𝐨𝐧 𝐉𝐨𝐮𝐫𝐧𝐞𝐲 𝐑𝐞𝐜𝐚𝐩: (Recap-2: Post-2)
#Day 35 of 100 Days of Python Coding Challenge
#September04, 2024

result = 3 + 5 * (2**2) ** 2 / 4 - 24
'''
PEMDAS: Parentheses, Exponents,
Multiplication/Division (left to right),
Addition/Subtraction (left to right)

multiplication and division have the
same precedence, and the same goes for addition and subtraction.
'''

print(result)
s1=2**2
s2=s1** 2
s3= 5 * s2
s4=s3/4
s5=3+s4
s6=s5-24
print(f"To veify: {s6}")


def is_prime(n):
    if number % 1 != 0:
        print(f"{number} is a fraction.")
    elif n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
    return True

# Example usage:
number = 30
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")



for i in range(100,10,-10): #steps can be negative
    print(i) #does not print last number 10



print(f"To find factors of a number:")
i=1
while i<=number:
    if number%i==0:
        print(f"{i}")
    i += 1  # Increment i to avoid infinite loop

    
