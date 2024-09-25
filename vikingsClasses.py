import random


# Soldier Class
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        """
        Subtracts the received damage from the health property.
        """
        self.health -= damage


# Viking Class
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name  # Only set name; health is already set

    def receiveDamage(self, damage):
        """Subtracts the received damage from the health property."""
        result = super().receiveDamage(damage)  # Reuse the parent class method
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        """
        Returns the Viking's battle cry.
        """
        return "Odin Owns You All!"


# Saxon Class

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        """Subtracts the received damage from the health property."""
        result = super().receiveDamage(damage)  # Reuse the parent class method
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        # Select a random Viking and Saxon
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        # Saxon receives damage equal to Viking's strength
        result = saxon.receiveDamage(viking.strength)

        # If the Saxon dies, remove them from the Saxon army
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)

        return result

    def saxonAttack(self):
        # Select a random Viking and Saxon
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        result = viking.receiveDamage(saxon.strength)

        if viking.health <= 0:
            self.vikingArmy.remove(viking)

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.vikingArmy) >= 1 and len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
