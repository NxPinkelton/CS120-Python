""" cards.py
    demonstrates functions
    manage a deck of cards db

"""
import random
NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
HANDS = ("deck", "player", "computer")

DECK = 0
PLAYER = 1
COMPUTER = 2

def main():
    cardDB = initCards() #Build cards

    for i in range(5):
        assignCard(cardDB, PLAYER)
        assignCard(cardDB, COMPUTER)

    showDB(cardDB) # show the cards

    showHand(cardDB, PLAYER)
    showHand(cardDB, COMPUTER)
    
def initCards():
    cardDB = []
    for i in range(NUMCARDS):
        cardDB.append(0)
    
    return cardDB

def showDB(cardDB):
    print("The deck of cards: ")
    for cardNum, location in enumerate(cardDB):
        print(f"{cardNum}: {getCardName(cardNum)}, {HANDS[location]}")

def getCardName(cardNum):
    suit = cardNum // 13
    rank = cardNum % 13
    cardName = str(f"{RANKNAME[rank]} of {SUITNAME[suit]}")

    return cardName

def assignCard(cardDB, hand):
    cardNum = random.randrange(NUMCARDS)
    cardDB[cardNum] = hand
    

def showHand(cardDB, hand):
    print("")
    print(f"Cards in {HANDS[hand]} hand:\n")
    for cardNum, location in enumerate(cardDB):
        if location == hand:
            print(f"{getCardName(cardNum)}")
        
    

main()
        