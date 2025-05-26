#So lets see what is our next step.
#We have our employees and animals. Now we need some events.
#Since it's a project for event-driven programming we need to add some events.
events = ["motion_detected", "temperature_alert", "humidity_low", "dirty_cage"]

for event in events:
    if event == "temperature_alert":
        print("Call the vet!")
    elif event == "motion_detected":
        print("Send security!")
    elif event == "humidity_low":
        print("Turn on humidifier!")
    elif event == "dirty_cage":
        print("Send a cleaner!")
    else:
        print("Unknown event.")

#It's quite simple right? Well if you ever learn scratch those kind of lines might be familiar.
#Also there are many things you can do with if-else statements. For more information please check.
#https://www.w3schools.com/python/python_conditions.asp

