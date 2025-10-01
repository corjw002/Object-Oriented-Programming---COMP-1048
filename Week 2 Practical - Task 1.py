class Bike:
    def __init__(self, type, max_gears, gear):
        self.type = type
        self.max_gears = max_gears
        self.gear = gear



bike_1 = Bike("Mountain", 15, 3)
bike_2 = Bike("Road", 25, 16)
bike_store = [bike_1, bike_2]

for bike in bike_store:
    print(f"The bike is a {bike.type} bike and it is in gear {bike.gear} of {bike.max_gears}.")

