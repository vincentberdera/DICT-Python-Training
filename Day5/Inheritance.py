#Single Inheritance
# class Animal: # Parent Class
#     def eat(self):
#         print("Eating...")
#
# class Dog(Animal): # Child Class
#     def bark(self):
#         print("Barking")
#
# #End of Class Definitions
# preppy = Dog()
# preppy.bark()
# preppy.eat()


# Multilevel Inheritance
# class Animal: # Parent Class
#     def eat(self):
#         print("Eating...")
#
# class Dog(Animal): # Child Class
#     def bark(self):
#         print("Barking")
#
# class Puppy(Dog):
#     def weep(self):
#         print("Wheeping...")
#
# babydog = Puppy()
# babydog.eat()
# babydog.bark()
# babydog.weep()

# Hierarchical Inheritance
# class Bird:
#     def eat(self):
#         print("Eating...")
#
# class Parrot(Bird):
#     def fly(self):
#         print("Flying...")
#
# class Penguin(Bird):
#     def swim(self):
#         print("Swimming...")
#
# peng = Penguin()
# par = Parrot()
#
# peng.eat()
# peng.swim()
# par.eat()
# par.fly()


# Multiple Inheritance
class A:
    def a(self):
        print("a")

class B:
    def b(self):
        print("b")

class C(A, B):
    def c(self):
        print("c")


c = C()
c.a()
c.b()
c.c()
