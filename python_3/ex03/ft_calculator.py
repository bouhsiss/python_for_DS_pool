class calculator:
    """__ docstring to be written later __ """

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        """__ docstring to be written later __ """
        self.vector = [x + object for x in self.vector]
        print(self.vector)
        return self.vector
    
    def __mul__(self, object) -> None:
        """__ docstring to be written later __ """
        self.vector = [x * object for x in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, object) -> None:
        """__ docstring to be written later __ """
        self.vector = [x - object for x in self.vector]
        print(self.vector)
        return self.vector
    
    def __truediv__(self, object) -> None:
        """__ docstring to be written later __ """
        if object == 0:
            print('Division by 0 is not possible')
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
        return self.vector