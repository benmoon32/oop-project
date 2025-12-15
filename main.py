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
        return f"{self.id}    {self.name}    {self.make}    {self.body}    {self.year}    {self.value:.1f}"

    def saveString(self):
        return f"{self.id},{self.name},{self.make},{self.body},{self.year},{self.value}"

def load_data(file):
    cars = []
    try:
        with open(file, 'w+') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(",")
                cars.append(Car(data[0], data[1], data[2], data[3], data[4], data[5]))
    except Exception as e:
        print(e)
    return cars

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
    print("Enter id of the car, followed by the car's information.")
    car_id = input("Id: \n")
    car_name = input("name: \n")
    car_make = input("make: \n")
    car_body = input("Body: \n")
    car_year = input("year: \n")
    car_value = input("value: \n")
    error = False
    for car in cars:
        if car.name == car_name and car.make == car_make and car.body == car_body and car.year == car_year and car.value == car_value:
            print("The car is already in the inventory. No action is required..")
            error = True
        elif car.id == car_id:
            print("Incorrect Id. Id already exist in the system.")
            error = True
    if error == False:
        new_car = Car(car_id, car_name, car_make, car_body, car_year, car_value)
        cars.append(new_car)
        print("car is added to the inventory.")
        print(new_car)
    print("Do you want to add more cars? y(yes)/n(no)")
    add_more = input("> ")
    if add_more == "y":
        addcar()

def editcar():
    car_id = ""
    while car_id != "-1":
        print("Enter the id of the car. Enter -1 to return to the previous menu")
        car_id = input("ID: ")
        car_found = False
        for car in cars:
            if car.id == car_id:
                car_found = True
                car_name = input("Name: ")
                car_make = input("Make: ")
                car_body = input("Body: ")
                car_year = input("Year: ")
                car_value = input("Value: ")

                car.name, car.make, car.body, car.year, car.value = car_name, car_make, car_body, car_year, car_value

                print(f"Car's new info is {car}")
        if not car_found:
            print("Car not found")
            

    
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
        print("To search using the Id enter 1. To search using the name of the car enter 2. Enter -1 to return to the previous menu")
        search_type = input("")
        if search_type == "1":
            print("Please Enter the id of the car:")
            car_id = input("ID: ")
            car_found = False
            for car in cars:
                if car.id == car_id:
                    print(f"Car found {car}")
                    car_found = True
            if not car_found:
                print("Car not found")
        elif search_type == "2":
            print("Please enter the name of the car:")
            car_name = input("Name: ")
            car_found = False
            for car in cars:
                if car.name.lower().strip() == car_name.lower().strip():
                    print(f"Car found {car}")
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
    print("Add a car? enter 1\nSearch for car? enter 2\nEdit car info? enter 3\nRemove a car? enter 4\nPrint the car list? enter 5\nSave the data to a file? enter 6\nExit? enter 0.")
    command = input("")
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


