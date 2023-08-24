import random
import tkinter as tk
def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissor") or
        (user_choice == "Scissor" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"
def play():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(["Rock", "Paper", "Scissor"])
    result = winner(user_choice, computer_choice)
    result_label.config(text=result)
    user_choice_label.config(text=f"Your choice: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")
root = tk.Tk()
root.title("Rock-Paper-Scissor Game")
root.geometry("400x300")
user_choice_label = tk.Label(root, text="Choose Rock, Paper, or Scissor:", font=("Helvetica", 14))
user_choice_label.pack()
user_choice_var = tk.StringVar()
user_choice_var.set("Rock")
Rock_button = tk.Radiobutton(root, text="Rock", variable=user_choice_var, value="Rock", font=("Helvetica", 12))
Rock_button.pack()
Paper_button = tk.Radiobutton(root, text="Paper", variable=user_choice_var, value="Paper", font=("Helvetica", 12))
Paper_button.pack()
Scissor_button = tk.Radiobutton(root, text="Scissor", variable=user_choice_var, value="Scissor", font=("Helvetica", 12))
Scissor_button.pack()
play_button = tk.Button(root, text="Play", command=play, font=("Helvetica", 12))
play_button.pack()
result_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"))
result_label.pack()
user_choice_label = tk.Label(root, text="", font=("Helvetica", 12))
user_choice_label.pack()
computer_choice_label = tk.Label(root, text="", font=("Helvetica", 12))
computer_choice_label.pack()
root.mainloop()
