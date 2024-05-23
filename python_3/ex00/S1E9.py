from abc import ABC, abstractmethod


class Character(ABC):
    """__ docstring to be written later__"""
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """ __ docstring to be written later__"""
    def __init__(self, first_name, is_alive=True):
        """__ docstring to be written later__"""
        super().__init__(first_name, is_alive)

    def die(self):
        """__ docstring to be written later__"""
        self.is_alive = False

