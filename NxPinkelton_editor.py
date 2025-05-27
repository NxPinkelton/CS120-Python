import json
def main():
    
    defaultGame = getDefaultGame()
    
    currentNode = "start"
    
    keepGoing = True
    while keepGoing:
        menuChoice = getMenuChoice()
        if menuChoice == "0":
            keepGoing = False
        elif menuChoice == "1":
            getDefaultGame()
            defaultGame = getDefaultGame()
            print("Default game has been loaded\n")
        elif menuChoice == "2":
            loadGame(defaultGame)
        elif menuChoice == "3":
            saveGame(defaultGame)
        elif menuChoice == "4":
            editNode(defaultGame, currentNode)
        elif menuChoice == "5":
            playGame(defaultGame, currentNode)
        else:
            print("Please type in a valid input. ")
    
    
    
def getMenuChoice():
    print("Menu options:")
    print("0) exit")
    print("1) load default game")
    print("2) load a game file")
    print("3) save the current game")
    print("4) edit or add a node")
    print("5) play the current game")
    menuChoice = input("What will you do? ")
    
    return menuChoice

def getDefaultGame():
    defaultGame = {"start": ["Default start node", "Start over", "start", "Quit", "quit"]}
    
    return defaultGame

def playNode(defaultGame, currentNode):
    nodeData = defaultGame[currentNode]
    description, menu1, node1, menu2, node2 = nodeData
    
    print(description)
    print(f"1: {menu1}")
    print(f"2: {menu2}")
    
    userChoice = input("What is your choice? (1/2) ")
    
    if userChoice == "1":
        nextKey = node1
    elif userChoice == "2":
        nextKey = node2
    else:
        print("Invalid choice, Please try again.")
        
    return nextKey

def playGame(defaultGame, currentNode):
    
    keepGoing = True
    while keepGoing:
        if currentNode == "quit":
            keepGoing = False
        else:
            currentNode = playNode(defaultGame, currentNode)
    return

def saveGame(defaultGame):
    saveFile = open("defaultGame.json", "w")
    json.dump(defaultGame, saveFile, indent=2)
    saveFile.close()
    print("Game has been saved.\n")
    
    return

def loadGame(defaultGame):
    loadFile = open("defaultGame.json", "r")
    defaultGame = json.load(loadFile)
    loadFile.close()
    print("Game has been loaded.\n")
    
    
    return defaultGame

def editField(defaultGame, currentNode):
    fieldData = defaultGame[currentNode]
    description, menu1, node1, menu2, node2 = fieldData
    descriptionChange = input(f"Description ({description}): ")
    if descriptionChange == "":
        print("no change made.\n")
    else:
        description = descriptionChange
    menu1Change = input(f"Menu 1 ({menu1}): ")
    if menu1Change == "":
        print("no change made.\n")
    else:
        menu1 = menu1Change
    node1Change = input(f"Node 1 ({node1}): ")
    if node1Change == "":
        print("no change made.\n")
    else:
        node1 = node1Change
    menu2Change = input(f"Menu 2 ({menu2}): ")
    if menu2Change == "":
        print("no change made.\n")
    else:
        menu2 = menu2Change
    node2Change = input(f"Node 2 ({node2}): ")
    if node2Change == "":
        print("no change made.\n")
    else:
        node2 = node2Change
    fieldData = description, menu1, node1, menu2, node2
    defaultGame[currentNode] = fieldData
    
    return defaultGame

def editNode(defaultGame, currentNode):
    print("Current Content:")
    print(json.dumps(defaultGame, indent=2))
    print("Current list of nodes:")
    for key in defaultGame:
        print(f"'{key}' ")
    newNode = input("Name of node you wish to edit or add: ")
    if newNode == key:
        currentNode = newNode
        editField(defaultGame, currentNode)
    else:
        description = input("Description (): ")
        menu1 = input("Menu 1 (): ")
        node1 = input("Node 1 (): ")
        menu2 = input("Menu 2 (): ")
        node2 = input("Node 2 (): ")
        defaultGame[newNode] = description, menu1, node1, menu2, node2

    return defaultGame

main()