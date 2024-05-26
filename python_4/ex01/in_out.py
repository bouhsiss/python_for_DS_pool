def square(x: int | float) -> int | float:
    """ a function that takes in a number and returns the square of it """
    return x ** 2

def pow(x: int | float) -> int | float:
    """ a function that takes a number and returns the exponentiation of it """
    return x ** x

def outer(x: int | float, function) -> object:
    """ a function that takes as argument a number and a function and returns an object that when called returns the result of the arguments calculation"""
    count = 0
    def inner() -> float:
        try :
            nonlocal count
            count += 1
            ret = x
            for i in range(count):
                ret = function(ret)
            return ret
        except Exception as e :
            print("An error has occured : ", e)
    return inner


my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
del outer
print(another_counter())
print(another_counter())
print(another_counter())
print(another_counter.__code__.co_freevars)
print(another_counter.__closure__[0]. cell_contents)
print(another_counter.__closure__[1]. cell_contents)
print(another_counter.__closure__[2]. cell_contents)
