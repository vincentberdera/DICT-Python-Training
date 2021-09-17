age = int(input("Enter your age: "))
if age >= 1 and age<=150:
    if age>= 60:
        print("Senior Citizen")
    elif age>=18:
        print("Qualified to vote")
    else:
        print("Not qualified to vote")
else:
    print("Age is not realistic")