from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)

print(chain['a'])  # Output: 1 (from dict1)
print(chain['b'])  # Output: 2 (from dict1)
print(chain['c'])  # Output: 4 (from dict2)

# Adding a new dictionary to the chain
dict3 = {'d': 5}
chain = chain.new_child(dict3)
print(chain['d'])  # Output: 5
