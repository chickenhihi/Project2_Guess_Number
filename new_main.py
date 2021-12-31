from art import logo
import random

x = random.randint(1,100)

def set_level():
    choose = input("Choose a difficulty. Type 'easy' or 'hard': " )
    if choose == 'easy':
        return 10
    elif choose == 'hard':
        return 5

def check_answer(your_guess):
        if your_guess > x:
            print("Too high.")
        elif your_guess < x:
            print("Too low.")
        else:
            print("Exacly ! Correct Answer: ", your_guess)

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game ! \nI'm thinking of a number between 1 and 100.\nPssst, the correct answer is 93 ")
    n = set_level()    
    for i in range(n):
        print(f"You have {n-i} attempts remaining to guess the number.")
        your_guess = int(input("Make a guess: "))
        check_answer(your_guess)
        if your_guess == x:
            break
    if your_guess != x:
        print("You've run out of guesses, you lose !")
    if input("Do you want to continue playing game ? Type 'yes' to continue, type 'no' to endgame: ") == 'yes':
        play_game()
play_game()

