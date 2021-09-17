import random as rand


# print(rand.randint(0,5))

fruits = ["apple", "grapes", "kiwi"]

rand.shuffle(fruits)
for f in fruits:
    print(f)