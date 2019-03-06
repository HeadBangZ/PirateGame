# owner

class Owner:
    def __init__(self, ownerid, ownername):
        self._ownerid = ownerid
        self._ownername = ownername
    
    def toString(self):
        return self._ownername + " has id " + str(self._ownerid)

class Dog:
    _dogcounter = 0
    def __init__(self, dogname = "No name yet", dogowner = None):
        Dog._dogcounter = Dog._dogcounter + 1
        self._dogid = Dog._dogcounter
        self._dogname = dogname
        self._dogowner = dogowner

    def toString(self):
        return self._dogname + " has id " + str(self._dogid) + " and owner " + self._dogowner._ownername
    
