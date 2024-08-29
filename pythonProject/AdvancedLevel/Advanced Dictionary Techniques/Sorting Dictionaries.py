my_dict = {'b': 2, 'a': 1, 'c': 3}

# Sort by keys
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Sort by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)  # Output: {'a': 1, 'b': 2, 'c': 3}
