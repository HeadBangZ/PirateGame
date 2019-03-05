class Pirate():
    def __init__(self, name):
        self._name = name
        self._next = None

    def getPointer(self):
        return self._next

    def setPointer(self, pointer):
        self._next = pointer
        return self._next
