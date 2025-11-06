# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com/)
# to help create the code in this file.

import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessGame:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        tk.Label(master, text="Welcome to the Number Guessing Game!", font=("Arial", 14, "bold")).pack(pady=10)

        self.high_score = None

        # Feature 1: Difficulty
        tk.Label(master, text="Choose difficulty (Easy, Medium, Hard):").pack()
        self.difficulty_var = tk.StringVar(value="medium")
        tk.Entry(master, textvariable=self.difficulty_var).pack()

        tk.Button(master, text="Start Game", command=self.start_game).pack()

        self.guess_label = tk.Label(master, text="")
        self.guess_label.pack()

        self.guess_var = tk.StringVar()
        self.guess_entry = tk.Entry(master, textvariable=self.guess_var)
        self.guess_entry.pack()
        self.guess_entry.config(state='disabled')

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        self.guess_button.config(state='disabled')

        self.message_label = tk.Label(master, text="")
        self.message_label.pack()

    def start_game(self):
        difficulty = self.difficulty_var.get().lower()
        if difficulty == "easy":
            self.secret = random.randint(1, 50)
        elif difficulty == "hard":
            self.secret = random.randint(1, 200)
        else:
            self.secret = random.randint(1, 100)

        self.attempts = 0
        self.message_label.config(text="")
        self.guess_label.config(text="Enter your guess:")
        self.guess_var.set("")
        self.guess_entry.config(state='normal')
        self.guess_button.config(state='normal')

    def check_guess(self):
        guess_input = self.guess_var.get().strip()

        if guess_input.lower() == "quit":
            messagebox.showinfo("Quit", "Thanks for playing! Goodbye.")
            self.master.quit()
            return

        try:
            guess = int(guess_input)
        except ValueError:
            self.message_label.config(text="Please enter a valid number.")
            return

        self.attempts += 1

        if guess < self.secret:
            self.message_label.config(text="Too low!")
        elif guess > self.secret:
            self.message_label.config(text="Too high!")
        else:
            msg = f"You got it in {self.attempts} tries!"
            if self.high_score is None or self.attempts < self.high_score:
                self.high_score = self.attempts
                msg += "\n🎉 New High Score!"
            else:
                msg += f"\nHigh Score is still {self.high_score} attempts."
            messagebox.showinfo("Correct!", msg)
            self.guess_entry.config(state='disabled')
            self.guess_button.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessGame(root)
    root.mainloop()

