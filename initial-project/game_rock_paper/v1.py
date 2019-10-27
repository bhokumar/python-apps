print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, Make your move ")
player2 = input("Player 2, Make your move ")

if player1 == "rock" and player2 == "scissors":
	print("Player 1 wins!")
elif player1 == "rock" and player2 == "paper":
	print("Player 2 win!!")
elif player1 == "paper" and player2 == "rock":
	print("Player 1 wins!")
elif player1 == "paper" and player2 == "scissors":
	print("Player 2 win!!")
elif player1 == "scissors" and player2 == "rock":
	print("Player 2 wins!")
elif player1 == "scissors" and player2 == "paper":
	print("Player 1 win!!")
elif player1 == player2:
	print("Its a tie!")
else:
	print("Something went wrong!!")