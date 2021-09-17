#Using Python List

#Array - static data structure (we can't change data during run time, you can't mix)
#List - dynamic data sturcture

games =["axie infinity", "mobile legends", "nba", "dota"]
fruits = ["apple", "dragon fruit", "kiwi", "cherry"]

# print(games[0])
# print(fruits[-1]) #negative indexing refers to the last item
# print(fruits[-2])
print("List of fruits(original):")
for f in fruits:
    if f == fruits[-1]:
        print(f, end="")
    else:
        print(f, end=", ")

item = str(input("\nEnter new fruit: "))
fruits.insert(3,item)
# fruits.append(item)
print("\n\nList of fruits after appending new item:")
for f in fruits:
    if f == fruits[-1]:
        print(f, end="")
    else:
        print(f, end=", ")