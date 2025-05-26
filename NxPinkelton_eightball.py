# I am Nathan Pinkelton. We (as in myself) are currently making a Magic 8 ball.
# The first step is importing our random commands and setting up our list of possibilites. Oooh, aaaah.

import random
fortunes = ["Yes", "No", "Maybe", "Possibly", "100%", "Will not happen", "Certainly", "Certainly not", "Absolutely", "Absolutely not", "Perhaps", "There's a chance", "It's looking hopeful", "It's looking doubtful"]


# Setting up the Menu.
print("Welcome to the Mysterious and Magical 8 Ball. What action would you like to take?")
print("1: Print all possible fortunes")
print("2: Print a specific fortune")
print("3: Receive a divinated fortune")
choices = input("Please choose 1, 2, or 3. ")

#Set up if and else statements for options

#Option 1
if choices == "1":
    print("Your Fortunes:")
    for (id, fortune) in enumerate(fortunes):
        print(f"{id}: {fortune}")
        
#Option 2
elif choices == "2":
    specFortune = input("What would you like to see? (0-13) ")
    fortuneNum = int(specFortune)
    fortuneChosen = fortunes[fortuneNum]
    print(f"{fortuneChosen}")

#Option 3
elif choices == "3":
    question = input("Your Question: ")
    randomFortune = random.randrange(14)
    print(f"{fortunes[randomFortune]}")
    
else:
    print("Unfortunately, I cannot help you if you do not choose one of the 3 options provided.")