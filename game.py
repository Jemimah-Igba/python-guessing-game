# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com/)
# to help create the code in this file.

import random

def play():
    print("Welcome to the Number Guessing Game!")
    secret = random.randint(1, 100)
    guess = 0
    attempts = 0

    while guess != secret:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"You got it in {attempts} tries!")

if __name__ == "__main__":
    play()
