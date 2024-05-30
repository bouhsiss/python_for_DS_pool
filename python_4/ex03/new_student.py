import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Function to generate a random id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class to represent a student"""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Method to initialize the login attribute of the class"""
        self.login = self.name[0].upper() + self.surname.lower()
