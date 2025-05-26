#Well you see there are many animals in a zoo. But we cant just create another line for each of them. I mean you can if you want to but python giving us a convenience for that matter.
# And thats called LIST's. Check this out.


animals = ["Elephant", "Tiger", "Giraffe"]

#Lists are surrounded by square brackets [] and can store multiple values.

#We can:
#Access items: 
animals[0] # As in a set the first elements always be 0 and continiues from there. So we got to suit to that.

#Add new ones: 
animals.append("Lion")

#Remove one : 
animals.remove("Tiger")

#Count them: 
print(len(animals))

print(animals)#By the way you have to do the changes before printing the list other ways it wont work. For example if we would have type len command before removing the tiger to output would be 4
#For more information please visit here https://www.w3schools.com/python/python_lists.asp