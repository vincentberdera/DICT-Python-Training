class String:
    def isupper(self, string):
        if string.isupper():
            return True

    def islower(self, string):
        if string.islower():
            return True
    def isVowel(self, char):
        if char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or \
            char.lower() == "o" or char.lower == "u":
            return True

process = String()

class Calculator:
    def factorial(self, n):
        i = 1
        f = 1
        while i <= n:
            f *= 1
            i += 1
        return f
