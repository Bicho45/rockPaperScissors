import random

print(f"Welcome to the Rock, Paper, Scissor")
press = input("Press Enter to continue or type (Help) for the rules: ").capitalize()
if press == "Help":
    print("""
                ********** RULES **********
            1) You choose and the computer chooses
            2) Rock smashes Scissors -> Rock wins
            3) Scissors cut Paper -> Scissors win
            4) Paper covers Rock -> Paper wins
    """)

#rock , scissors, paper ascii art
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

#choices
options = ['Paper', 'Scissors', 'Rock']
user_choice = input("Enter your choice (rock, paper, scissors): ").capitalize()
computer_choice = random.choice(options)

if user_choice not in options:
    print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")
else:
    #user choice
    if user_choice == options[0]:
        print("You chose:\n", paper)
    elif user_choice == options[1]:
        print("You chose:\n",scissors)
    else:
        print("You chose:\n",rock)

    #computer choice
    if computer_choice == options[0]:
        print("Computer chose:\n", paper)
    elif computer_choice == options[1]:
        print("Computer chose:\n", scissors)
    else:
        print("Computer chose:\n", rock)

    #tie , win or lose
    if user_choice == computer_choice:
        print("It's a tie!")
    else:
        if (user_choice == options[0] and computer_choice == options[2]) or  (user_choice == options[1] and computer_choice == options[0]) or (user_choice == options[2] and computer_choice == options[1]):
            print(f"You win {user_choice} beats {computer_choice}")
        else:
            print(f"You lose {computer_choice} beats {user_choice}")
