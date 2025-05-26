# How to create and use variables in python?
# For a better explanation you can visit the w3school which I'm using as resource
#https://www.w3schools.com/python/python_variables.asp


##First of all variables are nothing without values so we need at assing a value to our variable

Sensor1 = 'humidity'
Sensor2 = 'motion'
Sensor3 = 'temperature'

#Since I'm trying too build a zoo sensor system my variables will be related to that.
#Now we created values for our variables and when we print them--
print(Sensor1)
print(Sensor2)
print(Sensor3)

#We are seeing their values.
#That is easy right? But there are more ways to do same thing which it will be better if we know.
#First we assinged values with strings. Altough there are many data types we can talk about besides that we are going to focus on strings.
#To understand data types dear python gives us very easy way to find it which using type command.Here how it is-->
#We already had some datas sooo---
print(type(Sensor1))
#You see. The 'str' means string. What if we put numbers. Lets create another variable with numbers.

number =  1

print(number)
print(type(number))

# Thats an integer! Well have you seen the difference between strings and integers.
# If you didn't we put the strings between ('') these little guys. If you want to add a strings to your variable you need to make sure you have pair of those.

#So what is a string?
#A string is just text. Anything between quotes (' ' or " ") is considered a string.

#You can do a lot with strings. Let me show you some cool string methods Python gives us.

animal = 'Elephant' #Here we create another variable and it's an animal for our zoo.

print(animal.upper())   # makes all letters uppercase
print(animal.lower())   # makes all letters lowercase
print(animal.startswith("E"))  # checks if the string starts with 'E'
print(len(animal))  # gives us the length of the string 

#There are bunch of other features for strings check it from here https://www.w3schools.com/python/python_strings.asp

#So everythings cool but as we spoke about integer before there are 2 more data types would work for you. 
#But what is a data? Data types tell Python what kind of data we’re working with.
#Is it a number? Text? True/False? Python needs to know to handle it correctly.

#int	 5, 100	        Whole numbers (integers)
#float	 3.14, 0.01	    Decimal numbers (floating point)
#str	 "hello", 'a'	Text (strings)
#bool	 True, False	    True or False values


age = 25             # int
temperature = 36.6   # float
name = "Serhat"      # str
is_open = True       # bool

#So when we check their types-->

print(type(age))
print(type(temperature))
print(type(name))
print(type(is_open))

#We see their types. So yes it is pretty much like that. If you want to learn more go here https://www.w3schools.com/python/python_datatypes.asp


#Well you see there are many animals in a zoo. But we cant just create another line for each of them. I mean you can if you want to but python giving us a convenience for that matter.
# And thats called LIST's. Check this out.


animals = ["Elephant", "Tiger", "Giraffe"]

#Lists are surrounded by square brackets [] and can store multiple values.

#We can:
#Access items: 
animals[0] # As in a set the first elements always be 0 and continiues from there. So we got to suit to that.

#Add new ones: 
animals.append("Lion")

#Remove one : 
animals.remove("Tiger")

#Count them: 
print(len(animals))

print(animals)#By the way you have to do the changes before printing the list other ways it wont work. For example if we would have type len command before removing the tiger to output would be 4
#For more information please visit here https://www.w3schools.com/python/python_lists.asp
#So we have added our animals we are getting close. But someone need to check them right? So we need staffs. 
#What kind of staffs do zoos have? Maybe a zookeeper, vets, cleaners or guardians for the security.
#Lets add them all!

zoo_staff = {
    "vet": {"name": "Emily", "age": 45},
    "zookeeper": {"name": "Sam", "age": 32},
    "cleaner": {"name": "Luis", "age": 29},
    "guardian": {"name": "Ava", "age": 38}
}
#So here our staffs. We used dictionaries and as you see its little bit diffrent from the lists. It has curly braces.
#It is like regular dictionary. The only different thing is you creating the meanings. 
#So lets try to call someone.Our vet Emily.

print(zoo_staff["vet"]["name"])#Here she is 
#https://www.w3schools.com/python/python_dictionaries.asp

