from abc import ABC


class Pokemon (ABC):
    def __init__(self, name, power, color, owner):
        self.name = name
        self.power = power
        self. color = color
        self.owner = owner

    def attack(self):
        pass


class Pikachu(Pokemon):

    myattack = 'fire'

    def __init__(self, name, power, color, owner,battle_won):
        super().__init__(name, power, color, owner, battle_won)
        self.battle_won = battle_won

    def attack(self):
        return self.myattack

p1 = Pikachu("Pikachu", "fire", "yellow", "ash ketchp" , "12")
p1.attack()
print(p1.attack())