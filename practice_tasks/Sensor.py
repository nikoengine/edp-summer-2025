#This is our sensor file.
#We are going to code our sensors and than import it to our main.

class Sensor:
    def __init__(self, id_number, sensor_type, cage):
        self.id_number = id_number
        self.sensor_type = sensor_type
        self.cage = cage

    def describe(self):
        print(f"Sensor {self.id_number}: type = {self.sensor_type}, cage = {self.cage}")

#Now lets import it. But we need to go our main first.
