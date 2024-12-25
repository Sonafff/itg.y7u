from character import Character
import random

class Assassin(Character):
    def __init__(self, name, health=100, damage=5, defence=0, crit_chance=0.2):
        self.crit_chance = crit_chance

    def attack(self, target):
        if random.random() < self.crit_chance:
            critical_damage = 1000
            print(f"{self.name} uses critical impact and takes away {critical_damage} HP!")
            return target.take_damage(critical_damage)
        else:
            return Character.attack(self, target)