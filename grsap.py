import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the game variables
player_score = 0
computer_score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the player's choice
            player_choice = None
            if 100 <= event.pos[0] <= 300 and 200 <= event.pos[1] <= 300:
                player_choice = "rock"
            elif 350 <= event.pos[0] <= 550 and 200 <= event.pos[1] <= 300:
                player_choice = "paper"
            elif 100 <= event.pos[0] <= 300 and 350 <= event.pos[1] <= 450:
                player_choice = "scissors"

            # Get the computer's choice
            computer_choice = random.choice(["rock", "paper", "scissors"])

            # Determine the winner
            if player_choice == computer_choice:
                print("It's a tie!")
            elif (player_choice == "rock" and computer_choice == "scissors") or \
                 (player_choice == "paper" and computer_choice == "rock") or \
                 (player_choice == "scissors" and computer_choice == "paper"):
                print("You win this round!")
                player_score += 1
            else:
                print("Computer wins this round!")
                computer_score += 1

    # Draw everything
    screen.fill(WHITE)

    # Draw the player's score
    player_score_text = font.render(f"Player score: {player_score}", True, BLACK)
    screen.blit(player_score_text, (100, 50))

    # Draw the computer's score
    computer_score_text = font.render(f"Computer score: {computer_score}", True, BLACK)
    screen.blit(computer_score_text, (350, 50))

    # Draw the rock button
    pygame.draw.rect(screen, RED, (100, 200, 200, 100))
    rock_text = font.render("Rock", True, BLACK)
    screen.blit(rock_text, (150, 220))

    # Draw the paper button
    pygame.draw.rect(screen, GREEN, (350, 200, 200, 100))
    paper_text = font.render("Paper", True, BLACK)
    screen.blit(paper_text, (400, 220))

    # Draw the scissors button
    pygame.draw.rect(screen, BLUE, (100, 350, 200, 100))
    scissors_text = font.render("Scissors", True, BLACK)
    screen.blit(scissors_text, (150, 370))

    # Update the display
    pygame.display.flip()