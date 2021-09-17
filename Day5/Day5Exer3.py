class Person:
    firstname = ""
    middlename = ""
    lastname = ""

    def __init__(self, fn, mn, ln):
        self.firstname = fn
        self.middlename = mn
        self.lastname = ln
    def setValues(self, fn, mn, ln):
        self.firstname = fn
        self.middlename = mn
        self.lastname = ln

    def getValues(self):
        print(f"Firstname: {self.firstname}")
        print(f"Middlename: {self.middlename}")
        print(f"Lastname: {self.lastname}")
# end of class Person

p = Person("John", "Cruz", "Gosling")
p.getValues()
print("======After Modifying the attributes=========")
p.setValues("Mark", "Gates", "Jobs")
p.getValues()