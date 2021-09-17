# try:
#     number = 5
#     print(number)
#     q = number/0
#
# except NameError:
#     print("Error Message 1")
# except ValueError:
#     print("Error Message 2")
# except ZeroDivisionError:
#     print("Error Message 3")
# else:
#     print("No Error")
# finally:
#     print("Finished")

try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Can accept interger value only")