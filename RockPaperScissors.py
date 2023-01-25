import random

roca = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijeras = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

juego = [roca, papel, tijeras]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(juego[user_choice])

computer_choice=random.randint(0,2)
print(juego[computer_choice])

if user_choice >= 3 or user_choice <= 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
else:
  print("It's a draw")
