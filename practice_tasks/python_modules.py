#Well now we are moving to another topic
#What if we code with multiple files. 
#Instead of using only our main we can separate it.
#And we can have cleaner codes and they will be easy to follow.
#And this is the part modules involves.

#So lets create another file and name it Sensor.py

#Yes now we can import it.


from Sensor import Sensor  # Importing the Sensor class from sensor.py


#Now we add our objects as we learned.
sensor1 = Sensor(1, "temperature", "giraffes 1")
sensor2 = Sensor(2, "motion", "lions 2")
sensor3 = Sensor(3, "humidity", "penguins 1")

sensors = [sensor1, sensor2, sensor3]

for Sensor in sensors:
    Sensor.describe()


#Thats it. And if you need more information please visit https://www.w3schools.com/python/python_modules.asp
