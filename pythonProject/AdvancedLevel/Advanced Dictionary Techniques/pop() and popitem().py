my_dict = {'a': 1, 'b': 2, 'c': 3}

# Removing specific key
value = my_dict.pop('a')
print(value)  # Output: 1
print(my_dict)  # Output: {'b': 2, 'c': 3}

# Removing last item
last_item = my_dict.popitem()
print(last_item)  # Output: ('c', 3)
print(my_dict)  # Output: {'b': 2}
