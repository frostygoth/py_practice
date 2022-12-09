# Player verses computer
# A coin is flipped up to 10 times
# First, the player guesses how many times it'll be flipped before there is
#	one heads returned
# Then the computer guesses via rand
# The coins are flipped via rand
# Once there's a heads, whoever was closer gets the number of tails * 10 in
#	points. Then it goes again until 1 person has 100 points

from random import randint

def get_user_input():
	return int(input("Enter guess: "))

def get_comp_input():
	return randint(1,10)

def flip_coin(times):
	# odds are heads, evens are tails
	if randint(1,100) % 2 == 1:
		print("H", end="")
		return times + 1
		
	else:
		print("T", end=", ")
		mything = flip_coin(times + 1)
	return mything

user_score = 0
comp_score = 0

while True:
	print("")
	user_input = get_user_input()
	comp_input = get_comp_input()
	print(f"Computer guess: {comp_input}")

	print("Coin Flips : ", end="")
	coins = flip_coin(0)
	print("")
	print(f"Number of coin flips {coins}")

	if abs(user_input - coins) == abs(comp_input - coins):
		if user_input <= coins and comp_input != user_input:
			user_score = user_score + 10
			print("Congratulations, you didn't go over!")
		elif comp_input <= coins and comp_input != user_input:
			comp_score = comp_score + 10
			print("The computer didn't go over, but you did...")
		elif randint(1,2) > 1:
			user_score = user_score + 10
			print("Congratulations, you win the tie!")
		else:
			comp_score = comp_score + 10
			print("The computer won the tie...")
	elif abs(user_input - coins) < abs(comp_input - coins):
		if user_input <= coins:
			user_score = user_score + 10
			print("Congratulations, you were closer without going over!")
		elif user_input > coins and comp_input <= coins:
			comp_score = comp_score + 10
			print("The computer won because you went over and it didn't...")
		else:
			user_score = user_score + 10
			print("Congratulations, you were the closest, and you both went over!")
	else:
		if comp_input <= coins:
			comp_score = comp_score + 10
			print("The computer was closer without going over...")
		elif comp_input > coins and user_input <= coins:
			user_score = user_score + 10
			print("Congratulations, you didn't go over")
		else:
			comp_score = comp_score + 10
			print("The computer was closer, and you both went over...")

	if comp_score > 99:
		print("The computer wins the game")
		break
	if user_score > 99:
		print("You won the game!")
		break	

	print(f"Your score : {user_score}")
	print(f"Computer score : {comp_score}")
