from os import system

fruits = list() # list() - constructor to create an empty list

#Stack
#Queues - Circular
#Linked-List - Singularly or Doubly

res = " "
while res.upper()!="X":
    system('cls') # clearing the console
    print("FRUIT MANAGER")
    print("[C] - Add new fruits")
    print("[R] - Read List of Fruits")
    print("[U] - Update fruit")
    print("[D] - Delete fruit")
    print("[X] - Exit")

    res = str(input("Enter your choice: "))
    if res.upper() == "C":
        system('cls')
        print("Add New Fruit")
        item = str(input("Enter new fruit:"))
        fruits.append(item)
        input("Press any key to continue...")
    elif res.upper() == "R":
        system('cls')
        print("List of fruits")
        for f in fruits:
            print(f" -{f}")
        # pause statement
        input("Press any key to continue...")
    elif res.upper() == "U":
        system('cls')
        print("Updating the item")
        new = str(input("Enter an item: "))
        old = str(input("Enter item to be replaced: "))
        i = 0
        index = int()
        found = False
        for f in fruits:
            if f == old:
                found = True
            i+=1
        if found == True:
            fruits[index] = new
        else:
            print("The item does not exist")

        # pause statement
        input("Press any key to continue...")
    elif res.upper() == "D":
        system('cls')
        print("Remove")
        fruitToRemove = int(input("Enter word you want to remove:"))
        #fruits.remove(fruitToRemove)
        fruits.pop(fruitToRemove) #remove item in list using index number
        input("Press any key to continue...")
    elif res.upper() == "X":
        print("Thank you")