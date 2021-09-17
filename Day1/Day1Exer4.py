# number = int(input("Enter a number: "))
#
# print(f"The number entered is {number}")

hf = float(input("Enter your height in feet: "))
hi = float(input("Enter your height in inches: "))
wkg = float(input("Enter your weight in kilogram: "))

#PEMDAS
hm = ( (hf*30.48) + (hi*2.54)) / 100
bmi = wkg/(hm*hm)
print(f"Your Body Mass Index is {round(bmi,2)}")
