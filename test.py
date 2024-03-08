#Condtional satatemnet

"""n = int(input("Enter the number: "))

if n > 0:
    print("n is a postive number")
elif n<0:
    print("n is a negative number")
else:
    print("n is a zero")"""


#loops
"""for i in [0, 2, 3, 4, 5]:
    print(i)"""

"""for i in range(6):
    print(i)"""

"""names = ["Harry", "Ron", "Hermonite"]
for name in names:
    print(name)"""

"""name = "Daniel"
for chars in name:
    print(chars)"""


#Dictionary
"""houses = {"harry":"Griflenrors", "Daniel":"Alamata"}
houses["harry"] = "Korem"
print(houses["harry"])
print(houses["Daniel"])"""

#Functions
"""def square(x):
    return x * x
for i in range(10):
    print(f"The squre of {i} is {square(i)}")"""


#OOP in python
"""class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
p = Point(2, 7)
print(p.x)
print(p.y)"""


#Application on the class
"""class Flight():

    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def addPassagerrs(self, name):
        if not self.openSeat():
            return False
        self.passangers.append(name)
        return True

    def openSeat(self):
        return self.capacity - len(self.passangers)

flight = Flight(3)

persons = ["Daniel", "Kibrom", "Yirga", "Alex", "Kemal"]
for person in persons:
    if flight.addPassagerrs(person):
        print(f"We added {person} to flight successfully")
    else:
        print(f"No avalible seat for the {person}")"""

#Data stucture using Python

# Arrays:- we only have list on the python that is not static array

"""list1 = ["Daniel", "Berhe", "Mituku"]

print(list1[0])
for i in range(len(list1)):
    if list1[i] == "Mituku":
        print(f"{list1[i]} has been found in here")
    else:
        print("We can not find the name")"""

#Exercise

"""myList = [ 2200, 2350,2600, 2130, 2190]

print(myList[0]-myList[1])

print(myList[0]+ myList[1] + myList[2])

for i in myList:
    if i == 2000:
        print("Here we have got the 2000")

myList.append(1980)
print(myList)"""

input = int(input("insert the max number"))
list1 = []

for i in range(input + 1):
    if i % 2 != 0:
        list1.append(i)

print (list1)
        
