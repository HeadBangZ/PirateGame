class staticTest():
    def __init__(self):
        pass
    # implicit static function : does not ask for instance reference (self)
    # can only be called from class
    def staticFunction():
        return "I am an implicit static function"

    # explicit static function with decorators
    # can be called from class and object
    @ staticmethod
    def staticDecorator():
        return "I am an explicit static function"

    # normal instance function
    # can only be called from an object
    def instanceFunction(self):
        return "I am an instance function"

a = staticTest()
# print(a.staticFunction())     gives a runtime error

print(staticTest.staticFunction())
print(a.staticDecorator())
print(staticTest.staticDecorator())
#print(staticTest.instanceFunction())
print(a.instanceFunction())

# abstract classes and methods does not exist in python
# abstract methods can be made using the behavior of python
# else : can be handled by abstract base class (ABC)
# from abc import ABC, abstract method - a class and a decorator