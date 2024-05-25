class calculator:
    """
    A simple calculator class that can perform basic arithmetic operations on \
a vector.
    """

    def __init__(self, vector):
        """
        Initializes the calculator with a vector.

        Parameters:
            vector (list): A list of numbers to perform arithmetic \
operations on.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Adds a number to each element in the vector.

        Parameters:
            object (int): The number to add to each element in the vector.
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """
        Multiplies each element in the vector by a number.

        Parameters:
            object (int): The number to multiply each element in the vector by.
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """
        Subtracts a number from each element in the vector.

        Parameters:
            object (int): The number to subtract from each element in the \
vector.
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """
        Divides each element in the vector by a number.

        Parameters:
            object (int): The number to divide each element in the vector by.
        """
        self.vector = [x / object if object != 0 else float("NaN")
                       for x in self.vector]
        print(self.vector)
