from collections import OrderedDict

ordered = OrderedDict()
ordered['apple'] = 3
ordered['Banana'] = 2
ordered['Cherry'] = 5
print(ordered)                  # Output: OrderedDict([('apple', 3), ('banana', 2), ('cherry', 5)])
ordered.move_to_end('Banana')   # Moves 'banana' to the end
print(ordered)                  # Output: OrderedDict([('apple', 3), ('cherry', 5), ('banana', 2)])
