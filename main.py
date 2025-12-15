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
        return f"{self.id}: {self.name}, {self.make}, {self.body}, {self.year}, ${self.value}"

    def saveString(self):
        return f"{self.id},{self.name},{self.make},{self.body},{self.year},{self.value}"

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

# Function to save data to file
def save_data(file):
    file_contents = ""
    for car in cars:
        file_contents += f"{car.saveString()}\n"
    try:
        with open(file, 'w') as file:
            file.write(file_contents)
    except Exception as e:
        print(e)
    return cars

def printcars():
    for car in cars:
        print(car)

def addcar():
    print("Enter ID of the car, followed by the car's information")
    car_id = input("ID: ")
    car_name = input("Name: ")
    car_make = input("Make: ")
    car_body = input("Body: ")
    car_year = input("Year: ")
    car_value = input("Value: ")
    error = False
    for car in cars:
        if car.id == car_id:
            print("Incorrect ID - ID already exists in the system")
            error = True
    if error == False:
        new_car = Car(car_id, car_name, car_make, car_body, car_year, car_value)
        cars.append(new_car)
        print("Car is added to the inventory.")
        print(new_car)
    print("Do you want to add more cars? y(yes)/n(no)")
    add_more = input("> ")
    if add_more == "y":
        addcar()

def editcar():
    print("Not implemented yet")

def removecar():
    print("Enter ID of the car that you want to remove from the inventory")
    car_id = input("ID: ")
    for car in cars:
        if car.id == car_id:
            cars.remove(car)
            print("Car removed")
            return
    print("Invalid car ID")


def search():
    search_type = ""
    while search_type != "-1":
        print("To search using the ID enter 1. To search using the name of the car enter 2. Enter -1 to return to the previous menu")
        search_type = input("> ")
        if search_type == "1":
            print("Please enter the ID of the car:")
            car_id = input("ID: ")
            car_found = False
            for car in cars:
                if car.id == car_id:
                    print(f"Car found: {car}")
                    car_found = True
            if not car_found:
                print("Car not found")
        elif search_type == "2":
            print("Please enter the name of the car:")
            car_name = input("Name: ")
            car_found = False
            for car in cars:
                if car.name.lower().strip() == car_name.lower().strip():
                    print(f"Car found: {car}")
                    car_found = True
            if not car_found:
                print("Car not found")
        elif search_type != "-1":
            print("Invalid command")


# Load the cars from data.txt
saved_cars = load_data("data.txt")
cars = saved_cars

print("Welcome to the cars inventory system") 
command = ""
while command != "0":
    print("What would you like to do today?")
    print("Add a car? Enter 1\nSearch for car? Enter 2\nEdit car info? Enter 3\nRemove a car? Enter 4\nPrint the car list? Enter 5\nSave the data to a file? Enter 6\nExit? Enter 0")
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
        save_data("data.txt")
    elif command == "0":
        pass
    else:
        print("Invalid command")


