# Day 21 Python Programming
# August 21, 2024


#multiple assignments


# List of student IDs
_id_l = ['PY-23', 'PY-45','PY-16', 'PY-50', 'PY-39', 'PHY-65']


print(_id_l)


# Assign individual IDs to variables
d_1=_id_l[0]
d_3=_id_l[2]
print(f"{d_1},{d_3}, {_id_l}")






# Example of multiple assignment to separate variables
d_1,d_2,d_3,d_4,d_5,d_6=_id_l
print(f"{d_1},{d_2},{d_3},{d_4},{d_5},{d_6}")


# This doesn't work: mismatch in the number of variables and list elements
# d_9, d_10 = _id_l  # Too many values to unpack (expected 2)
d_9, d_10 = _id_l[:2]
print(f"{d_9},{d_10}")
d_9, d_10, *_ = _id_l
print(f"{d_9},{d_10}")
d_1, d_2, *rest = _id_l
print(f"{d_9},{d_10}")


# Slice to get the 3rd and 4th elements (index 2 and 3)
d_3, d_4 = _id_l[2:4]

print(f"3rd element: {d_3}, 4th element: {d_4}")


# Unpack the list, ignoring unwanted elements
_, _, d_3, d_4, *_ = _id_l
print(f"3rd element: {d_3}, 4th element: {d_4}")
