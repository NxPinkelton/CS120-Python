import random

randomNumber = random.randint(1, 100)
prompt = print("Try and guess my number! It's between 1 and 100")

numGuesses = 0
keepGoing = True

while keepGoing:
    numGuesses += 1
    guess = input(f"{numGuesses}) What is your guess? ")
    guessNum = int(guess)
    if guessNum < randomNumber:
        print("Too low")
    if guessNum > randomNumber:
        print("Too high")
    if guessNum == randomNumber:
        print(f"You got it in {numGuesses} turns!")
        print("You Win!!!")
        keepGoing = False
# this bottom one is elif to make sure that, on the 7th guess, "you lose" doesn't get printed if you get it correct.
    elif numGuesses > 6:
        print("You were not able to guess correctly within 7 turns...")
        print("You lose.")
        keepGoing = False
    
        
