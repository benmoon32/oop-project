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

def load_data(file):
    cars = []
    try:
        with open(file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.split(",")
                cars.append(Car(data[0], data[1], data[2], data[3], data[4], data[5]))
    except Exception as e:
        print(e)
    return cars

cars = load_data("data.txt")

print(len(cars))
print(cars)
