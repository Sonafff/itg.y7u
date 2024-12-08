from character import Character

player1 = Character(name="lizo", health=120, damage=7, defence=0)
player1.print_stats()

player2 = Character(name="Kriss", health=100, damage=10, defence=0)
player2.print_stats()

player1.attack(player2)

print("\n\n")
player1.print_stats()
player2.print_stats()