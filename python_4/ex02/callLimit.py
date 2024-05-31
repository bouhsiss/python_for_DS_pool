def callLimit(limit: int):
    """Creates a decorator that limits the number of times a function can be \
called

    Parameters:
    limit: int : the number of times the function can be called

    Returns:
    function : A decorator function that wraps the target function and \
enforces the call limit
    """
    count = 0

    def callLimiter(function):
        """Wraps the given function to enforce a call limit

        Parameters:
        function : function : the function to be wrapped and limited

        Returns:
        function: A wrapped version of the input function that will only \
exceute up to the limit.
        """
        def limit_function(*args, **kwargs):
            """
            Executes the wrapped function if the call limit has not been \
reached.

            Parameters:
            args : tuple : the positional arguments to be passed to the \
wrapped function
            kwargs : dict : the keyword arguments to be passed to the wrapped \
function

            Returns:
            The result of the wrapped function if the call limit has not been \
reached.
            Prints an error message if the call limit has been reached.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print("Error : " + str(function) + " call too many times")
        return limit_function
    return callLimiter
