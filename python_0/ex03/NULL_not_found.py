import math


def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None", type(object))
    elif isinstance(object, (int, float)) and math.isnan(object):
        print("Cheese: nan", type(object))
    elif object == 0:
        print("Zero:", object, type(object))
    elif object == '':
        print("Empty:", type(object))
    elif object is False:
        print("Fake:", object, type(object))
    else:
        print("Type not Found")
        return 1
    return 0