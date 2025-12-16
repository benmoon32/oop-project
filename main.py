# Car Inventory Manager
# December 15th, 2025
# Allows you to add, remove, edit, search for, print a list of, and save cars.
# Cars have an id (string), name (string), make (string), body (string), year (int), and value (float).
# Cars are saved to and loaded from a text file (data.txt), and stored in a list.
# Input is validated to ensure it is the correct type, and error messages will display if the user's input is incorrect.

# Car class
class Car:
    def __init__(self, id, name, make, body, year, value):
        self.id = id
        self.name = name
        self.make = make
        self.body = body
        self.year = int(year)
        self.value = float(value)

    def __repr__(self):
        return f"Car(id={self.id}, name={self.name}, make={self.make}, body={self.body}, year={self.year}, value={self.value})"

    # String representation of car
    def __str__(self):
        return f"{self.id}    {self.name}    {self.make}    {self.body}    {self.year}    {self.value:.1f}"

    # String that is saved to the text file
    def saveString(self):
        return f"{self.id},{self.name},{self.make},{self.body},{self.year},{self.value}"

# Helper function to ask for an input with validation
def input_with_validation(prompt, typecast, allow_empty, error_message = "Invalid input"):
    while True:
        value = input(prompt)
        if len(value) > 0 or allow_empty:
            try:
                if typecast is not None:
                    value = typecast(value)
                return value
            except ValueError:
                print(error_message)
        else:
            print(error_message)

# Function to load data from a text file
def load_data(filename):
    cars = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(",")
                cars.append(Car(data[0], data[1], data[2], data[3], data[4], data[5]))
    except FileNotFoundError:
        pass
    except Exception as e:
        print(e)
    return cars

# Function to save data to a text file
def save_data(filename):
    file_contents = ""
    for car in cars:
        file_contents += f"{car.saveString()}\n"
    try:
        with open(filename, 'w') as file:
            file.write(file_contents)
        print("Data saved to local file successfully!")
    except Exception as e:
        print(e)

# Print car list command
def printcars():
    for car in cars:
        print(car)

# Add car command
def addcar():
    print("Enter id of the car, followed by the car's information.")
    car_id = input_with_validation("Id: \n", str, False, "Invalid input - id cannot be empty")
    car_name = input_with_validation("name: \n", str, False, "Invalid input - name cannot be empty")
    car_make = input_with_validation("make: \n", str, False, "Invalid input - make cannot be empty")
    car_body = input_with_validation("Body: \n", str, False, "Invalid input - body cannot be empty")
    car_year = input_with_validation("year: \n", int, False, "Invalid input - Please enter an integer")
    car_value = input_with_validation("value: \n", float, False, "Invalid input - Please enter a number")
    error = False
    for car in cars:
        if car.name == car_name:
            print("The car is already in the inventory. No action is required..")
            error = True
        elif car.id == car_id:
            print("Incorrect Id. Id already exist in the system.")
            error = True
    if error == False:
        # Create the new car and add it to the list
        new_car = Car(car_id, car_name, car_make, car_body, car_year, car_value)
        cars.append(new_car)
        print("car is added to the inventory.")
        print(new_car)
    print("Do you want to add more cars? y(yes)/n(no)")
    add_more = input("")
    if add_more == "y":
        addcar()

# Edit car command
def editcar():
    car_id = ""
    while car_id != "-1":
        print("Enter the id of the car. Enter -1 to return to the previous menu")
        car_id = input("")
        car_found = False
        for car in cars:
            if car.id == car_id:
                car_found = True
                car_name = input_with_validation("name: \n", str, False, "Invalid input - name cannot be empty")
                car_make = input_with_validation("make: \n", str, False, "Invalid input - make cannot be empty")
                car_body = input_with_validation("Body: \n", str, False, "Invalid input - body cannot be empty")
                car_year = input_with_validation("year: \n", int, False, "Invalid input - Please enter an integer")
                car_value = input_with_validation("value: \n", float, False, "Invalid input - Please enter a number")
                
                # Update car with new values
                car.name, car.make, car.body, car.year, car.value = car_name, car_make, car_body, car_year, car_value

                print(f"Car's new info is {car}")
        if not car_found:
            print("Car not found")

# Remove car command
def removecar():
    print("Enter id of the car that you want to remove from the inventory")
    car_id = input("")
    for car in cars:
        if car.id == car_id:
            cars.remove(car)
            print("car removed")
            return
    print("Car not found")
    remove_more = input("Do you want to remove more cars? y(yes)/n(no)")

# Search command
def search():
    search_type = ""
    while search_type != "-1":
        print("To search using the Id enter 1. To search using the name of the car enter 2. Enter -1 to return to the previous menu")
        search_type = input("")
        # Search type 1 - ID
        if search_type == "1":
            print("Please Enter the id of the car:")
            car_id = input("")
            car_found = False
            for car in cars:
                if car.id == car_id:
                    print(f"Car found {car}")
                    car_found = True
            if not car_found:
                print("Car not found")
        # Search type 2 - name
        elif search_type == "2":
            print("Please enter the name of the car:")
            car_name = input("")
            car_found = False
            for car in cars:
                if car.name == car_name:
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
# Main loop
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


