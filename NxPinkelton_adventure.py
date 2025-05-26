def makeGame():
    game = {
      "start": ["You wake up in a dark cave. What do you do?", "Check your belongings", "phone", "Start walking", "walk"], 
      "walk": ["You end up tripping and hit your head. You've passed out", "Start over", "start", "Quit", "quit"], 
      "phone": ["You check your pockets and find your phone. What do you do?", "Make a call", "call", "Use your phone's flashlight", "flashlight"], 
      "call": ["You try to make a phone call, but you have no service in the cave. What now?", "Try to use your flashlight instead", "flashlight", "Cry and wallow in sorrow", "cry"], 
      "cry": ["You cried so hard that your eyes are swollen. You've given up.", "Start over", "start", "Quit", "quit"], 
      "flashlight": ["You use your phone's flashlight and started walking forward. You've come across two paths:", "Choose the left path", "leftpath", "Choose the right path", "rightpath"], 
      "leftpath": ["As you go along the left path, you see a giant hole in front of you. What's your move?", "Jump down to reach the bottom", "fall", "Back track", "backtrack"], 
      "fall": ["You start falling. You keep falling. You fall, and you cannot get up.", "Start over", "start", "Quit", "quit"], 
      "backtrack": ["You go back to where the cave splits paths. Where will you go?", "Choose the left path", "leftpath", "Choose the right path", "rightpath"], 
      "rightpath": ["You go along the right path for a while.", "Wait a bit to catch your breath", "breather", "Keep trudging along", "going"], 
      "breather": ["You sit to take a break. Unfortunately, poisonous snakes were following you silently. They got you good.", "Start over", "start", "Quit", "quit"], 
      "going": ["You walk for a long time and you find another crossroads, but your phone dies. Oh no! ", "Wait for a moment so your eyes adjust", "adjust", "Choose a path at random", "random"], 
      "random": ["You walk blindly into the dark and become lost forever.", "Start over", "start", "Quit", "quit"], 
      "adjust": ["Your eyes adjust slightly, but it's still too dark to move. As you star- wait a minute, what's that? There's sound coming from somewhere.", "Head towards the sound", "escape", "Ignore the sound", "ignore"], 
      "ignore": ["You ignore the sound and lose your chance to escape. Dang.", "Start over", "start", "Quit", "quit"], 
      "escape": ["You follow the sound... you see light in the distance... and finally, you have escaped the dark cave! Congratulations!", "Start over", "start", "Quit", "quit"], 
     }
    
    
    return game

    
def playNode(game, currentNode):
    nodeData = game[currentNode]
    description, menu1, node1, menu2, node2 = nodeData
    print(description)
    print(f"1: {menu1}")
    print(f"2: {menu2}")
    
    userChoice = input("Your choice: (1/2): ")
    
    if userChoice == "1":
        nextKey = node1
    elif userChoice == "2":
        nextKey = node2
    else:
        print("Sorry, that's invalid. Try again. ")
        print("")
        nextKey = currentNode
    
    return nextKey


            
def main():
    game = makeGame()
    
    currentNode = "start"
    
    keepGoing = True
    while keepGoing:
        if currentNode == "quit":
            keepGoing = False
        else:
            currentNode = playNode(game, currentNode)
            
main()