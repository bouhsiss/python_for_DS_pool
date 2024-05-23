from abc import ABC, abstractmethod


class Character(ABC):
    """
    An abstract class representing a Game of Thrones character.
    create your own hero, villain, or poor soul who won't survive the next episode.
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
    Winter is coming. but so are loyalty, honor, and a surprising amount of direwolves
    """
    def __init__(self, first_name, is_alive=True):
        """__ docstring to be written later__"""
        super().__init__(first_name, is_alive)

    def die(self):
        """__ docstring to be written later__"""
        self.is_alive = False

