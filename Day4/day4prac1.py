import random as rand

res = ""
generatedNames = list()

firstName = ["John", "Mark", "Chris", "James", "Philip"]
middleName = ["Doe", "Cruz", "Tolentino", "Milla", "Santiago"]
lastName = ["Reyes", "Gates", "Francisco", "Perez", "Dela Cruz"]

def generateName(rand1,rand2,rand3):
    fname = firstName[rand1]
    mname = middleName[rand2]
    lname = lastName[rand3]
    newname = fname + " " + mname + " " + lname
    return newname

def prompt():
    global res
    res = str(input("Do you want to generate new name?[y/n]: "))

while res.lower() != "n":
    prompt()
    if res.lower() == "y":
        rand1 = rand.randint(0, 4)
        rand2 = rand.randint(0, 4)
        rand3 = rand.randint(0, 4)
        newname = generateName(rand1, rand2, rand3)
        generatedNames.append(newname)

        print(f"Your new name is {newname}\n")

    elif res.lower() == "n":
        print("Thank You!")
        print("List of Generated Names:")
        for name in generatedNames:
            print(f"-{name}")
    else:
        print("Invalid Input")