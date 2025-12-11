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

# Command class
class Command:
    def __init__(self, name, description, func = None):
        self.name = name
        self.description = description
        self.func = func

    def run(self):
        self.func()

    def __str__(self):
        return f"{self.name} - {self.description}"

#Command functions
def listcommands():
    for command in commands:
        print(command)

def listcars():
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

def exitcmd():
    global should_exit
    if saved_cars != cars:
        print("Warning: you have unsaved changes!")
        print("Would you still like to exit? [Y/N]")
        exit_input = input()
        if exit_input.lower().strip() == "y":
            should_exit = True
    else:
        should_exit = True

# Possible commands
commands = [
        Command("help", "Print a list of avaliable commands", listcommands),
        Command("list", "Print a list of all cars", listcars),
        Command("add", "Add a new car", addcar),
        Command("edit", "Edit an existing car", editcar),
        Command("remove", "Remove a car", removecar),
        Command("search", "Search for a car", search),
        Command("save", "Saves modified data", savedata),
        Command("exit", "Exit the program", exitcmd)
]

def parse_command(cmd):
    for command in commands:
        if command.name == cmd:
            command.run()
            return
    print(f"Error: '{cmd}' is not a valid command!")

# Load the cars from data.txt
saved_cars = load_data("data.txt")
cars = saved_cars

print("Car Inventory Manager v0.1")
should_exit = False
command = ""
while should_exit == False:
    command = input("> ")
    parse_command(command)
