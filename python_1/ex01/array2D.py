import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    this function takes as a parameter a 2D array, prints its shape, and \
returns a truncated version of the array based on the provided start \
and end arguments.

    Parameters:
    family : list : A 2D array.
    start : int : The starting index.
    end : int : The ending index.

    Returns:
    list : A truncated version of the array.
    """
    try:
        if (not isinstance(family, list) or
                not isinstance(start, int) or
                not isinstance(end, int)):
            raise AssertionError("family must be a list, start and end must \
be integers")

        if not all(isinstance(i, list) for i in family):
            raise AssertionError("all elements of family must be lists")

        try:
            np_family = np.array(family)
        except ValueError:
            raise AssertionError("all sublists must have the same length")
        if np_family.ndim != 2:
            raise AssertionError("family must be a 2D array")

        print("My shape is: ", np_family.shape)
        truncated_family = np_family[start:end]
        print("My new shape is: ", truncated_family.shape)
        return truncated_family.tolist()
    except AssertionError as e:
        print("An error has occured: ", e)
        return []
