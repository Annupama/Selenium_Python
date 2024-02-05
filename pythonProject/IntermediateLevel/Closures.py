# A function that is defined inside another function is known as a nested function.
# Nested functions are able to access variables of the enclosing scope.
# these non-local variables can be accessed only within their scope and not outside their scope.
def outerFunction(text):
    def innerFunction():
        print(text)

    innerFunction()


if __name__ == '__main__':
    outerFunction('Hey!')

# A Closure in Python is a function object that remembers values in enclosing scopes even if they are not present in memory.

def outerFunction(text):
    def innerFunction():
        print(text)

        # Note we are returning function

    # WITHOUT parenthesis
    return innerFunction


if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()


def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

print(transmit_to_space("Test message"))

# Non Local Keyword
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)

# Print odd numbers using Python Closure
def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

# call the outer function
odd = calculate()

# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate()
print(odd2())