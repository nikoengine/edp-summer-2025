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

#Also there are another way to create a dictionary with using the dict() method.
zoo_staff = dict(
    vet=dict(name="Dr. Emily", age=45),
    zookeeper=dict(name="Sam", age=32),
    cleaner=dict(name="Luis", age=29),
    guardian=dict(name="Ava", age=38),
    technician=dict(name="Leo", age=30)
)

print(zoo_staff)

#https://www.w3schools.com/python/python_dictionaries.asp