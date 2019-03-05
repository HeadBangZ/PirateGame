from pirates import Pirate
import random

count = random.randint(1, 10)
start = 0
dummy = Pirate("Dummy")
prev = dummy
more = True

print("Enter as many pirates you want, when you want no more pirates just press enter")
print("\n")
print("Count number: " + str(count))
print("\n")

# Game Initialization
def walk_the_plank(next_pirate):
    while next_pirate.getPointer() != next_pirate:
        print("New round: ")
        for i in range(start, count):
            print(next_pirate.setPointer(next_pirate.getPointer())._name)
            prev = next_pirate
            # print(prev._name)
            next_pirate = next_pirate.getPointer()
        prev.setPointer(next_pirate.getPointer())
    print("\nThe winner is: " + prev.setPointer(next_pirate.getPointer())._name)

# Pirate Creation
while more:
    name = input("Enter a name: ")
    if name == "":
        walk_the_plank(next_pirate)
        more = False
    else:
        next_pirate = Pirate(name)
        prev.setPointer(next_pirate)
        prev = next_pirate
    prev.setPointer(dummy.getPointer())




