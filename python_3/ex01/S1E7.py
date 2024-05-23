from S1E9 import Character


class Baratheon(Character):
    """__ docstring to be written later__"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """__ docstring to be written later__"""
        self.is_alive = False

    def __str__(self) -> str:
        return f"i can write whatever i want here since it's only intended for the user to read it."
    
    def __repr__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    hehe = "hehe"
    """__ docstring to be written later__"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    
    def die(self):
        """__ docstring to be written later__"""
        self.is_alive = False

    def __str__(self) -> str:
        return f"i can write whatever i want here since it's only intended for the user to read it."

    def __repr__(self) -> str:
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)