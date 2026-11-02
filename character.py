# Object-oriented game simulator


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage

    def take_damage(self, amount: int) -> None:
        """Reduce the character's HP."""
        self._hp = max(0, self._hp - amount)

    def heal(self, amount: int) -> None:
        """Increase the character's HP without exceeding maximum HP."""
        self._hp = min(self.hp_max, self._hp + amount)

    def attack(self, target) -> None:
        """Attack and deal damage to target character."""
        target.take_damage(self.damage)

    def introduce(self) -> None:
        """Creates string that introduces character."""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object."""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object."""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Return True if the character is alive, otherwise False."""
        return self._hp > 0







    # Create dice
from dice import Dice
d6 = Dice()
d20 = Dice(sides=20)

# Test __repr__
print(d6)
print(d20)

# Roll using roll()
print("D6 roll:", d6.roll())
print("D20 roll:", d20.roll())

# Roll using __call__()
print("D6 call:", d6())
print("D20 call:", d20())






# Object-oriented game simulator
# INF201, NMBU, 2026

from items import Weapon


class Character:
    """Represents a character in the RPG."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon = None
    ) -> None:
        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, amount: int) -> None:
        """Reduce the character's HP."""
        if amount < 0:
            raise ValueError("Damage cannot be negative.")

        self._hp = max(0, self._hp - amount)

    def heal(self, amount: int) -> None:
        """Restore HP without exceeding maximum HP."""
        if amount < 0:
            raise ValueError("Healing cannot be negative.")

        self._hp = min(self.hp_max, self._hp + amount)

    def attack(self, target) -> None:
        """Attack another character."""
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage

        target.take_damage(damage)

    def introduce(self) -> None:
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        return (
            f"<Character name={self.name} "
            f"hp={self.hp} damage={self.damage}>"
        )

    def __str__(self) -> str:
        return (
            f"Character: {self.name} "
            f"with {self.hp} HP and {self.damage} damage"
        )

    @property
    def hp(self) -> int:
        """Return current HP."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Check whether the character is alive."""
        return self._hp > 0


# TASK 4: Character specialisations


class Warrior(Character):
    """A defensive character specialised in absorbing damage."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        armor: int = 5,
        weapon: Weapon = None
    ) -> None:
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """Reduce incoming damage by the warrior's armor."""
        reduced_damage = max(0, amount - self.armor)
        super().take_damage(reduced_damage)


class Mage(Character):
    """A magical character that uses mana for powerful attacks."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        mana: int = 30,
        mana_max: int = 30,
        weapon: Weapon = None
    ) -> None:
        super().__init__(name, hp_max, damage, weapon)

        self.mana_max = mana_max
        self.mana = min(mana, mana_max)

    def attack(self, target) -> None:
        """Perform a magical attack or a normal attack."""

        if self.mana >= 10:
            # Magical attack: costs 10 mana and deals double damage
            self.mana -= 10
            target.take_damage(self.damage * 2)

        else:
            # Normal attack: uses equipped weapon if available
            super().attack(target)

            # Restore 5 mana, up to the maximum
            self.mana = min(self.mana_max, self.mana + 5)
