from os import system
res1 = ""
res2 = ""
def menu():
    print("CALCULATOR")
    print("[A] - Addition")
    print("[S] - Subtraction")
    print("[M] - Multiplication")
    print("[D] - Division")

def prompt1():
    global res1
    res1 = str(input("Do you want to generate new name?[y/n]: "))
def prompt2():
    global res2
    res2 = str(input("Enter your choice: "))


def addition():
    try:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        result = num1+num2
        print(f"Sum: {result}")
    except ValueError:
        print("Can accept integer value only")
def subraction():
    try:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        result = num1-num2
        print(f"Difference: {result}")
    except ValueError:
        print("Can accept integer value only")
def multipplication():
    try:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        result = num1*num2
        print(f"Product: {result}")
    except ValueError:
        print("Can accept integer value only")
def division():
    try:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        result = num1/num2
        print(f"Quotient: {result}")
    except ValueError:
        print("Can accept integer value only")
    except ZeroDivisionError:
        print("Any number divided by zero is invalid")


while res1.lower() != "n":
    system('cls')
    menu()
    prompt2()
    if res2.lower() == "a":
        system('cls')
        print("Addition")
        addition()
        prompt1()
    elif res2.lower() == "s":
        system('cls')
        print("Subtraction")
        subraction()
        prompt1()
    elif res2.lower() == "m":
        system('cls')
        print("Multiplication")
        multipplication()
        prompt1()
    elif res2.lower() == "d":
        system('cls')
        print("Division")
        division()
        prompt1()
print("THANK YOU")