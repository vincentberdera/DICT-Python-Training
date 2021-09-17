class Person:
    # firstname = ""
    # middlename = ""
    # lastname = ""

    def __init__(self, fn, mn, ln): # self is also a variable that you can change to whatever you want, self is the default variable for that
        self.firstname = fn
        self.middlename = mn
        self.lastname = ln

# end of class Person

p = Person("Christian", "Cruz", "Gates")
print(p.firstname + " " + p.middlename + " " + p.lastname)

m = Person("Lester", "Berg", "Cruz")
print(m.firstname + " " + m.middlename + " " + m.lastname)