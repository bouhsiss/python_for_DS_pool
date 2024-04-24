import numpy as np

def give_bmi(height : list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    This function takes in a list of heights and weights and returns a list of BMI values.
    
    Parameters:
    height : list(int | float) : A list of heights in cm.
    weight : list(int | float) : A list of weights in kg.
    
    Returns:
    list(int | float) : A list of BMI values.
    """
    try :
        height = np.array(height)
        weight = np.array(weight)
        
        bmi = weight / (height / 100) ** 2
    except Exception as e:
        print("Error : " + e)
        bmi = None
    return bmi