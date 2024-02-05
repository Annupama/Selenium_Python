# Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class.
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

#  Treating the functions as objects.
def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))

# Passing the function as an argument

def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)

# Returning functions from another function.

def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10)) 