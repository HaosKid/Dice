import random
Multiplayer = False
Singleplayer = False
#Choosing Multiplayer(yes) or singleplayer(no)
answear1 = input("Hey, do you want to play with your friend?\nYes/No: ")
if answear1.upper() == "YES":
	Multiplayer = True
	Player1 = input("Player 1 name: ")
	Player2 = input("Player 2 name: ")
#egg
elif answear1.upper() == "PING":
	print("pong!")
elif answear1.upper() == "NO":
	Player = input("Your name: ")
	Dealer = "Dealer"
	Singleplayer = True
#egg
else:
	print("I didn`t expect this answear >.>\nBye!")
#Multiplayer Game
while Multiplayer:
	#if no, the game will end.
	answear2 = input("Dice?\nYes/No: ")
	if answear2.upper() == "YES":
		Player1FirstDice, Player2FirstDice = random.randint(1, 6), random.randint(1, 6)
		Player1SecondDice, Player2SecondDice = random.randint(1, 6), random.randint(1, 6)
		Player1Total = Player1FirstDice + Player1SecondDice
		Player2Total = Player2FirstDice + Player2SecondDice
		print(f"""
		--------------------------------------------------------
					{Player1} : {Player1FirstDice}, {Player1SecondDice} = {Player1Total}
					{Player2} : {Player2FirstDice}, {Player2SecondDice} = {Player2Total}
		--------------------------------------------------------
		""")
		if  Player1Total > Player2Total:
			print(f"{Player1} won the game!")
		elif Player1Total == Player2Total:
			print("Draw")
		else:
			print(f"{Player2} won the game!")
	elif answear2.upper() == "NO":
		print("Have a nice day!")
		break
	#egg
	else:
		print("I didn`t expect this answear >.>\nBye!")

#SinglePlayer game
while Singleplayer:
	#if no, the game will end.
	answear2 = input("Dice?\nYes/No: ")
	if answear2.upper() == "YES":
		PlayerFirstDice, DealerFirstDice = random.randint(1, 6), random.randint(1, 6)
		PlayerSecondDice, DealerSecondDice = random.randint(1, 6), random.randint(1, 6)
		PlayerTotal = PlayerFirstDice + PlayerSecondDice
		DealerTotal = DealerFirstDice + DealerSecondDice
		print(f"""
		--------------------------------------------------------
					{Player} : {PlayerFirstDice}, {PlayerSecondDice} = {PlayerTotal}
					{Dealer} : {DealerFirstDice}, {DealerSecondDice} = {DealerTotal}
		--------------------------------------------------------
		""")
		if  PlayerTotal > DealerTotal:
			print(f"{Player} won the game!")
		elif PlayerTotal == DealerTotal:
			print("Draw")
		else:
			print(f"{Dealer} won the game!")
	elif answear2.upper() == "NO":
		print("Have a nice day!")
		break
	#egg
	else:
		print("I didn`t expect this answear >.>\nBye!")
		break
