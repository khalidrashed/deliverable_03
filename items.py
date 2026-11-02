
# Object-oriented game simulator
# INF201, NMBU, 2026

from dice import Dice


class Weapon:
    """Represents a weapon that characters can use."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise a Weapon.

        Args:
            name (str): Name of the weapon.
            damage_dice (Dice): Dice used to calculate damage.
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the weapon's damage dice."""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """Return a string representation of the weapon."""
        return f"Weapon(name={self.name}, damage_dice={self.damage_dice})"






from dice import Dice


class Weapon:
    """Represents a weapon that characters can use."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise a weapon.

        Args:
            name (str): Name of the weapon.
            damage_dice (Dice): Dice used to calculate damage.
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the weapon's damage dice."""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """Return a string representation of the weapon."""
        return (
            f"Weapon(name={self.name}, "
            f"damage_dice={self.damage_dice})"
        )
