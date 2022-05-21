rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game = [rock, paper, scissors]

p_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if p_choice >= 3 or p_choice < 0:
	print("Please enter a valid input")
else: 
	print(game[p_choice])
	
	c_choice = random.randint(0, 2)
	
	print("Computer chose:")
	
	print(game[c_choice])
	
	#0 ROCK
	#1 PAPER
	#2 SCISSOR
	
	
	if p_choice == 0 and c_choice == 2:
		print("You win!")
	elif c_choice == 0 and p_choice == 2:
		print("You loose")
	elif c_choice > p_choice:
		print("You lose!")
	elif p_choice > c_choice:
		print("You win!")
	elif p_choice == c_choice:
		print("Its a draw!")
	