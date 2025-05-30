import tbc

def main():
    hero = tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2

    monster = tbc.Character()
    monster.name = "Monster"
    monster.hitPoints = 20
    monster.hitChance = 30
    monster.maxDamage = 5
    monster.armor = 0

    hero.printStats()
    monster.printStats()

    tbc.fight(hero, monster)

if __name__ == "__main__":
    main()
