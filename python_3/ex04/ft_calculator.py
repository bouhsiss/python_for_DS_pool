class calculator:
    """
    A class representing a calculator that can perform basic arithmetic operations on a vector.
    """
    
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Computes the dot product of two vectors.

        Parameters:
            V1 (list): The first vector.
            V2 (list): The second vector.
        
        Returns:
            float: The dot product of the two vectors.
        """
        result = sum([x * y for x, y in zip(V1, V2)])
        print("Dot product is: {}".format(result))
        return result

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Computes the addition of two vectors.

        Parameters:
            V1 (list): The first vector.
            V2 (list): The second vector.
        
        Returns:
            list: The result of adding the two vectors.
        """
        result = [float(x + y)for x, y in zip(V1, V2)]
        print("Addition of vectors is: {}".format(result))
        return result
    
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Computes the subtraction of two vectors.

        Parameters:
            V1 (list): The first vector.
            V2 (list): The second vector.
        
        Returns:
            list: The result of subtracting the two vectors.
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print("Subtraction of vectors is: {}".format(result))
        return result