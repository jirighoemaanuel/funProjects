import random

rock_paper_scissors = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
user_inp = int(input(""))
computer_choice = random.randint(0, 2)
final_verdict = ""


