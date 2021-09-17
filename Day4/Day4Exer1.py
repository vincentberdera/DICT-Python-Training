# Function with parameter(s) and returning value
# def sum(n1,n2):
#     s = n1+n2
#     return s
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(f"The sum of {num1} and {num2} is {sum(num1,num2)}")

#Function without parameter(s) and returning value
from os import system
res = "" #global variable if it is on the topmost
def menu():
    print("ATM PROGRAM")
    print("[V] - Check Balance")
    print("[D] - Deposit")
    print("[W] - Withdraw")
    print("[C] - Change PIN")
    print("[X] - Exit")

def prompt():
    global res
    res = str(input("Enter your choice: "))


while res.lower() != "x":
    system('cls')
    menu()
    prompt()
    if res.lower() == "v":
        system('cls')
        print("Balance Inquiry")
        input("Press any key to continue...")
    elif res.lower() == "w":
        system('cls')
        print("Withdraw")
        input("Press any key to continue...")
    elif res.lower() == "d":
        system('cls')
        print("Deposit")
        input("Press any key to continue...")
    elif res.lower() == "c":
        system('cls')
        print("Change PIN")
        input("Press any key to continue...")
    elif res.lower() == "x":
        print("THANK YOU")

