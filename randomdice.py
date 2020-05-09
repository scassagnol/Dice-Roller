import random

print(random.randint(1,6))

answer = input("Do you want to keep rolling the dice yes or no " )

if answer == 'no':
		print("goodbye")

while answer == 'yes':
	dice = random.randint(1,6)
	print (dice)
	answer = input("Do you want to keep rolling the dice yes or no " )
	
	if answer == 'no':
		print("goodbye")
	
	if answer != 'yes' and answer != 'no':
			print("Please enter yes to continue or no to stop ")
			answer = input("Do you want to keep rolling the dice yes or no " )
