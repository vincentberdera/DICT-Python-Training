from os import system

res = ""
def menu():
    print("Record App")
    print("[1] - Check Balance")
    print("[2] - Deposit")
    print("[3] - Widthraw")
    print("[4] - Change PIN")
    print("[5] - Exit")

def prompt():
    global res
    res = str(input("Enter your choice: "))

def balance():
    try:
        system('cls')
        fr = open("account.txt", "r")
        for line in fr:
            line = line.strip("\n")
            line = line.strip(" ")
            acc = line.split(",")
            print(f"Balance: {acc[2]}")

        fr.close()

    except FileNotFoundError:
        print("File does not exists")
    input()

def deposit():
    try:
        system('cls')
        amount = int(input("Enter amount:"))

        fr = open("account.txt", "r")
        for line in fr:
            line = line.strip("\n")
            line = line.strip(" ")
            acc = line.split(",")

            balance = int(acc[2])

        fr.close()

        balance = balance + amount

        fw = open("account.txt", "w")
        content = acc[0] + "," + acc[1] + "," + str(balance)
        fw.write(content)
        fw.close()
        print(f"You deposited {amount} successfully!")
        print(f"New Balance: {balance}")
    except ValueError:
        print("Can accept integer value only")
    except FileNotFoundError:
        print("File does not exists")
    input()

def withdraw():
    try:
        system('cls')
        amount = int(input("Enter amount:"))

        fr = open("account.txt", "r")
        for line in fr:
            line = line.strip("\n")
            line = line.strip(" ")
            acc = line.split(",")

            balance = int(acc[2])

        fr.close()

        balance = balance - amount

        fw = open("account.txt", "w")
        content = acc[0] + "," + acc[1] + "," + str(balance)
        fw.write(content)
        fw.close()
        print(f"You withdrawn {amount} successfully!")
        print(f"New Balance: {balance}")

    except ValueError:
        print("Can accept integer value only")

    except FileNotFoundError:
        print("File does not exists")

    input()

def pin():
    try:
        system('cls')
        newpin = int(input("Enter new PIN:"))

        fr = open("account.txt", "r")
        for line in fr:
            line = line.strip("\n")
            line = line.strip(" ")
            acc = line.split(",")

        fr.close()

        fw = open("account.txt", "w")
        content = acc[0] + "," + str(newpin) + "," + acc[2]
        fw.write(content)
        fw.close()
        print(f"Changing PIN successful!")
        print(f"New PIN: {newpin}")

    except ValueError:
        print("Can accept integer value only")

    except FileNotFoundError:
        print("File does not exists")

    input()

while res != "5":
    system('cls')
    menu()
    prompt()
    acc = list()

    if res == "1":
        balance()
    elif res == "2":
        deposit()
    elif res == "3":
        withdraw()
    elif res == "4":
        pin()

print("Thank you!")