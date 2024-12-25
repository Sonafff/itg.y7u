from les3.berserk import Berserk
from assassin import Assassin
from character import Character

player1 = Character("A", 120, 7, 0)
player1.print_stats()

player2 = Assassin("B", 100, 10, 0)
player2.print_stats()
print("\n")

while player1.health > 0 and player2.health > 0:
    player1_damage = player1.attack(player2)
    print(f"{player1.name} attack {player2.name} and took off {player1.damage} HP")
    print(f"{player2.name} has {player2.health} HP left")

    player2_damage = player2.attack(player1)
    print(f"{player2.name} attack {player1.name} and took off {player2.damage} HP")
    print(f"{player1.name} has {player1.health} HP left")
    print("")

print("\n\n")
player1.print_stats()
player2.print_stats()