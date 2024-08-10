#Day 10 python programming
#August 10, 2024

print('Hi! Today we will summarize what we have learned over the last 9 days.')

print("Let us begin with this.")

print("Python can replace the simple calculator at home. Want to see how?")
print("Type '50+70+200' and press ENTER to see the total in your wallet!")
print(50+70+200)






print("Want to try? Type 'Y' for yes or 'N' for no.")
_consent=input()
if('Y'== _consent):
    NUM_1=int(input("Enter an integer number"))
    NUm_1=float(input("Enter a floating-point number",))
    print("The multiplication of", NUM_1, "and", NUm_1, "is", NUM_1*NUm_1)

elif('N'==_consent):
    pass
else:
    print("Wrong insput.")
print("We have learned 'if-elif-else', and 'pass'.")
print("And 'NUM_1', 'Num_1', 'NUM_', and '_NUM' \n - are all valid variable names.")
NUM_=2



#for loop to find factors of a number
number=int(input("Enter an integer number:",))

print("factors of ",number, "are:")
for i in range(1,number+1):
    if (number%i)==0:
        print(i,",")
        print("\n")
    else:
        continue


#same programme using while

i=1;
while i<= number:
    if (number%i)==0:
        print(i,",")
    i=i+1
