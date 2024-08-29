# Python 3.5+ way of merging
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged)

# Python 3.9+ way of merging
merged = dict1 | dict2
print(merged)
