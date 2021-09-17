# summation and factorial using while loop

#Summation
# Eg. 5
# 1 + 2 + 3 + 4 + 5 = 15
# s = 0
# i = 1
# n = int(input("Enter a number: "))
# while i <= n:
#     s += i # s = s + i (accumulation statement)
#     i += 1
# print(f"The summation of {n} is {s}")

#Factorial
# Eg. 5
# 1 * 2 * 3 * 4 * 5 = 120
n = int(input("Enter a number: "))
f = 1
i = 1
while i <= n:
    f *= i
    i += 1
print(f"The factorial of {n} is {f}")