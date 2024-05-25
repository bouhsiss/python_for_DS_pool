from abc import ABC, abstractmethod


class Character(ABC):
    """
    An abstract class representing a Game of Thrones character.
    create your own hero, villain, or poor soul who won't survive the next \
episode.
    Valar Morghulis.
    """
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """
    A class representing the Stark family. Or those still alive.
    Winter is coming. but so are loyalty, honor, and a surprising amount of \
direwolves
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Stark Character with the given first name and default \
status of being alive.

        Parameters:
            first_name (str): The first name of the Stark character.
            is_alive (bool, optional): The status of the character's life. \
Default is True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Sets the status of the Stark character to deceased.
        """
        self.is_alive = False
