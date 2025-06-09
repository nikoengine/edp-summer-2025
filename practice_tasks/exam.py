#If we are going to build a sensor system first we need channels to communicate with them
from enum import Enum

security_channel = []
cage_quality_channel = []

#Here we define our types for our events and sensors
class SensorType(Enum):
    HUMIDITY = 'humidity'
    TEMPERATURE = 'temperature'
    MOTION = 'motion'

class EventType(Enum):
    HUMIDITY_ALERT = 'humidity_alert'
    TEMPERATURE_ALERT = 'temperature_alert'
    ANIMAL_ESCAPE = 'animal_escape'

# Event class for define events
class Event:
    def __init__(self, name: EventType, payload):
        self.name = name
        self.payload = payload

#And defining sensors and what they do
class Sensor:
    def __init__(self, id_number, sensortype: SensorType, cage):
        self.id_number = id_number
        self.sensortype = sensortype
        self.cage = cage

    def inform_event(self, name: EventType, payload):
        event = Event(name, payload)
        
        
        if name == EventType.HUMIDITY_ALERT or name == EventType.TEMPERATURE_ALERT:
            cage_quality_channel.append(event)
        elif name == EventType.ANIMAL_ESCAPE:
            security_channel.append(event)
        else:
            print("Unknown event!")
        
        print(f"Sensor {self.id_number} ({self.sensortype.value}) from cage '{self.cage}' reporting event: {name.value} with payload {payload}")

#Now lets create our events and sensors.
temperature_sensor = Sensor(1, SensorType.TEMPERATURE, "elephants_cage")
humidity_sensor = Sensor(2, SensorType.HUMIDITY, "tigers_cage")
motion_sensor = Sensor(3, SensorType.MOTION, "lions_cage")


humidity_sensor.inform_event(EventType.HUMIDITY_ALERT, {"value": "%90", "cage": "tigers_cage"})
temperature_sensor.inform_event(EventType.TEMPERATURE_ALERT, {"value": "40°C", "cage": "elephants_cage"})
motion_sensor.inform_event(EventType.ANIMAL_ESCAPE, {"cage": "monkeys_cage"})

#In a zoo we need 
class Employee:
    def __init__(self, id_number, name, role):
        self.id_number = id_number
        self.name = name
        self.role = role

    def handle_security_event(self):
        if self.role == 'guard':
            print(f"Guard {self.name} is catching the animal!")

    def handle_cage_quality_event(self, event_name):
        if self.role == 'zookeeper' and event_name == EventType.TEMPERATURE_ALERT:
            print(f"Zookeeper {self.name} is stabilizing the temperature.")
        elif self.role == 'cleaner' and event_name == EventType.HUMIDITY_ALERT:
            print(f"Cleaner {self.name} is cleaning the cage due to high humidity.")

employees = [
    Employee(1, "Ali", "guard"),
    Employee(2, "Tom", "cleaner"),
    Employee(3, "Serhat", "zookeeper")
]

def dispatch_events():
    print("\n---- DISPATCHING EVENTS ----")
    
    for event in security_channel:
        print(f"[Dispatch] Security Event: {event.name.value}, payload: {event.payload}")
        for emp in employees:
            emp.handle_security_event()

    for event in cage_quality_channel:
        print(f"\n[Dispatch] Cage Quality Event: {event.name.value}, payload: {event.payload}")
        for emp in employees:
            emp.handle_cage_quality_event(event.name)

dispatch_events()
