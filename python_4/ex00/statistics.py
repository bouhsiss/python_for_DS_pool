import math


def calculate_mean(data: list) -> float:
    """ a function that takes in a list of numbers and returns the mean """
    return sum(data) / len(data)


def calculate_median(data: list) -> float:
    """ a function that takes in a list of numbers and returns the median """
    data.sort()
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    return data[n // 2]


def calculate_quartiles(data: list) -> tuple:
    """ a function that takes in a list of numbers and returns the \
25% and 75% quartiles """
    data.sort()
    n = len(data)
    q1 = data[n // 4]
    q3 = data[3 * n // 4]
    return (float(q1), float(q3))


def calculate_var(data: list) -> float:
    """ a function that takes in a list of numbers and returns the variance """
    mean = calculate_mean(data)
    variance = sum([(x - mean) ** 2 for x in data]) / len(data)
    return variance


def calculate_std(data: list) -> float:
    """ a function that takes in a list of numbers and returns the standard \
deviation """
    return math.sqrt(calculate_var(data))


def ft_statistics(*args: any, **kwargs: any) -> None:
    """ a function that takes in *args and make the Mean, Median, Quartiles \
(25% and 75%), Standard Deviation and Variance of the data, according to the \
what **kwargs asks for """
    try:
        # define an operations dict
        operations_dict = {
            "mean": calculate_mean,
            "median": calculate_median,
            "quartile": calculate_quartiles,
            "std": calculate_std,
            "var": calculate_var
        }
        for key, value in kwargs.items():
            if ((len(args) == 0)):
                print("ERROR")
            else:
                if value in operations_dict.keys():
                    print(f"{value}:", operations_dict[value](list(args)))
    except Exception as e:
        print("An error has occurred: ", e)
