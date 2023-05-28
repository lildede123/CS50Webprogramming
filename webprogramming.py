"""
print("Hello, World!")

name = input("Please enter your name: ")
print(f"Hello, {name}")

n = int(input("Number: "))

if (n > 0):
    print("n is positive")
elif n < 0:
    print("n is negative")
else :
    print("n is zero")

#Define a list of names
name = ["Harry", "Ron", "Hermione", "Ginny"]
name.append("Draco")
name.sort()
print(name)

#Create an emmpty set
s = set()

#Add elements to the set
s.add("Harry")
s.add("Ron")
s.add("Hermione")
s.add("Ginny")
s.add("Draco")

s.remove("Draco")
print(s)
print(f"The set has {len(s)} elements")

#Loops
#for i in range(6):
    #print(i)

houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
for name, house in houses.items():
    print(f"{name} lives in {house}")

#Functions
from webprogramming import square

def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")


#Classes
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 5)
print(p.x)
print(p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
            return True
        else:
            return False
   
    def open_seats(self):
        return self.capacity - len(self.passengers)

flights = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flights.add_passenger(person)
    if success:
        print(f"{person} was added to the plane")
    else:
        print(f"The plane is full, {person} is not added")

#Decorators 

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()

#lambda 
people = [{"name": "Harry", "house": "Gryffindor"}, 
        {"name": "Cho", "house": "Ravenclaw"},
        {"name": "Hermione", "house": "Slytherin"}
]

people.sort(key=lambda x: x["name"])
print(people)

#Exceptions

import sys

try:
    x = int(input("Please enter a number: "))
    y = int(input("Please enter another number: "))
    z = x / y
    print(int(z))
except ZeroDivisionError:
    print("Cannot divide by zero")
    sys.exit(1)
except ValueError:
    print("Please enter a number")
    sys.exit(1)
except:
    print("Something went wrong")
    sys.exit(1)
"""
