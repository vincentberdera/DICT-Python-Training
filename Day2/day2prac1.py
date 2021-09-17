name = str(input("Enter Name: "))
math = float(input("Enter Math: "))
science = float(input("Enter Science: "))
english = float(input("Enter English: "))

averageGrade = (math + science + english) / 3

print(f"Average Grade: %.2f" % averageGrade)
print("\n")

if averageGrade >= 75:
    print("Congratulations!")
    print("You passed the semester.")
else:
    print("You failed the semester")