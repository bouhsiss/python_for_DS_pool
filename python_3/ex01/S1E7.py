from S1E9 import Character


class Baratheon(Character):
    """
    A class representing a member of House Baratheon, known for their \
strength, ambition, and tumultuous history.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Baratheon character with the given first name and \
default status of being alive.

        Parameters:
            first_name (str): The first name of the Baratheon character.
            is_alive (bool, optional): The status of the character's life. \
Default is True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Sets the status of the Baratheon character to deceased.
        """
        self.is_alive = False

    def __str__(self) -> str:
        """
        Returns a string representation of the Baratheon character.

        Returns:
            str: A descriptive string of the Baratheon character.
        """
        return "I am member of House Baratheon"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Baratheon character.

        Returns:
            str: A representation of the Baratheon character.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """
    A class representing a member of House Lannister, known for their wealth, \
cunning, and the phrase "A Lannister always pays his debts."
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialized a Lannister Character with the given first name and \
default status of being alive.

        Parameters:
            first_name (str): The first name of the Lannister character.
            is_alive (bool, optional): The status of the character's life. \
Default is True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Sets the status of the Lannister character to deceased.
        """
        self.is_alive = False

    def __str__(self) -> str:
        """
        Returns a string representation of the Lannister character.

        Returns:
            str: A descriptive string of the Lannister character.
        """
        return "I am member of House Lannister"

    def __repr__(self) -> str:
        """
        returns a string representation of the Lannister character.

        Returns:
            str: A representation of the Lannister character.
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        creates a Lannister character with the given first name and status of \
being alive.

        Parameters:
            first_name (str): The first name of the Lannister character.
            is_alive (bool, optional): The status of the character's life. \
Default is True.

        Returns:
            Lannister: A new instance of the Lannister class.
        """
        return cls(first_name, is_alive)
