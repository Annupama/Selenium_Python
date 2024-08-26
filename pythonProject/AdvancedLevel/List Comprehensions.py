# Creating a List of Squares

squares = [x**2 for x in range(10)]
print(squares)        # output is [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtering with a Condition

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)      # Output is [0, 4, 16, 36, 64]

# Nested List Comprehensions

pairs = [(x, y) for x in range(5) for y in range(5)]
print(pairs)   # Output is [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0),
# (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

# Modifying Items in the List

words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # Output is ['HELLO', 'WORLD', 'PYTHON']


# List Comprehension with a Function

def square(x):
    return x*x


squares = [square(x) for x in range(10)]
print(squares)     # Output is [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Flattening a List of Lists

