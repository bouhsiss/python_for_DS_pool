from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    A class representing a king in the world of Game of Thrones, inheriting \
traits from both House Baratheon and House Lannister.
    """

    def set_eyes(self, eyes):
        """
        Set the eye color of the King.

        Parameters:
            eyes (str): The eye color of the King.
        """
        self.eyes = eyes

    def set_hairs(self, hairs):
        """
        Set the hair color of the King.

        Parameters:
            hairs (str): The hair color of the King.
        """
        self.hairs = hairs

    def get_eyes(self):
        """
        Get the eye color of the King.

        Returns:
            str: The eye color of the King.
        """
        return self.eyes

    def get_hairs(self):
        """
        Get the hair color of the King.

        Returns:
            str: The hair color of the King.
        """
        return self.hairs
