# Nathan Pinkelton
# Mad Lib Project
# 5/12/2025
# I will be Mad-libbing with the user's inputs. The base of my story comes from the lyrics of "Baa-Baa Black Sheep"

# Replace lyrics with string variables that need input 

# List of string variables in order of when they are used: <animalNoise>, <adjective1>, <animal1>, <item>, <name>, <number>, <storage>, <animal2>, <name2>, <adjective2>, <nickname>, <place>.

# Create a string variable called animalNoise. Prompt "Please enter a noise an animal would make" 


animalNoise = input("Please enter a noise an animal would make. ")

# Create string variables with the same names as listed above. All will start empty. All will prompt the user to provide an input for what the variable is named

adjective1 = input("Please enter an adjective. ")
animal1 = input("Please enter an animal. ")
item = input("Please enter a random item. ")
name = input("Please enter a name. ")
number = input("Please enter a number. ")
storage = input("Please enter something that is used for storage. ")
animal2 = input("Please enter another animal. ")
name2 = input("Please enter another name. ")
adjective2 = input("Please enter another adjective. ")
nickname = input("Please enter a nickname. ")
place = input("Please enter a place. ")

# Follow the lyrics of the nursery rhyme. Replace lyrics with the string variables. Use print and printf function

print(" ")
print(f"{animalNoise} {animalNoise}, {adjective1} {animal1}, have you any {item}? ")
print(f"Yes {name}, yes {name}, {number} {storage}'s full! ")
print(f"Some for the {animal2}, some for the {name2}, ")
print(f"Some for the {adjective2} {nickname} who lives in {place}. ")
print(f"{animalNoise} {animalNoise} {animal1}, have you any {item}? ")
print(f"Yes {name}, yes {name}, {number} {storage} full! ")
print(" ") 