#   writing class defination
class Person:
    #   declared variables with dummy value
    #   java like approach of defining class
    name = "no name"
    age = -1
    height = -1
    weight = -1

    #   consructor initialises the variables
    def __init__(self, n, h, w, a):
        self.name = n
        self.height = h
        self.weight = w
        self.age = a


#   creating objects of class Person
neel = Person("neel", 169, 50, 24)
juhi = Person("juhi", 160, 41, 21)
prajakta = Person("prajakta", 163, 56, 22)
niket = Person("niket", 169, 59, 28)


print( neel.name )
print(niket.age)
