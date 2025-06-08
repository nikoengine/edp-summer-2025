from enum import Enum

security_channel = []
cage_quality_channel = []
animal_condition_channel = []

class SensorType(Enum):
    HUMIDITY = 'humidity'
    TEMPERATURE = 'temperature'
    MOTION = 'motion'
    ANIMAL = 'animal'

class EventType(Enum):
    ANIMAL_ESCAPE = 'animal_escape'
    HUMIDITY_ALERT = 'humidity_alert'
    CAGE_CLEANING_NEEDED = 'cage_cleaning_needed'
    TEMPERATURE_ALERT = "temperature_alert"
    ANIMAL_SICK = 'animal_sick'

class Event:
    def __init__(self, name:EventType, payload):
        self.name = name
        self.payload = payload


class Sensor:
    def __init__(self, id_number, sensor_type:SensorType, cage):
        self.id_number = id_number
        self.sensor_type = sensor_type
        self.cage = cage

    def emit_event(self, name:EventType, payload):
        event = Event(name,payload)
        if name == EventType.ANIMAL_ESCAPE:
            security_channel.append(event)
        elif name in [EventType.TEMPERATURE_ALERT, EventType.HUMIDITY_ALERT, EventType.CAGE_CLEANING_NEEDED]:
            cage_quality_channel.append(event)
        elif name == EventType.ANIMAL_SICK:
            animal_condition_channel.append(event)
        else:
            print('Unkown Event')
        print(f"Sensor; Emitted event! '{name.value}' from '{payload}'")

    
class Employee:
    def __init__(self, id_number, name, role):
        self.id_number = id_number
        self.name = name
        self.role = role

    def handle_security_event(self):
        if self.role == 'guard':
            print(f"Guard {self.name} cathing the animal!")
            print(f"Guard {self.name} Reporting to manager")

    def handle_cage_quality_event(self, event_name):
        if self.role == 'zookeeper' and event_name == EventType.TEMPERATURE_ALERT:
            print(f"Zookeper {self.name} stabilizing the temperature!")
            print(f"Zookeper {self.name} reporting to manager!")
        elif self.role == 'cleaner' and event_name == EventType.HUMIDITY_ALERT:
            print(f"Cleaner {self.name} cleaning the cage")
            print(f"Cleaner {self.name} sending report!")

    def handle_animal_condition_event(self, event_name):
        if self.role == 'vet' and event_name == EventType.ANIMAL_SICK:
            print(f"Vet {self.name} taking care of animal!")
            print(f"Vet {self.name} reporting to manager")


def dispatch_events():
    print("\n   DISPATCHING EVENTS   ")
    for event in security_channel:
        print(f"[Dispatch] Security Event: {event.name.value}, payload: {event.payload}")
        for emp in employees:
            emp.handle_security_event()

    for event in cage_quality_channel:
        print(f"\n[Dispatch] Cage Quality Event: {event.name.value}, payload: {event.payload}")
        for emp in employees:
            emp.handle_cage_quality_event(event.name)

    for event in animal_condition_channel:
        print(f"\n[Dispatch] Animal Condition Event: {event.name.value}, payload: {event.payload}")
        for emp in employees:
            emp.handle_animal_condition_event(event.name)


employees = [
    Employee(1, "Emre", "guard"),
    Employee(2, "Umut", "cleaner"),
    Employee(3, "Hakan", "vet"),
    Employee(4, "Serhat", "zookeeper")
]

humidity_sensor = Sensor(1, SensorType.HUMIDITY, "elephants 1")
temperature_sensor = Sensor(2, SensorType.TEMPERATURE, "tigers 1")
motion_sensor = Sensor(3, SensorType.MOTION, "elephants 1")
animal_condition_sensor = Sensor(4, SensorType.ANIMAL, "monkeys 1")



humidity_sensor.emit_event(EventType.HUMIDITY_ALERT, {"value": "70%" , "cage_1": "elephants 1"})
temperature_sensor.emit_event(EventType.TEMPERATURE_ALERT, {"value": "36°C", "cage_2": "tigers 1"})
motion_sensor.emit_event(EventType.ANIMAL_ESCAPE, {"cage_1": "elephants 1"})
animal_condition_sensor.emit_event(EventType.ANIMAL_SICK, {"cage_3" : "monkeys 1"})

dispatch_events()