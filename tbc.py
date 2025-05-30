"""Turn Based Combat System
We'll define Character class and a fight function, as well as a print stats function"""


import random

class Character(object):
    
    def __init__(self):
        super().__init__()
        self.name = "Hero"
        self.hitPoints = 100
        self.hitChance = 50
        self.maxDamage = 1
        self.armor = 0
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        if type(value) == int:
            if value > 0:
                self.__hitPoints = value
            else:
                print(f"{self.name}'s HP must be higher than 0")
                self.__hitPoints = 10
        else:
            print("{self.name}'s HP must be a number")
            self.__hitPoints = 10

    
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        if type(value) == int:
            if value > 0:
                if value <= 100:
                    self.__hitChance = value
                else:
                    print("{self.name}'s Hit Chance cannot be greater than 100")
            else:
                print("{self.name}'s Hit Chance must be greater than 0")
                self.__hitChance = 50
        else:
            print("{self.name}'s Hit Chance must be a number")
            self.__hitChance = 50
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        if type(value) == int:
            if value > 0:
                self.__maxDamage = value
            else:
                print("{self.name}'s Max damage must be bigger than 0")
                self.__maxDamage = 1
        else:
            print("{self.name}'s Max damage must be a number")
            self.__maxDamage = 1
    
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        if type(value) == int:
            if value >= 0:
                #if value < oppmaxDamage:
                self.__armor = value
                #else:
                    #print("Armor cannot be more than opponent's max damage.")
                    #self.__armor = 0
            else:
                print("{self.name}'s Armor cannot be below zero")
                self.__armor = 0
        else:
            print("{self.name}'s Armor must be a number")
            self.__armor = 0
        

    def printStats(self):
        print(f"{self.name}")
        print("=================\n")
        print(f"Hit Points: {self.hitPoints}")
        print(f"Hit Chance: {self.hitChance}")
        print(f"Max Damage: {self.maxDamage}")
        print(f"Armor: {self.armor}\n")
    
def fight(self, Character):
    sHealth = self.hitPoints
    cHealth = Character.hitPoints
    keepGoing = True
    while keepGoing:
        input("Press 'ENTER' to continue")
        sDiceRoll = random.randint(0, 100)
        if sDiceRoll <= self.hitChance:
            sDamage = random.randint(1, self.maxDamage)
            sDamage = sDamage - Character.armor
            if sDamage <= 0:
                print("")
                print(f"{Character.name} blocked {self.name}'s attack with it's armor!")
            else:
                cHealth = cHealth - sDamage
                print("")
                print(f"{self.name} hit {Character.name} for {sDamage} damage!")
        else:
            print("")
            print(f"{self.name} missed their attack!")
        
        cDiceRoll = random.randint(0, 100)
        if cDiceRoll <= Character.hitChance:
            cDamage = random.randint(1, Character.maxDamage)
            cDamage = cDamage - self.armor
            if cDamage <= 0:
                print("")
                print(f"{self.name} blocked {Character.name}'s attack with it's armor!")
            else:
                sHealth = sHealth - cDamage
                print("")
                print(f"{Character.name} hit {self.name} for {cDamage} damage!")
        else:
            print("")
            print(f"{Character.name} missed their attack!")
        
        print("")
        print(f"{self.name}'s Health: {sHealth}")
        print(f"{Character.name}'s Health: {cHealth}")
        print("")
        
        if sHealth <= 0:
            print(f"{self.name} has fallen! {Character.name} wins the battle!")
            keepGoing = False
        if cHealth <= 0:
            print(f"{Character.name} has fallen! {self.name} wins the battle!")
            keepGoing = False
        elif sHealth <= 0 and cHealth <= 0:
            print(f"Both {self.name} and {Character.name} have fallen! The battle ends in a Draw.")
            
        


    
def main():
    hero = Character()
    hero.name = "Dog"
    hero.hitPoints = 20
    hero.hitChance = 100
    hero.maxDamage = 10
    hero.armor = 2
    
    other = Character()
    other.name = "Cat"
    other.hitPoints = 20
    other.hitChance = 100
    other.maxDamage = 10
    other.armor = 2
    
    
    hero.printStats()
    other.printStats()
    
    fight(hero, other)
    
if __name__ == "__main__":
    main()
        
