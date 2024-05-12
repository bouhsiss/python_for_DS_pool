import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    This function takes in a list of heights and weights and returns a list \
 of BMI values.

    Parameters:
    height : list(int | float) : A list of heights in cm.
    weight : list(int | float) : A list of weights in kg.

    Returns:
    list(int | float) : A list of BMI values.
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise ValueError("height and weight must be a list of integers \
or floats")
        try:
            height = np.array(height)
            weight = np.array(weight)

            bmi = weight / (height ** 2)
        except TypeError:
            raise ValueError("height and weight must be a list of integers \
or floats")
        if height.shape != weight.shape:
            raise ValueError("hieght and weight must be of the same length")
        if (height < 0).any() or (weight < 0).any():
            raise ValueError("height and weight must be positive")
    except ValueError as e:
        print(" An error has occured: ", e)
        return []
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function accepts a list of integers or floats and an integer \
representing a limit as a parameters. It returns a list of booleans \
(True if above the limit).

    Parameters:
    bmi : list(int | float) : A list of BMI values.
    limit : int : An integer representing a limit.

    Returns:
    list(bool) : A list of booleans.
    """
    try:
        if not isinstance(limit, int):
            raise ValueError("limit must be an integer")
        for i in bmi:
            if not isinstance(i, (int, float)):
                raise ValueError("bmi must be a list of integers or floats")
        bmi = np.array(bmi)
        limit = np.array(limit)
        if (bmi < 0).any():
            raise ValueError("bmi must be positive")
    except ValueError as e:
        print("An error has occured: ", e)
        return []
    return (bmi > limit).tolist()
