# Class Car
class Car:
    model = "Everest"
    brand = "Ford"
    color = "Blue"
    year = "2020"

    def start(self):
        print("Starting the engine...")

    def stop(self):
        print("Turning off the engine...")

    class A:
        point = 12
        wheel = 4
        cylinder = 6

    # End of class A--------------------------
    aobject = A()

# End of class car--------------
mycar = Car()

print(mycar.model)
# print(mycar.start) #print function is not recommended here
mycar.start()
print(mycar.aobject.point)