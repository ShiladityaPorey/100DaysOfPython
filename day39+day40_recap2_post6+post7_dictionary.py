#𝐏𝐲𝐭𝐡𝐨𝐧 𝐉𝐨𝐮𝐫𝐧𝐞𝐲 𝐑𝐞𝐜𝐚𝐩 🚀 (Recap-2: Post-6 + Post-7)
#Day 39+40 of 100 Days of Python Coding Challenge
#September 08+09, 2024

# Creating a dictionary with various types of keys
mixed_key_dict = {
    101: "Integer key",                   # Integer key
    "key": "String key",                  # String key
    (2, 3): "Tuple key",                  # Tuple key
    4 + 5j: "Complex number key",         # Complex number key
    True: "Boolean key",                  # Boolean key
    3.14: "Float key",                    # Float key
    frozenset({1, 2, 3}): "Frozen set key",  # Frozen set key
    None: "None key"                      # None key
}

# Print the initial dictionary and its type
print("Initial dictionary:", mixed_key_dict)
print("Type of dictionary:", type(mixed_key_dict))

# Accessing Values
print("Value for key True:", mixed_key_dict[True])  # Output: Boolean key (True is treated as 1)
print("Value for key 'key':", mixed_key_dict["key"])  # Output: String key






# Adding a new key-value pair
mixed_key_dict["new_key"] = "New string key"

# Updating an existing key-value pair
mixed_key_dict[3.14] = "Updated float key"

# Removing a key-value pair by key
del mixed_key_dict[None]  # Removes the key 'None'

# Removing a key-value pair and retrieving the value
value = mixed_key_dict.pop("key")  # Removes the key 'key' and returns its value

# Looping Through a Dictionary
# Looping through keys
for key in mixed_key_dict:
    print("Key:", key)

# Looping through values
for value in mixed_key_dict.values():
    print("Value:", value)

# Looping through key-value pairs
for key, value in mixed_key_dict.items():
    print(f"{key}: {value}")

# Getting dictionary keys, values, and items
print("Keys:", mixed_key_dict.keys())   # Output: dict_keys([101, (2, 3), (4+5j), True, 3.14, frozenset({1, 2, 3}), 'new_key'])
print("Values:", mixed_key_dict.values()) # Output: dict_values(['Integer key', 'Tuple key', 'Complex number key', 'Boolean key', 'Updated float key', 'Frozen set key', 'New string key'])
print("Items:", mixed_key_dict.items())  # Output: dict_items([(101, 'Integer key'), ((2, 3), 'Tuple key'), ((4+5j), 'Complex number key'), (True, 'Boolean key'), (3.14, 'Updated float key'), (frozenset({1, 2, 3}), 'Frozen set key'), ('new_key', 'New string key')])


























# Creating a dictionary with various types of keys
mixed_key_dict = {
    101: "Integer key",                   # Integer key
    "key": "String key",                # String key
    (2, 3): "Tuple key",                # Tuple key
    4 + 5j: "Complex number key",       # Complex number key
    True: "Boolean key",                # Boolean key
    3.14: "Float key",                  # Float key
    frozenset({1, 2, 3}): "Frozen set key",  # Frozen set key
    None: "None key"                    # None key
}

# Print the initial dictionary and its type
print("Initial dictionary:", mixed_key_dict)
print("Type of dictionary:", type(mixed_key_dict))

# Accessing Values
print("Value for key True:", mixed_key_dict[True])  # Output: Boolean key (True is treated as 1)
print("Value for key 'key':", mixed_key_dict["key"])   # Output: String key

# Adding a new key-value pair
mixed_key_dict["new_key"] = "New string key"

# Updating an existing key-value pair
mixed_key_dict[3.14] = "Updated float key"

print("Dictionary after adding and updating:", mixed_key_dict)

# Removing a key-value pair by key
del mixed_key_dict[None]  # Removes the key 'None'

# Removing a key-value pair and retrieving the value
value = mixed_key_dict.pop("key")  # Removes the key 'key' and returns its value

print("Removed value:", value)
print("Dictionary after removal:", mixed_key_dict)


#Checking if a Key Exists
if "Boolean key" in mixed_key_dict:

    print("Boolean key exists in the dictionary")

if "key" in mixed_key_dict:
    print("key exists in the dictionary")


#Looping Through a Dictionary
# Looping through keys
for key in mixed_key_dict:
    print(key)

# Looping through values
for value in mixed_key_dict.values():
    print(value)

# Looping through key-value pairs
for key, value in mixed_key_dict.items():
    print(f"{key}: {value}")





print(mixed_key_dict.keys())   # Output: mixed_key_dict(['name', 'email'])
print(mixed_key_dict.values()) # Output: mixed_key_dict(['Alice', 'alice@example.com'])
print(mixed_key_dict.items())  # Output: mixed_key_dict([('name', 'Alice'), ('email', 'alice@example.com')])
