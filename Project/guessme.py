#!/usr/bin/python3
#Thaninthorn Sabaiying (Fahsai)
#Rawikarn Choenkhwanma (Nuea)
#Punyapa Chamsaard (Yok)

import random

play_again = "yes"

while play_again == "yes":
    secret_number = random.randint(1, 100)
    attempts = 5
    min = 1
    max = 100

    print("Welcome to the Guess the Number game!")
    print("I've generated a secret number between", min, "and", max,". You have", attempts, "guesses.")

    while attempts > 0:
        print("Attempts left:", attempts)
        print("Guess a number between", min, "and", max)

        user_input = input("Enter your guess: ")

        guess = int(user_input)

        if guess < min or guess > max:
            print("Please guess a number between", min, "and", max,".")
            continue

        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < secret_number:
            print("Too low!")
            min = guess + 1
        else:
            print("Too high!")
            max = guess - 1

        attempts = attempts - 1

    if attempts == 0:
        print("Sorry! You've used all your guesses. The secret number was", secret_number,".")

    play_again = input("Do you want to play again? (yes/no): ").lower()

print("Thanks for playing! Goodbye!")