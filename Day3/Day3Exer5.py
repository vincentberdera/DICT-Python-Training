#Nested Loops

# n = int(input("Enter a number: "))
# i = 1
# while i <= n:
#     j = 1
#     while j <= n:
#         print("*", end="  ")
#         j+=1
#     print()
#     i+=1

n = int(input("Enter a number: "))
i = 1
while i <= n:
    j = 1
    while j <= n:
        if j == 1 or j == n:
            print("*",end = "  ") # end = 2 spaces
        elif i == 1 or i == n:
            print("*",end = "  ") # end = 2 spaces
        elif j != 1 or j != n:
            print(" ",end = "  ") # end = 2 spaces
        j += 1
    print()
    i += 1
