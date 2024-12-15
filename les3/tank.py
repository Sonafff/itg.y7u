from les2.character import Character


class Tank(Character):
    defence_multiplier = 2
    chet_limit = 1

    def __init__(self, name, health=100, damage=10, defence=0,
                 defence_multiplier = 1.5, chet_limit = 1):
        Character.__init__(self, name, health, damage, defence)
        self.defence_multiplier = defence_multiplier
        self.chet_limit = chet_limit

        # def defence(self):
            # final_damage =