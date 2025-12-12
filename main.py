# Car class
class Car:
    def __init__(self, id, name, make, body, year, value):
        self.id = id
        self.name = name
        self.make = make
        self.body = body
        self.year = year
        self.value = value

    def __repr__(self):
        return f"Car(id={self.id}, name={self.name}, make={self.make}, body={self.body}, year={self.year}, value={self.value})"

    def __str__(self):
        return f"{self.id}. {self.name}, {self.make}, {self.body}, {self.year}, ${self.value}"

# Function to load data from file
def load_data(file):
    cars = []
    try:
        with open(file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(",")
                cars.append(Car(data[0], data[1], data[2], data[3], data[4], data[5]))
    except Exception as e:
        print(e)
    return cars

def printcars():
    for car in cars:
        print(car)

def addcar():
    print("Not implemented yet")

def editcar():
    print("Not implemented yet")

def removecar():
    print("Not implemented yet")

def search():
    print("Not implemented yet")

def savedata():
    print("Not implemented yet")

# Load the cars from data.txt
saved_cars = load_data("data.txt")
cars = saved_cars

print("Welcome to the cars inventory system\nWhat would you like to do today?")
print("1 - Add a car\n2 - Search for a car\n3 - Edit a car\n4 - Remove a car\n5 - Print all cars\n6 - Save data\n0 - Exit")
command = ""
while command != "0":
    command = input("> ")
    if command == "1":
        addcar()
    elif command == "2":
        search()
    elif command == "3":
        editcar()
    elif command == "4":
        removecar()
    elif command == "5":
        printcars()
    elif command == "6":
        savedata()
    elif command == "0":
        pass
    else:
        print("Invalid command")


