def callLimit(limit: int):
    """a function that takes as argument a call limit of another function \
and blocks its execution above a limit"""
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwargs):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print("Error : " + str(function) + " call too many times")
        return limit_function
    return callLimiter
