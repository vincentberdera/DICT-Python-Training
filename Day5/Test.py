import MyModule as mm

letter = str(input("Enter a letter: "))
if mm.process.isVowel(letter) == True:
    print("Vowel")
else:
    print("Consonant")