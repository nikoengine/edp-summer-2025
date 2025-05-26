# How to create and use variables in python?
# For a better explanation you can visit the w3school which I'm using as resource
#https://www.w3schools.com/python/python_variables.asp


##First of all variables are nothing without values so we need at assing a value to our variable

Sensor1 = 'humidity'
Sensor2 = 'motion'
Sensor3 = 'temperature'
Sensor4= 'cleaning_sensor'

#Since I'm trying too build a zoo sensor system my variables will be related to that.
#Now we created values for our variables and when we print them--
print(Sensor1)
print(Sensor2)
print(Sensor3)
print(Sensor4)

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



