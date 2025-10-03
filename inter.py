import tkinter as tk
from random import choice

class RockPaperScissor:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissor")
        self.window.geometry("300x200")
        self.player_score = 0
        self.computer_score = 0

        self.score_label = tk.Label(self.window, text="Player: 0 - Computer: 0", font=("Arial", 16))
        self.score_label.pack()

        self.result_label = tk.Label(self.window, text="", font=("Arial", 16))
        self.result_label.pack()

        self.rock_button = tk.Button(self.window, text="Rock", command=self.rock)
        self.rock_button.pack()

        self.paper_button = tk.Button(self.window, text="Paper", command=self.paper)
        self.paper_button.pack()

        self.scissor_button = tk.Button(self.window, text="Scissor", command=self.scissor)
        self.scissor_button.pack()

    def computer_choice(self):
        return choice(["rock", "paper", "scissor"])

    def rock(self):
        computer = self.computer_choice()
        if computer == "rock":
            self.result_label['text'] = "Tie!"
        elif computer == "paper":
            self.computer_score += 1
            self.score_label['text'] = f"Player: {self.player_score} - Computer: {self.computer_score}"
            self.result_label['text'] = "Paper covers rock! Computer wins!"
        else:
            self.player_score += 1
            self.score_label['text'] = f"Player: {self.player_score} - Computer: {self.computer_score}"
            self.result_label['text'] = "Rock smashes scissor! Player wins!"

    def paper(self):
        computer = self.computer_choice()
        if computer == "rock":
            self.player_score += 1
            self.score_label['text'] = f"Player: {self.player_score} - Computer: {self.computer_score}"
            self.result_label['text'] = "Paper covers rock! Player wins!"
        elif computer == "paper":
            self.result_label['text'] = "Tie!"
        else:
            self.computer_score += 1
            self.score_label['text'] = f"Player: {self.player_score} - Computer: {self.computer_score}"
            self.result_label['text'] = "Scissor cuts paper! Computer wins!"

    def scissor(self):
        computer = self.computer_choice()
        if computer == "rock":
            self.computer_score += 1
            self.score_label['text'] = f"Player: {self.player_score} - Computer: {self.computer_score}"
            self.result_label['text'] = "Rock smashes scissor! Computer wins!"
        elif computer == "paper":
            self.player_score += 1
            self.score_label['text'] = f"Player: {self.player_score} - Computer: {self.computer_score}"
            self.result_label['text'] = "Scissor cuts paper! Player wins!"
        else:
            self.result_label['text'] = "Tie!"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissor()
    game.run()

