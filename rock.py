import random
def rock_paper():
   player1 = input("Enter your choice: ")
   program_choice  = ["rock", "paper", "scissor"]
   choices = random.choice(program_choice)
   if player1 == choices:
        print("computer choosed: ", choices)
        print("Its... Tie..")
   elif(player1 == "rock" and choices == "scissor") or \
        (player1 == "paper" and choices == "rock") or \
         (player1 == "scissor" and choices == "paper"):
        print("computer choosed: ", choices)
        print("You win.... huraah")
   else:
        print("computer choosed: ", choices)
        print("Computer win.....")
   again_play = input("want to play again ? (yes or no)")
   if again_play == "yes":
       return rock_paper()
rock_paper()