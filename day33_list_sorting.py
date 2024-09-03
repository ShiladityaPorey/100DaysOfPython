#Day33 of Python Programming
#September02, 2024


L=['a','d', 'z','','p','c','e']
L1=L
print(L)

L.sort() # Sorted in ascending order
print(L)

L1.sort(reverse=True) # Sorted in descending order
print(L1)


L2=['AE','BK','XJ','BA']
L2.sort()   # Sorted alphabetically
print(L2)

L2.sort(reverse=True)  # Sorted in reverse alphabetical order
print(L2)


L3=['a','B','c','D','j']
L3.sort(key=str.lower)  # Default sort (case-sensitive)
print(L3)

L3=['a','B','c','D','j']
L3.sort()
print(L3)
L3.sort(reverse=True) # Reverse default sort
print(L3)


L3.sort(key=lambda x: (x.isupper(), x)) # Prioritize lowercase over uppercase
print(L3)


L3.sort(key=lambda x: (x.islower(), x)) # Prioritize uppercase over lowercase
print(L3)
