import pickle
from Classes import *

# write and read a text file
outfile = open("myinfo", "w")
outfile.write("Name: Thomas Nordvig Hermansen\n")
outfile.write("Age: " + str(28))
outfile.close()

infile = open("myinfo", "r")
line = infile.readline()
while line != "":
    print(line)
    line = infile.readline()
infile.close()
print()

# write and read a single object
o1 = Owner(1, "Jack")
one_ownerfile = open("ownerfile", "wb")
pickle.dump(o1, one_ownerfile)
one_ownerfile.close()

one_ownerfile = open("ownerfile", "rb")
new_o1 = pickle.load(one_ownerfile)
print(new_o1.toString())
print()

# write and read a list of objects
o1 = Owner(1, "Jack")
o2 = Owner(2, "Thomas")
o3 = Owner(3, "Anthony")

owner_arr = []
owner_arr.append(o1)
owner_arr.append(o2)
owner_arr.append(o3)

arr_ownerfile = open("ownerlist", "wb")
pickle.dump(owner_arr, arr_ownerfile)
arr_ownerfile.close()

arr_ownerfile = open("ownerlist", "rb")
new_ownerlist = pickle.load(arr_ownerfile)

for i in range(len(new_ownerlist)):
    print(new_ownerlist[i].toString())
print()

# list of objects with references
o1 = Owner(2, "Thomas")
o2 = Owner(3, "Anthony")

owner_arr = []
owner_arr.append(o1)
owner_arr.append(o2)

d1 = Dog("Balto", o1)
d2 = Dog("Fido", o2)
d3 = Dog(dogowner = o1)

doglist = []
doglist.append(d1)
doglist.append(d2)
doglist.append(d3)

objectlist = []
objectlist.append(owner_arr)
objectlist.append(doglist)

dogownerfile = open("listdogowner", "wb")
pickle.dump(objectlist, dogownerfile)
dogownerfile.close()

dogownerfile = open("listdogowner", "rb")
new_objectlist = pickle.load(dogownerfile)
new_ownerlist = new_objectlist[0]
for i in range(len(new_ownerlist)):
    print(new_ownerlist[i].toString())

new_doglist = new_objectlist[1]
for i in range(len(new_doglist)):
    print(new_doglist[i].toString())