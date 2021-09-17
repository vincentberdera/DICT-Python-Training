n = int(input("Enter a number: "))
i = 1
while i <= (n*n):
    if i % n == 1:
        print()
        print("*", end="  ")
    elif i <= n:
        print("*", end="  ")
    elif i % n == 0:
        print("*", end="  ")
    elif i >= ((n*n) - (n-2)):
        print("*", end="  ")
    else:
        print(" ", end="  ")

    i+=1