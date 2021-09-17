# Function with parameter(s) and no returning value
def sum(n):
    s = 0
    i = 1
    while i<=n:
        s += i
        i +=1
    print(f"The summation of {n} is {s}")

n = int(input("Enter a number: "))
sum(n)

#Function with paramater(s) and returning value
def sum(n):
    s = 0
    i = 1
    while i<=n:
        s += i
        i +=1
    return s

n = int(input("Enter a number: "))
print(f"The summation of {n} is {sum(n)}")
