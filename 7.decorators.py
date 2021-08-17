# Decorators


def uppercase_decorator(function):
    def wrapper():
        words = function()
        words = str(words)
        print(words.upper())  
    return wrapper


@uppercase_decorator
def say_hi():
     return 'hi'


say_hi()