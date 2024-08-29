from collections import Counter

counter = Counter("Hello World")
print(counter)              # Output is Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})

print(counter.most_common(2))    # Output is [('l', 3), ('o', 2)]
