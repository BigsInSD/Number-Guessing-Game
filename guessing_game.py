"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------


import random


def start_game():

print("WELCOME TO THE GREAT NUMBER GUESSING GAME")

ran_num = random.randint(1, 10)

try:
  guess = int(input("Please guess a number between 1 and 10  "))
  num_guess = 1

  if guess > 10:
    raise ValueError
  elif guess < 1:
    raise ValueError

except ValueError:
    print("Please use an integer between 1 and 10. Example 5")

else:
  while guess != ran_num:
    if guess < ran_num:
      guess = input("It's higher.  ")
      guess = int(guess)
    else:
      guess = input("It's lower.  ")
      guess = int(guess)
    num_guess = num_guess + 1

  print("congratulations! it took you {} tries to guess the number!".format(num_guess))

print("Thanks for playing. See you next time.")


# Kick off the program by calling the start_game function.
start_game()
