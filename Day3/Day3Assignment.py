from os import system

fruits = list()

res = " "
while res.upper()!="X":
    system('cls') # clearing the console
    print("FRUIT MANAGER")
    print("[C] - Add new fruits")
    print("[D] - Delete fruit")
    print("[X] - Exit")

    res = str(input("Enter your choice: "))
    if res.upper() == "C":
        system('cls')
        print("Add New Fruit")
        item = str(input("Enter new fruit:"))
        fruits.append(item)
        for f in fruits:
            print(f" -{f}")
        input("Press any key to continue...")
    elif res.upper() == "R":
        system('cls')
        print("List of fruits")
        for f in fruits:
            print(f" -{f}")
        # pause statement
        input("Press any key to continue...")
    elif res.upper() == "D":
        system('cls')
        print("Remove")
        fruitToRemove = str(input("Enter fruit you want to delete:"))
        fruits.remove(fruitToRemove)
        #fruits.pop(fruitToRemove) #remove item in list using index number # make the fruitToRemove an integer
        for f in fruits:
            print(f" -{f}")
        input("Press any key to continue...")
    elif res.upper() == "X":
        print("Thank you")