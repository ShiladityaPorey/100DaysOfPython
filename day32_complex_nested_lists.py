#Day32 of Python Programming
#September 01, 2024

complex_list = [
    [{'name': 'Alice', 'age': 28, 'skills': ['Python', 'Machine Learning']}, 
     {'name': 'Bob', 'age': 32, 'skills': ['Java', 'Web Development']}],
    
    [['x', 'y', 'z', {'key1': 'value1', 'key2': 'value2'}], 
     [100, 200, 300, 400], 
     [0.1, 0.01, 0.001, [10, 20, {'nested_key': 'nested_value'}]]],
    
    ['level_1', ['level_2', ['level_3', ['end', {'final_key': 'final_value'}]]]]
]

# Access elements:
# 'Machine Learning' from Alice's skills
ml_skill = complex_list[0][0]['skills'][1]
# 'value2' in a nested dictionary
value2 = complex_list[1][0][3]['key2']
# 200 from a list of integers
integer_200 = complex_list[1][1][1]
# 'nested_value' in a deeply nested dictionary
nested_val = complex_list[1][2][3][2]['nested_key']
# 'final_value' from multiple nested levels
final_val = complex_list[2][1][1][1][1]['final_key']

print(" ", ml_skill, value2, integer_200, nested_val, final_val)
