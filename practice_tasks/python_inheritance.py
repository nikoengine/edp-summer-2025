#Let’s say we want to make a more specific sensor class for temperature sensors, but still keep the general behavior of all sensors.
#What do we need to do?
#There are 2 types of classes
#Parent and child.
#When we need to work on something that we already have in our class.
#We use inheritances.

#Let me explain it briefly and then we are going to adjust it to zoo sensor system.
class Parent:
    def __init__(self):
        print("I'm the parent.")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call the parent's constructor
        print("I'm the child.")



#super() is a built-in function that gives you access to methods and attributes of a parent class from within a child class.
#You typically use super() to:
#Call the parent class's constructor (__init__)
#Use a method from the parent class without re-writing it


#Now lets make it with sensor system.


class Sensor:
    def __init__(self, id_number, sensor_type, cage):
        self.id_number = id_number
        self.sensor_type = sensor_type
        self.cage = cage

    def describe(self):
        print(f"Sensor {self.id_number}: type={self.sensor_type}, cage={self.cage}")

#This is our parent class.
#But I want to add more specific about sensors.


class TemperatureSensor(Sensor):
    def __init__(self, id_number, cage, unit="Celsius"):
        super().__init__(id_number, "temperature", cage)  # sensor_type is always 'temperature'
        self.unit = unit

    def show_unit(self):
        print(f"Temperature is measured in {self.unit}.")

#Simply I just add temperature and a unit to our sensors types. 
#For more information visit https://www.w3schools.com/python/python_inheritance.asp