#Patterns using while loop

first = 0
second = 1
third = first+second

n = int(input("Enter a number: "))

print(f"{first} {second}", end =" ")
i = 3
while i<=n:
    print(third, end=" ")
    first = second
    second = third
    third = first + second
    i += 1