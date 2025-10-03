import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
BULLET_SIZE = 10

# Set up some variables
player_x, player_y = WIDTH / 2, HEIGHT / 2
player_speed = 5
bullets = []
enemies = []

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot a bullet
                bullets.append([player_x, player_y])

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Move the bullets
    for i, bullet in enumerate(bullets):
        bullet[1] -= 5
        if bullet[1] < 0:
            bullets.pop(i)

    # Create enemies
    if random.random() < 0.1:
        enemies.append([random.randint(0, WIDTH), random.randint(0, HEIGHT)])

    # Move the enemies
    for i, enemy in enumerate(enemies):
        enemy[1] += 2
        if enemy[1] > HEIGHT:
            enemies.pop(i)

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    for bullet in bullets:
        pygame.draw.rect(screen, (0, 255, 0), (bullet[0], bullet[1], BULLET_SIZE, BULLET_SIZE))
    for enemy in enemies:
        pygame.draw.rect(screen, (0, 0, 255), (enemy[0], enemy[1], PLAYER_SIZE, PLAYER_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)


