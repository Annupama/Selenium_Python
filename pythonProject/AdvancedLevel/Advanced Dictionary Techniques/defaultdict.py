from collections import defaultdict

# Default factory is int, so it defaults to 0
counts = defaultdict(int)
counts['a'] += 1
counts['b'] += 2
print(counts)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})

# Default factory is list, so it defaults to an empty list
list_dict = defaultdict(list)
list_dict['a'].append(1)
print(list_dict)  # Output: defaultdict(<class 'list'>, {'a': [1]})
