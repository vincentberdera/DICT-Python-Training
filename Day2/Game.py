#
#Paper - Pp
#Rock - Rr
#Scissor - Ss
#
player1 = str(input("Player 1: "))
player2 = str(input("Player 2: "))

print("====================")

#Paper vs Rock
if (player1.lower()=="p") and (player2.lower()=="r"):
    print("Player 1 Wins!")
    print("Paper covers rock")
#Rock vs Paper
elif (player1.lower()=="r") and (player2.lower()=="p"):
    print("Player 2 Wins!")
    print("Paper covers rock")
#Paper vs Scissors
elif (player1.lower()=="p") and (player2.lower()=="s"):
    print("Player 2 Wins!")
    print("Scissors cut paper")
#Scissors vs Paper
elif (player1.lower()=="s") and (player2.lower()=="p"):
    print("Player 1 Wins!")
    print("Scissors cut paper")
#Scissors vs Rock
elif (player1.lower()=="s") and (player2.lower()=="r"):
    print("Player 2 Wins!")
    print("Rock breaks scissors")
#Rock vs Scissors
elif (player1.lower()=="r") and (player2.lower()=="s"):
    print("Player 1 Wins!")
    print("Rock breaks scissors")
#Rock vs Rock
elif (player1.lower()=="r") and (player2.lower()=="r"):
    print("Draw")
#Scissors vs Scissors
elif (player1.lower()=="s") and (player2.lower()=="s"):
    print("Draw")
#Paper vs Paper
elif (player1.lower()=="p") and (player2.lower()=="p"):
    print("Draw")
else:
    if (player1.lower()!="p" or player1.lower()!="r" or player1.lower()!="s") and \
            (player2.lower()=="p" or player2.lower()=="r" or player2.lower()=="s"):
        print(f"Player 1: {player1}")
        print("Invalid Input")
    elif (player2.lower()!="p" or player2.lower()!="r" or player2.lower()!="s") and \
            (player1.lower()=="p" or player1.lower()=="r" or player1.lower()=="s"):
        print(f"Player 2: {player2}")
        print("Invalid Input")
    else:
        print(f"Player 1: {player1}")
        print(f"Player 2: {player2}")
        print("Invalid Inputs")
