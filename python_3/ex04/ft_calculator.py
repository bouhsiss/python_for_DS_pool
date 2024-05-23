class calculator:
    
    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """__ docstring to be written later __ """
        result = sum([x * y for x, y in zip(V1, V2)])
        print("Dot product is: {}".format(result))
        return result

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """__ docstring to be written later __ """
        result = [float(x + y )for x, y in zip(V1, V2)]
        print("Addition of vectors is: {}".format(result))
        return result
    
    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        """__ docstring to be written later __ """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print("Subtraction of vectors is: {}".format(result))
        return result