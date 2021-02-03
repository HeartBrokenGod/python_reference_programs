#   Parent Class Person
class Person:
    name = None
    height = 0
    weight = 0
    age = 0

    #   constructor
    def __init__(self, n, h, w, a):
        self.name = n
        self.height = h
        self.weight = w
        self.age = a

    #   getter methods
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getWeight(self):
        return self.weight

    def getHeight(self):
        return self.height


#   Child Class Student
#   Class Student inherits Class Parent
class Student(Person):
    rollNo = 0

    #   constructor
    def __init__(self, n, h, w, a, r):
        super().__init__(n, h, w, a)
        self.rollNo = r

    #   getter methods
    def getRollNo(self):
        return self.rollNo

#   creates object of class Person
#   p1 is the object
p1 = Person("neel", 169, 51, 24)

print(p1.getName())

#   creates object of class Student
#   s1 is the object
s1 = Student("neel", 169, 51, 24, 10)

print(s1.getName())
print(s1.getRollNo())

