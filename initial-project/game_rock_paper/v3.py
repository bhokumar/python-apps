import random
#print("Rock...")
#print("Paper...")
#print("Scissors...")

player = input("Player Make your move ")
#player2 = input("Player 2, Make your move ")
rand_num = random.randint(0, 2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"
print(f"Computer plays {computer}")

if player == "rock":
	if computer == "scissors":
		print("Player wins!")
	elif computer == "paper":
		print("Computer win!!")
elif player == "paper" :
	if computer == "rock":
		print("Player  wins!")
	elif computer == "scissors" :
		print("Computer win!!")
elif player == "scissors": 
	if computer == "rock":
		print("Computer wins!")
	elif computer == "paper":
		print("Player  win!!")
elif player == computer:
	print("Its a tie!")
else:
	print("Something went wrong!!")
