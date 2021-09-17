from os import system
data = dict()
res = ""

while res.lower() != "c":
    system('cls')
    print("Simple Phonebook")
    print("[a] - Add Data")
    print("[b] - Delete Data")
    print("[c] - Exit")
    res = str(input("Enter choice: "))
    if res.lower() == "a":
        system('cls')
        print("Add Data")
        key = str(input("Enter key: "))
        value = str(input("Enter value: "))
        data[key] = value
        for iter in data:
            print(f"-{iter}: {data[iter]}")
        input("Press any key to continue...")

    elif res.lower() == "b":
        system('cls')
        print("Delete Data")
        key = str(input("Enter key: "))
        data.pop(key)
        for iter in data:
            print(f"-{iter}: {data[iter]}")
        input("Press any key to continue...")

    elif res.lower() == "c":
        system('cls')
        print("THANK YOU")