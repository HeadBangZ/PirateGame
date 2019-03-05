#  Person

class Person():
    # class variable
    _personcounter = 0
    # constructor
    def __init__(self, name):
        self._name = name
        Person._personcounter += 1
        self._id = Person._personcounter

    # get name
    def getName(self):
        return self._name

    # get id
    def getId(self):
        return self._id

    # person talk
    def personTalk(self):
        return "Good morning"

    # to string
    def toString(self):
        return "Person : " + str(self.getId()) + " is called " + self.getName()

# Adult

class Adult(Person):
    # constructor
    def __init__(self, name, title):
        super().__init__(name)
        self._title = title
        
    #get title
    def getTitle(self):
        return self._title

    # adult talk
    def adultTalk(self):
        return "Wash your hand"
    
    # to string ( overriding )
    def toString(self):
        return super().toString() + " and has the title " + self.getTitle()

# Child
class Child(Person):
    # constructor
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age
    
    # get age
    def getAge(self):
        return self._age

    def childTalk(self):
        return "I am a child"

    # to string ( overriding )
    def toString(self):
        return super().toString() + " and has the age " + str(self.getAge())

# fish
class Fish():
    # class variables - state values
    NOT_HUNGRY = 0
    LITTLE_HUNGRY = 1
    VERY_HUNGRY = 2
    # constructor
    def __init__(self, type):
        self._type = type
        self._hungry = Fish.NOT_HUNGRY

    # get
    def getType(self):
        return self._type

    # swim
    def swim(self):
        if self._hungry == Fish.NOT_HUNGRY:
            self._hungry = Fish.LITTLE_HUNGRY
            return "swimming around"
        else:
            if self._hungry == Fish.LITTLE_HUNGRY:
                self._hungry = Fish.VERY_HUNGRY
                return "swimming more"

    # eat
    def eat(self):
        if self._hungry == Fish.NOT_HUNGRY:
            return "Not hungry"
        elif self._hungry == Fish.LITTLE_HUNGRY:
            self._hungry = Fish.NOT_HUNGRY
            return "Eats a little"
        else:
            self._hungry = Fish.LITTLE_HUNGRY
            return "Eats a lot"

    # to string 
    def toString(self):
        return "Happy to be a " + self.getType() + " is in hungry state " + str(self._hungry)
