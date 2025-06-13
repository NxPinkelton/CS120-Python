# graphicFight
# combines ideas from simpleGE and tbc

import pygame, simpleGE, random

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("mockup_5.png")
        
        self.music = simpleGE.Sound("Dungeon.wav")
        self.music.play()
        
        self.result = "placeholder"
        
        self.enemy = Character(self, name = "enemy")
        self.enemy.setImage("ant_2.png")
        self.enemy.setSize(75, 75)
        self.enemy.reset()
       
        self.hero = Hero(self)
        self.hero.setImage("idle_001_0.png")
        self.hero.setSize(75, 75)
        self.hero.reset()
       
        self.lblHeroStats = simpleGE.MultiLabel()
        self.lblHeroStats.textLines = self.hero.getStats()
        self.lblHeroStats.center = (150, 350)
        self.lblHeroStats.size = (200, 170)
        self.lblHeroStats.bgColor = "lightblue"

        self.lblEnemyStats = simpleGE.MultiLabel()
        self.lblEnemyStats.textLines = self.enemy.getStats()
        self.lblEnemyStats.center = (500, 350)
        self.lblEnemyStats.size = (200, 170)
        self.lblEnemyStats.bgColor = "pink"
       
        self.sprites = [self.lblHeroStats,
                        self.lblEnemyStats,
                        self.enemy, self.hero
                        ]
       
    def process(self):
        if self.hero.collidesWith(self.enemy):
            self.hero.hit(self.enemy)
            self.enemy.hit(self.hero)
            self.enemy.reset()
           
            self.lblHeroStats.textLines = self.hero.getStats()
            self.lblEnemyStats.textLines = self.enemy.getStats()
           
            if self.enemy.hitPoints <= 0:
                print("hero wins")
                self.result = "win"
                self.stop()
            if self.hero.hitPoints <= 0:
                print ("enemy wins")
                self.result = "lose"
                self.stop()

       
class Character(simpleGE.Sprite):
    def __init__(self, scene,
                 name = "rando",
                 hitPoints = 10,
                 hitPerc = 30,
                 maxDamage = 3,
                 armor = 0):
        super().__init__(scene)
        self.name = name
        self.hitPoints = hitPoints
        self.hitPerc = hitPerc
        self.maxDamage = maxDamage
        self.armor = armor
        
        self.hitSnd = simpleGE.Sound("HitSound.wav")
        self.missSnd = simpleGE.Sound("missHit.wav")
       
    def hit(self, enemy):
        if random.randint(1, 100) < self.hitPerc:
            print (f"{self.name} hits {enemy.name}...")
            damage = random.randint(1, self.maxDamage)
            print (f"  for {damage} points of damage...")
            damage -= enemy.armor
            self.hitSnd.play()
            if damage < 0:
                damage = 0
            if enemy.armor > 0:
                print(f"  but {enemy.name}'s armor absorbs {enemy.armor} points")
            enemy.hitPoints -= damage
        elif random.randint(1, 100) >= self.hitPerc:
            print(f"{self.name} misses {enemy.name}")
            self.missSnd.play()
           
           
    def getStats(self):
        stats = [
            f"Name:       {self.name}",
            f"Hit Points: {self.hitPoints}",
            f"Hit Perc:   {self.hitPerc}",
            f"Max Damage: {self.maxDamage}",
            f"Armor:      {self.armor}"
        ]
        return stats
   
    def reset(self):
        self.x = random.randint(0, self.screenWidth)
        self.y = random.randint(0, self.screenHeight)
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)

class Hero(Character):
    """ just like character,
        but with motion ability
        slightly different defaults"""
   
    def __init__(self, scene,
                 name = "hero",
                 hitPoints = 10,
                 hitPerc = 50,
                 maxDamage = 3,
                 armor = 0):
        super().__init__(scene, name, hitPoints, hitPerc, maxDamage, armor)
        self.moveSpeed = 5
       
       
    def process(self):
        #cancel auto-move. Use arrows instead
        self.dx = 0
        self.dy = 0
       
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed


class EndScreen(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.winMusic = simpleGE.Sound("winMusic1.wav")
        self.loseMusic = simpleGE.Sound("loseMusic1.wav")
        
        self.BtnResponse = "Holder"
        
        self.endLabel = simpleGE.Label()
        self.endLabel.center = (300, 100)
        self.endLabel.text = "Holder"
        
    
        self.startOvrBtn = simpleGE.Button()
        self.startOvrBtn.text = "Start Over"
        self.startOvrBtn.center = (150, 300)
    
        self.quitBtn = simpleGE.Button()
        self.quitBtn.text = "Quit"
        self.quitBtn.center = (450, 300)
    
        self.sprites = [self.endLabel,
                        self.startOvrBtn,
                        self.quitBtn]
    def process(self):
        if self.startOvrBtn.clicked:
            self.BtnResponse = "start"
            self.stop()
        elif self.quitBtn.clicked:
            self.BtnResponse = "quit"
            self.stop()
        
        if self.endLabel.text == "You Win!":
            self.winMusic.play()
        elif self.endLabel.text == "You Lose...":
            self.loseMusic.play()


def main():
    
    game = Game
    end = EndScreen()
    
    keepGoing = True
    
    
    while keepGoing:
        
        
        if end.BtnResponse == "quit":
            keepGoing = False
        else:
            game = Game()
            game.start()
        
        result = game.result
        
        if result == "win":
            resultText = "You Win!"
        elif result == "lose":
            resultText = "You Lose..."
    
        end = EndScreen()
        end.endLabel.text = resultText
        end.start()
    
    
        
   
if __name__ == "__main__":
    main()