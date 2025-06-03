#Well we all forgot to great our employees to their new job.
#Lets do that. Meanwhile we are going to learn another feature of python.
#Well there are many ways in python for using loops. We can either use dictionaires or lists.
#But we need to use square brackets both of them.
#First we are going to great our animals because we create them with lists.
animals = ["elephant","tiger","lion","monkey"]

for animal in animals:
    print(f"Hello {animal}")

#So you might get confused but don't worry.
#We wrote animal because we wanted to use this instead of animals.
#You see its something you need to do when you use loops.Something is need to represent your variable, list and dictionary.
#It can be anything most of the coders use "i" or "x" but its doesnt really matter.
#Also let me tell you why did we put f there.
#The f in front of the string stands for formatted string literal. It’s a Python feature that lets us embed variables directly inside strings very handy and clean.
#If we dont use formatted strings we have to write---
for animal in animals:
    print("Hello " + animal)
#It might seem like its not a big deal but when you have more messy example its going to be useful.

#There is another loop function called "while".
#We using while loop when we dont know how many times we need to loop.
#And if we dont add a limit to our while functions it's just goes forever.

escaped = True
tries = 0

while escaped:
    print("Searching for the tiger...")
    tries += 2
    if tries >= 3:
        escaped = False
        print("Tiger found!")

#So here we created a simple loop. First we created a variable with type bool. Which contains True and False. 
#The tiger escaped and we are going to find it. 
#There are some custom operators that python uses if you want to check it you can visit https://www.w3schools.com/python/python_operators.asp

#https://www.w3schools.com/python/python_while_loops.asp
#https://www.w3schools.com/python/python_for_loops.asp

