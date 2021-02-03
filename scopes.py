#   x is global variable and can be accessed anywhere from the file
x = "neel"

#   create func abc
def abc():
    #   y is the local variable to function abc and can be accessed only from the function abc
    y = "niket"
    # a variable can be made global from function using keyword global followed by variable name
    global z
    z = "shinjo"
    print(x)
    print(y)

abc()

#   create func mno
def mno():
    print(x)
    #   we declared z variable in function abc but as a global variable thats why we can access it from function mno
    print(z)

mno()