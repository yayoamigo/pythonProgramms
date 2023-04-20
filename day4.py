import random

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
---.__(___)1
'''

#Write your code below this line 👇

number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


gameArray = [rock, paper, scissors]

print(gameArray[number])

computerChoice = random.randint(0, 2)

print("Computer chose:" + gameArray[computerChoice])

if (number == 0 and computerChoice == 0):
  print("It's a draw!")
elif (number == 0 and computerChoice == 1):
  print("You lose!")
elif (number == 0 and computerChoice == 2):
  print("You win!")
elif (number == 1 and computerChoice == 0):
  print("You win!")
elif (number == 1 and computerChoice == 1):
  print("It's a draw!")
elif (number == 1 and computerChoice == 2):
  print("You lose!")
elif (number == 2 and computerChoice == 0):
  print("You lose!")
elif (number == 2 and computerChoice == 1):
  print("You win!")
elif (number == 2 and computerChoice == 2):
  print("It's a draw!")

