name = str(input("Enter Name: "))
math = float(input("Enter Math: "))
science = float(input("Enter Science: "))
english = float(input("Enter English: "))

averageGrade = (math + science + english) / 3
print(f"Average Grade: %.2f" % averageGrade)
print("\n")

if averageGrade >= 75:
    print("Congratulations!")
    print("You passed the semester")
    if math < 75 or science < 75 or english < 75:
        print("but you need to retake the following subject(s):")
        if math < 75:
            print("Math")
        if science < 75:
            print("Science")
        if english < 75:
            print("English")
else:
    print("You failed the semester")