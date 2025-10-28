# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com/)
# to help create the code in this file.

import random

def play():
    print("Welcome to the Number Guessing Game!")
    # Feature 1: Difficulty Levels

    difficulty = input("Choose difficulty (Easy, Medium, Hard): ").lower()
    if difficulty == "easy":
        secret = random.randint(1, 50)
        
    elif difficulty == "hard":
        secret = random.randint(1, 200)
    else:
        secret = random.randint(1, 100)

    guess = 0
    attempts = 0
    
    while guess != secret:
        try:
            guess = int(input("Your guess"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        attempts += 1
        if guess < secret:
            print("Too low!")

        elif guess > secret:
            print("Too high!")
        else:
            print(f"You got it in {attempts} tries!")

if __name__ == "__main__":
    play()
