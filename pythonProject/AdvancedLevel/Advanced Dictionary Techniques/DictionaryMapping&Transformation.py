# Example: Transform values
my_dict = {'a': 1, 'b': 2, 'c': 3}
transformed = {k: v ** 2 for k, v in my_dict.items()}  # Squaring values
print(transformed)  # Output: {'a': 1, 'b': 4, 'c': 9}
