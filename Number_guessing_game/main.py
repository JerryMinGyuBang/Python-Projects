#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo

def game():
    print(logo)

    import random
    number = random.choice(range(1, 101))

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    def guess():
        guess = int(input("Make a guess: "))
        return guess

    def feedback(num, life_remaining):
        guessed_num = num
        if guessed_num < number:
            print("Too low.")
            print("Guess again")
            print(f"You have {life_remaining} atttempts remaining to guess the number.")
        elif guessed_num > number:
            print("Too high.")
            print("Guess again")
            print(f"You have {life_remaining} atttempts remaining to guess the number.")
        else:
            print(f"You got it! The answer was {number}.")
            print("Play again?")
            game()

    if difficulty == "easy":
        lives = 10
        while lives != 0:
            lives -= 1
            feedback(guess(), lives)
        print ("You've run out of guesses, you lose")

    if difficulty == "hard":
        lives = 5
        while lives != 0:
            lives -= 1
            feedback(guess(), lives)
        print ("You've run out of guesses, you lose")

game()