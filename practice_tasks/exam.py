#creating edp event driven system to manage zoo sensor system
from enum import Enum
#If we are going to build a sensor system first we need channels.
#like security, cage quality and animal confitions.

security_channel = []
cage_quality_channel = []

#Now we need our sensor types to create sensor later.
#We can add humidity sensor temperature sensor and motion sensor

class SensorType(Enum):
    HUMIDITY = 'humidity'
    TEMPERATURE = "temperature"
    MOTION = "motion"

#And we need our events related to our sensor types.

class EventType(Enum):
    HUMIDITY_ALERT = 'humidity_alert'
    TEMPERATURE_ALERT = 'temperature_alert'
    ANIMAL_ESCAPE = 'animal_escape'

#Lets define our events.

class Event:
    def __init__(self, name:EventType, payload):
        self.name = name
        self.payload = payload

#And next our sensor and what they to when they emitted an event
class Sensor:
    def __init__(self,id_number, sensortype : SensorType, cage):
        self.cage = cage
        self.id_number = id_number
        self.sensortype = sensortype

    def inform_event(self, name:EventType, payload):
        event = Event(name, payload)
        if name == EventType.HUMIDITY_ALERT and EventType.TEMPERATURE_ALERT:
            cage_quality_channel.append()
        elif name == EventType.ANIMAL_ESCAPE:
            security_channel.append()
        else:
            print("Unknown event!")
        print(f"Sensor with payload {payload} informing event: {name.value} ")

#now lets create our events and sensors.

temperature_sensor = Sensor(1, SensorType.TEMPERATURE, "elephants_cage")
humidity_sensor = Sensor(2, SensorType.HUMIDITY, "tigers_cage")
motion_sensor = Sensor(3, SensorType.MOTION, "lions_cage")

#Now our events

humidity_sensor.inform_event(EventType.HUMIDITY_ALERT, {"value": "%90", "cage_2":"tigers_cage"})
temperature_sensor.inform_event(EventType.TEMPERATURE_ALERT, {"value": "40", "cage_1":"elephants_cage"})
motion_sensor.inform_event(EventType.ANIMAL_ESCAPE{"cage_3":"monkeys_cage"})







    
    

    

        
    
