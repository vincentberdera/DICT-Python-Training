num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
num3 = int(input("Enter Number3: "))

#HIGHEST NUMER
if (num1 > num2) and (num1 > num3):
    highest = num1
elif (num2 > num1) and (num2 > num3):
    highest = num2
elif (num3 > num1) and (num3 > num2):
    highest = num3
elif (num1 == num2) and (num1 > num3):
    highest = num1
elif (num1 == num3) and (num1 > num2):
    highest = num1
elif (num2 == num3) and (num2 > num1):
    highest = num2

#LOWEST NUMBER
if (num1 < num2) and (num1 < num3):
    lowest = num1
elif (num2 < num1) and (num2 < num3):
    lowest = num2
elif (num3 < num1) and (num3 < num2):
    lowest = num3
elif (num1 == num2) and (num1 < num3):
    lowest = num1
elif (num1 == num3) and (num1 < num2):
    lowest = num1
elif (num2 == num3) and (num2 < num1):
    lowest = num2

#ALL NUMBER ARE EQUAL
if (num1 == num2) and (num1 == num3):
    print("ALL NUMBER ARE EQUAL")
else:
    total = lowest + highest
    print(f"Lowest: {lowest}")
    print(f"Highest: {highest}")
    print(f"Sum: {total}")