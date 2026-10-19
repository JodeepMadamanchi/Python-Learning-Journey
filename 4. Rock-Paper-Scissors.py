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
type_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if type_number == 0:
    print(rock)
elif type_number == 1:
    print(paper)
elif type_number == 2:
    print(scissors)
else:
    print("You have typed invalid number")

print("COMPUTER CHOSE")
import random
random_number = random.randint(0,2)
lists = [rock, paper, scissors]
print(lists[random_number])

if type_number == 0 and random_number == 0:
    print("TIE")
elif type_number == 1 and random_number == 1:
    print("TIE")
elif type_number == 2 and random_number == 2:
    print("TIE")
elif type_number == 0 and random_number == 1:
    print("YOU LOST AND COMPUTER WON")
elif type_number == 0 and random_number == 2:
    print("YOU WON!!")
elif type_number == 1 and random_number == 0:
    print("YOU WON!!")
elif type_number == 1 and random_number == 2:
    print("YOU LOST AND COMPUTER WON")
elif type_number == 2 and random_number == 0:
    print("YOU LOST AND COMPUTER WON")
else:
    print("YOU WON!!")