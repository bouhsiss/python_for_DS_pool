def square(x: int | float) -> int | float:
    """ a function that takes in a number and returns the square of it """
    return x ** 2


def pow(x: int | float) -> int | float:
    """ a function that takes a number and returns the exponentiation of it """
    return x ** x


def outer(x: int | float, function) -> object:
    """ a function that takes as argument a number and a function and returns \
an object that when called returns the result of the arguments calculation"""
    count = 0

    def inner() -> float:
        """ a function that returns the result of the calculation of the \
arguments """
        try:
            nonlocal count
            count += 1
            ret = x
            for _ in range(count):
                ret = function(ret)
            return ret
        except Exception as e:
            print("An error has occured : ", e)
    return inner
