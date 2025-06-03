#So lets talk about functions.
#So... what is a function?
#A function is a block of code that only runs when you call it.
#Imagine it like a machine: you give it something -> it does something -> maybe gives something back.
#Let’s create our first function:

def greet():
    print("Hello, zoo staff!")

greet()
#Functions with parameters
#What if we want to say hello to someone specific?
def greet_employee(name):
    print(f"Hello {name}, welcome back!")
#So its basicly like that when we calling our functions we put the name and the parameter inside the function.

greet_employee("Serhat")
greet_employee("Tom")

#And in the end we put our parameters that we wanted.

#But what if we have more than one parameters.

def add(a, b):
    return a + b

result = add(3, 4)
print(result)

#So did you get the concept. We create a function called add and whatever we write inside it will do it.
#For me information https://www.w3schools.com/python/python_functions.asp