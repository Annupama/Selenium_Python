my_dict = {'a': 1, 'b': 2}
# Safe access with .get()
print(my_dict.get('a'))  # Output: 1
print(my_dict.get('c'))  # Output: None
print(my_dict.get('c', 'Not Found'))  # Output: Not Found
