temp = int(input("Enter temperature: "))
if temp > 100:
    print("Steam")
elif temp == 100:
    print("Boiling Point")
elif temp >= 1:
    print("Water")
elif temp == 0:
    print("Freezing Point")
# elif temp >= -25 and temp <= -17:
#     print("Alaska")
elif temp < 0:
    print("Ice")