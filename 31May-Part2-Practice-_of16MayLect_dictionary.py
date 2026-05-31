# ==========================================
# Dictionary with different key/value types
# ==========================================

_dictio = {
    2.70986: "float key",

    True: "boolean true",
    False: "boolean false",

    "name": "Alice",

    (1, 2): "tuple key",
    ("a", 1): "Another Tuple key!!.",

    "int_value": 100,
    "float_value": 10.5,
    "bool_value": True,
    "tuple_value": (10, 20),
    "list_value": [1, 2, 3],
    "set_value": {1, 2, 3},

    "nested_dict": {
        "id": 101,
        "name": "Rahul",
        "marks": {
            "Math": {"midterm": 85, "final": 92},
            "Physics": {"midterm": 88, "final": 51}
        }
    }
}

# Dictionary keys must be hashable (immutable).
# list, set, and dict cannot be used as keys.


# ==========================================
# Basic access operations
# ==========================================

print(_dictio, end="\n\n")

print(_dictio[2.70986], end="\n\n")

print(_dictio["nested_dict"]["marks"], end="\n\n")


# ==========================================
# keys(), values(), (items()-> see later)
# ==========================================

print(*_dictio.keys(), sep="; ")

print(*_dictio["nested_dict"].keys(), sep=", ")

print(*_dictio.values(), sep="; ")


# ==========================================
# Membership tests
# ==========================================

if 1 in _dictio:
    print(f"key name {1} exist.")
else:
    print("Not exist.")

if "Rahul" in _dictio:
    print("Found")
else:
    print("Not exist.")

if "Rahul" in _dictio["nested_dict"].values():
    print("key name Rahul exist")
else:
    print("Not exist.")


# ==========================================
# Nested dictionary lookup
# ==========================================

if _dictio["nested_dict"]["name"] == "Rahul":
    print(_dictio["nested_dict"])


# ==========================================
# get() method
# ==========================================

print(
    _dictio.get(("a", 1)),
    _dictio["nested_dict"]["marks"]["Physics"].get("midterm") + 0.07,
    sep=" ,\n"
)


# ==========================================
# Add new key/value pair
# ==========================================

_dictio[("nested_dict", 2)] = {
    "id": 102,
    "name": "Aman",
    "marks": {
        "Math": {"midterm": 93, "final": 97},
        "Physics": {"midterm": 79, "final": 75}
    }
}

print(_dictio)


# ==========================================
# Update nested value
# ==========================================

_dictio["nested_dict"]["marks"]["Physics"]["midterm"] = 69


# ==========================================
# Delete key
# ==========================================

del _dictio[("nested_dict", 2)]


# ==========================================
# Iterate using items()
# ==========================================

for k1, k2 in _dictio.items():
    print("KeysList =", k1)
    print("ValuesList =", k2)
    print()


# ==========================================
# Assignment (not a copy)
# ==========================================

dictio2 = _dictio

# ==========================================
# copy
# ==========================================
dictio3 = _dictio.copy()

# ==========================================
# Sort dictionary items
# ==========================================

sorted_marks = sorted(
    _dictio["nested_dict"]["marks"]["Physics"].items(),
    key=lambda x: x[1]
)

print(sorted_marks)


# ==========================================
# setdefault() vs update()
# ==========================================

_dictio["nested_dict"].setdefault("address", "Delhi")

print(_dictio["nested_dict"])

_dictio["nested_dict"].update(address="Kolkata")

print(_dictio["nested_dict"])


# ==========================================
# pop() and popitem()
# ==========================================

gh = _dictio["nested_dict"]["marks"]["Physics"].pop("midterm")

print(gh)

print(_dictio)

_dictio["nested_dict"]["marks"].popitem()

print(_dictio)


# ==========================================
# Dictionary merge
# ==========================================

d1 = {"a": 1}
d2 = {"b": 2}

d3 = d1 | d2

print(d3)


# ==========================================
# Dictionary comprehension
# ==========================================

squares = {
    x: x**2
    for x in range(10)
}

print(squares)