#𝐏𝐲𝐭𝐡𝐨𝐧 𝐉𝐨𝐮𝐫𝐧𝐞𝐲 𝐑𝐞𝐜𝐚𝐩: (Recap-2: Post-3)
#Day 37 of 100 Days of Python Coding Challenge
#September06, 2024


variable_list1 = [78, 3.0009, 98, 5, [8, 3, 9, 10], 400]
variable_list2 = ['z', 'E', 'W', 's', 'M', 'c']

# Access, slice, and unpack lists
print(variable_list1[3])  
variable_list3 = variable_list1[:4]  
print(variable_list1[-3])  

v1, v2, v3 = variable_list1[1:4]
print(v1, v2, v3)
_, _, v1, v2, *_ = variable_list1
print(v1, v2)
v1, v2, *rest = variable_list1

# Nested list operations and deletions
print(variable_list1[4][1])
del(variable_list1[-2])
print(variable_list1)

# Modifications and concatenations
print(variable_list1 + [90.00999])
variable_list1[0] += 3
print(variable_list1)
variable_list1[0] -= 11
print(variable_list1)
variable_list1[0] *= 4
print(variable_list1)

variable_list3 = [1.008, 2.907, 4.0007]
print(variable_list1 + variable_list3)
variable_list3 *= 3
print(variable_list3)

# Finding index and sorting
element_index = variable_list1.index(98)
print(f"Index of 98: {element_index}")

variable_list2.sort()
print(variable_list2)
variable_list2.sort(key=str.lower)
print(variable_list2)
variable_list2.sort(key=lambda x: (x.isupper(), x))
print(variable_list2)
variable_list3=[1.008, 2.907,4.0007]
print(variable_list1+variable_list3)
variable_list3*=3
print(variable_list3)

# Find the index of an element
element_index = variable_list1.index(98)

variable_list2.sort()
print(variable_list2)
variable_list2.sort(key=str.lower)
print(variable_list2)
variable_list2.sort(key=lambda x: (x.isupper(), x))
print(variable_list2)
