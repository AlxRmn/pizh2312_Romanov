from random import randint

class Unit():
    count = 0
    def __init__(self, team):
        self.id = Unit.count
        Unit.count += 1
        self.team = team
        
class Hero(Unit):
    def __init__ (self, team):
        Unit.__init__(self, team)
        self.lvl = 1
    def up_lvl(self):
        self.lvl += 1

class Fighter(Unit):
    def __init__(self, team):
        Unit.__init__(self, team)

    def follow_hero(self, hero):
        print(f"Солдат {self.id} следует за Героем {hero.id}")

team1_fighters = []
team2_fighters = []

hero1 = Hero("Команда 1")
hero2 = Hero("Команда 2")

for i in range(20):
    team = randint(1, 2)
    fighter = Fighter("Команда 1" if team == 1 else "Команда 2")
    if team == 1:
        team1_fighters.append(fighter)
    else:
        team2_fighters.append(fighter)

if len(team1_fighters) > len(team2_fighters):
    hero1.up_lvl()
else:
    hero2.up_lvl()

if team1_fighters:
    team1_fighters[0].follow_hero(hero1)
    print(f"Солдат: {team1_fighters[0].id}, Герой: {hero1.id}")
