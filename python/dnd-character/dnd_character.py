from random import randrange

def modifier(score):
    return (score - 10) // 2

class Character:
    def __init__(self):
        self.strength       = self.ability()
        self.dexterity      = self.ability()
        self.constitution   = self.ability()
        self.intelligence   = self.ability()
        self.wisdom         = self.ability()
        self.charisma       = self.ability()
        self.hitpoints      = 10 + modifier(self.constitution)
    def ability(self):
        return sum(sorted([randrange(1,7) for x in range(4)])[1:])
