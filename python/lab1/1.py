from random import randint

class Fighter: 
    def makeHealth(self, health):
        self.health = health
    def makeKick(enemy):
        enemy.health -= 20

class Fight: 
    def fight(self, f1, f2):
        while f1.health > 0 and f2.health > 0:
            num = randint(1, 2)
            if num == 1:
                Fighter.makeKick(f2)
                print("Воин 1 совершил атаку")
                print (f"Воин 2 имеет {f2.health} здоровья")
            else:
                Fighter.makeKick(f1)
                print("Воин 2 совершил атаку")
                print (f"Воин 1 имеет {f1.health} здоровья")
        if f1.health > f2.health:
            print("Победил воин 1")
        else:
            print("Победил воин 2")

fighter1 = Fighter()
fighter2 = Fighter()
fighter1.makeHealth(100)
fighter2.makeHealth(100)

fight1 = Fight()
fight1.fight(fighter1, fighter2)

