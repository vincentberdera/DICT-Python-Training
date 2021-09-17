class Computer:
    __price = 46000

    def getPrice(self):
        return self.__price

    def setPrice(self, p):
        self.__price = p

comp = Computer()
print(f"The price of a computer is {comp.getPrice()}")
comp.__price = 15000 # direct modification
print(f"The new price of a computer is {comp.getPrice()}")
comp.setPrice(15000) #setter
print(f"Using setter method. The new price of a computer is {comp.getPrice()}")