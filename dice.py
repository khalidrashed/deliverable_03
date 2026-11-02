import random

class Dice:
    """Represents an n-sided dice."""

    def __init__(self, sides: int = 6) -> None:
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")

        self.sides = sides

    def roll(self) -> int:
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        return self.roll()


# Object-oriented game simulator
# INF201, NMBU, 2026

import random


class Dice:
    """Represents an n-sided dice."""

    def __init__(self, sides: int = 6) -> None:
        """
        Initialise a dice.

        Args:
            sides (int): Number of sides (default = 6).
        """
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")

        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a random number."""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Return a string representation of the dice."""
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Allow the dice object to be called directly."""
        return self.roll()
