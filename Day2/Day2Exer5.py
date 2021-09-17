# value = "asd"
#
# if value.isupper():
#     print("Uppercase")
# else:
#     print("Not in uppercase")

# if value.isupper() == True:
#     print("Uppercase")
# else:
#     print("Not in uppercase")
#
# if value.islower() == True:
#     print("Lowercase")
# else:
#     print("Not in lowercase")
#
# if value.isdigit() == True:
#     print("Digits")
# else:
#     print("Not digits")
#
# if value.isalpha() == True:
#     print("Alphabet")
# else:
#     print("Not in the alphabet")

try:
    number = int(input("Enter a number: "))
    print(f"Magic number is {number*24}")
except ValueError:
    print("Invalid Input")