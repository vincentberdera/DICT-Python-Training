# Polymorphism
class Parrot:
    def fly(self):
        print("Parrot can fly...")
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly...")
    def swim(self):
        print("Penguin can swim")

#Interfaces
def test_fly(obj):
    obj.fly()
def test_swim(obj):
    obj.swim()

par = Parrot() # instance object
peng = Penguin() # instance object

test_fly(par)
test_swim(par)

test_fly(peng)
test_swim(peng)