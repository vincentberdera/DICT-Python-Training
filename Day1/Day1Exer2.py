# name = "Vincent"
# food = "Burger"
# game = "COD"
#
# text1 = "My name is {} I love {} and playing {}"
# info1 = text1.format(name,food,game)
# print(info1)

# text1 = "My name is {0} I love {1} and playing {2}"
# info1 = text1.format(name,food,game)
# print(info1)

text1 = "My name is {newname} I love {newfood} and playing {newgame}"
info1 = text1.format(newname="Michael",newfood="Fries",newgame="Chess")
print(info1)
