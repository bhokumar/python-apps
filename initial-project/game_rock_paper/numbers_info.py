for number in range(1, 21):
	if number == 4 or number == 13:
		print("unlucky!")
	elif number % 2 == 0:
		print("even")
	else:
		print("odd")