
# Object-oriented game simulator
# INF201, NMBU, 2026

from character import Character


class Battle:
    """Manages turn-based combat between two characters."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Initialise a battle.

        Args:
            hero (Character): The hero character.
            enemy (Character): The enemy character.
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Play one round of combat."""

        # Hero attacks first if alive
        if self.hero.is_alive:
            self.hero.attack(self.enemy)

        # Enemy attacks if still alive
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Run the battle until one character is defeated."""

        print(f"Battle starts: {self.hero.name} vs {self.enemy.name}")

        round_number = 1

        while self.hero.is_alive and self.enemy.is_alive:
            print(f"\n--- Round {round_number} ---")

            self.play_round()

            print(f"{self.hero.name}: {self.hero.hp} HP")
            print(f"{self.enemy.name}: {self.enemy.hp} HP")

            round_number += 1

        # Announce the winner
        print("\n--- Battle finished ---")

        if self.hero.is_alive:
            print(f"{self.hero.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")



if __name__ == "__main__":
    from items import Weapon
    from character import Warrior, Mage
    from dice import Dice

    sword = Weapon("Sword", Dice(8))
    staff = Weapon("Magic Staff", Dice(6))

    hero = Warrior("Aragorn", 100, 15, armor=5, weapon=sword)
    enemy = Mage("Gandalf", 80, 20, mana=30, weapon=staff)

    battle = Battle(hero, enemy)
    battle.simulate_battle()

    


from character import Character


class Battle:
    """Manages turn-based combat between two characters."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Initialise a battle.

        Args:
            hero (Character): The hero character.
            enemy (Character): The enemy character.
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Play one round of combat."""

        # Hero attacks first
        if self.hero.is_alive:
            self.hero.attack(self.enemy)

        # Enemy attacks only if still alive
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Run the battle until one character is defeated."""

        print(
            f"Battle starts: {self.hero.name} "
            f"vs {self.enemy.name}"
        )

        round_number = 1

        while self.hero.is_alive and self.enemy.is_alive:

            print(f"\n--- Round {round_number} ---")

            self.play_round()

            print(f"{self.hero.name}: {self.hero.hp} HP")
            print(f"{self.enemy.name}: {self.enemy.hp} HP")

            round_number += 1

        print("\n--- Battle finished ---")

        if self.hero.is_alive:
            print(f"{self.hero.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")
