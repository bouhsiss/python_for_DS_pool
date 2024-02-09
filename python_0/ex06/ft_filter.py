import sys

def function_to_apply(x):
    return x % 2 == 0

def ft_filter(function_to_apply, list_of_inputs):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function_to_apply :
        return [i for i in list_of_inputs if function_to_apply(i)]
    return [i for i in list_of_inputs if i]