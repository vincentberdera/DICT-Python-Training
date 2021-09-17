res = "y"
while res.lower() == "y":
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    if (num1 + num2) % 2 == 0:
        print(f"The sum of {num1} and {num2} is Even")
    else:
        print(f"The sum of {num1} and {num2} is Odd")
    print("______________________________________________________________")
    res = str(input("Do you want to try Again? [Y/y] or [N/n]: "))
    print()
    if res.lower() == "n":
        print("Thank You!")