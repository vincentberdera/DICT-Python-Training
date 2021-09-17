from os import system

words = list()
res = "y"
while res.lower() == "y":
    system('cls')
    item = str(input("Enter a word: "))
    words.append(item)
    res = str(input("Do you want to try again? input [Y/y] if yes and [N/n] if No: "))
    if res.lower() == "n":
        system('cls')
        print(f"Total number of words : {len(words)}")
        print("List of Words:")
        for w in words:
            print(f"-{w}")