my_dict = {'a': 1, 'b': 2, 'c': 3}

# View of keys
keys_view = my_dict.keys()
print(keys_view)  # Output: dict_keys(['a', 'b', 'c'])

# View of values
values_view = my_dict.values()
print(values_view)  # Output: dict_values([1, 2, 3])

# View of items
items_view = my_dict.items()
print(items_view)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Modifying the dictionary affects the views
my_dict['d'] = 4
print(keys_view)  # Output: dict_keys(['a', 'b', 'c', 'd'])
