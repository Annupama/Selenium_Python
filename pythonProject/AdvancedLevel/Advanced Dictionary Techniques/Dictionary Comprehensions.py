squares = {x:x*x for x in range(1,6)}
print(squares)                       # Output is {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 2
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)                        # Output is {1: 'a', 2: 'b', 3: 'c'}
