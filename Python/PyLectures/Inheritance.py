from MyClasses import *

p1 = Person("Thomas")

print(p1.toString())
print("The person can say " + p1.personTalk())

a1 = Adult("Bebe", "Programmer")
print(a1.toString())
print("The adult can say " + a1.adultTalk() + " and " + a1.personTalk())

c1 = Child("Anthony", 2)
print(c1.toString())
print("The child can say " + c1.childTalk() + " and " + c1.personTalk())

fish1 = Fish("Halibut")
print(fish1.toString())
print(fish1.eat())
print(fish1.getType())
print(fish1.swim())
print(fish1.toString())
print(fish1.swim())
print(fish1.toString())
print(fish1.eat())
print(fish1.toString())