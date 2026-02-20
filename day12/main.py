import random


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


number = random.randint(0, 101)
print(number)
attempts = 0
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

print(
    f"You have {attempts} attempts remaining to guess the number.")

guess = int(input("Make a guess: "))


def game(guess, number):
    global attempts
    while True:
        if guess > number:
            print("Too high")
            attempts -= 1
            print(
                f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
        elif guess < number:
            print("Too low")
            attempts -= 1
            print(
                f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
        else:
            print(f"Congratulations, you got it, the number is {number}")
            break


game(guess, number)
