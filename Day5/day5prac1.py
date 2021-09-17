class Car:
    def __init__(self, c, m, manu):
        self.color = c
        self.model = m
        self.manufacturer = manu
    def setValues(self, c, m, manu):
        self.color = c
        self.model = m
        self.manufacturer = manu

    def getValues(self):
        print(f" Car is color {self.color}, Model is {self.model}, Manufacturer is {self.manufacturer}")

# end of class Car

car = Car("Red", "Everest", "Ford")
car.getValues()
print("==========After modifying the properties=========")
car.setValues("Blue", "Fortuner", "Toyota")
car.getValues()
car.setValues("White", "mu-X", "Isuzu")
car.getValues()
car.setValues("Brown", "Terra", "Nissan")
car.getValues()

