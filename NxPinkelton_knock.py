# Nathan Pinkelton
# 5/13/2025

# This code will run a knock-knock joke for the user

# Variables used (in order of when they are used): <name> , <knock> , <whosThere> <woo>

# I'm not sure how to make the code pick up any string that starts with "Y" and still run correctly
# Coming up with every sentence and phrase doesn't seem practical, but at the moment, the beginning only runs if "Y" or "y" is typed in.
# 

name = input("Hello! What's your name? \n")

knock = input(f"Nice to meet you {name}! Would you like to hear a joke (Y/N)? ")
if knock.startswith("Y"):
    print("Knock Knock") 
    whosThere = input("")
    if whosThere == "Who's there?":
        print("Woo")
        woo = input("")
        if woo == "Woo who?":
            print("I want to have fun too :(")
        elif woo == "woo who?":
            print("I want to have fun too :(")
        else:
            print("Could you just say 'Woo who?' Please?")
    elif whosThere == "who's there?":
        print("Woo")
        woo = input("")
        if woo == "Woo who?":
            print("I want to have fun too :(")
        elif woo == "woo who?":
            print("I want to have fun too :(")
        else:
            print("Could you just say 'Woo who?' Please?")
    else:
        print("You're supposed to say 'Who's there?'")

elif knock.startswith("y"):
    print("Knock Knock") 
    whosThere = input("")
    if whosThere == "Who's there?":
        print("Woo")
        woo = input("")
        if woo == "Woo who?":
            print("I want to have fun too :(")
        elif woo == "woo who?":
            print("I want to have fun too :(")
        else:
            print("Could you just say 'Woo who?' Please?")
    elif whosThere == "who's there?":
        print("Woo")
        woo = input("")
        if woo == "Woo who?":
            print("I want to have fun too :(")
        elif woo == "woo who?":
            print("I want to have fun too :(")
        else:
            print("Could you just say 'Woo who?' Please?")
    else:
        print("You're supposed to say 'Who's there?'")
else:
    print("aw, okay...")
