#   simple function
def func1():
    print("This is func1 executing")


#   simple function
def func2():
    print("This is func2 executing")


#   function with argument
def func3(name):
    print("Hello "+name)


#   function with keyword argument
def func4(name, country):
    print("Hello "+name+" . "+"You are from "+country)


#   function with default argument
def func4(name, country= "INDIA"):
    print("Hello "+name+" . "+"You are from "+country)


#   function with arbitrary arguments
def func5(*args):
    for arg in args:
        print(arg)


#   func with return value
def func6(num):
    return 2 * num


#   function with empty body
def func6():
    pass