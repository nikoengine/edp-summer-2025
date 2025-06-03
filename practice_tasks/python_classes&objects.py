#Classes let us create custom data types. Instead of using just strings we can create our own. 
#A class is like a blueprint. It defines how an object should behave and what properties (attributes) it has.
# And an object is an instance of a class. You can create many objects from the same class.

#So lets build the sensors that we created before as a variable.

class Sensor:
    def __init__(self, id_number, sensor_type, cage):
        self.id_number = id_number
        self.sensor_type = sensor_type
        self.cage = cage

    def describe(self):
        print(f"Sensor {self.id_number}: type={self.sensor_type}, cage={self.cage}")

# Let’s break this down:
#class Sensor: We define a new class called Sensor.
#__init__: This is the constructor — it runs automatically when you create an object.
#self: Refers to the current object (you must include it in class methods).
#self.id_number, self.sensor_type, self.cage: These are attributes attached to each object.
#describe: A method (function inside a class) that prints sensor details.

#so lets create our objects.
#we have the id number,sensor type and the cage

sensor1 = Sensor(1, 'humidity', 'Elephant Cage')
sensor2 = Sensor(2, 'temperature', 'Tiger Cage')
sensor3 = Sensor(3, 'motion', 'Monkeys Cage')

#sensor as a self so its easy to understand 
#Then we call our objects with the functions.

sensor1.describe()
sensor2.describe()
sensor3.describe()
 
#Yeah its pretty much like that. For better explanation please visit https://www.w3schools.com/python/python_classes.asp



