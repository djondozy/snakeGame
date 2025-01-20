import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Serpent")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)


snake_pos = [100, 50]  
snake_body = [[100, 50], [90, 50], [80, 50]]  
snake_direction = "RIGHT"  
change_to = snake_direction
speed = 15


food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True


score = 0


clock = pygame.time.Clock()
running = True


def show_score():
    font = pygame.font.SysFont('arial', 20)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])


def game_over():
    font = pygame.font.SysFont('arial', 40)
    message = font.render("Tu as perdu, tu es trop nul!", True, RED)
    screen.fill(BLACK)
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quitter le jeu
            running = False
        if event.type == pygame.KEYDOWN:  # Gestion des touches
            if event.key == pygame.K_UP and not change_to == "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and not change_to == "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and not change_to == "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and not change_to == "LEFT":
                change_to = "RIGHT"

   
    if change_to == "UP":
        snake_direction = "UP"
    if change_to == "DOWN":
        snake_direction = "DOWN"
    if change_to == "LEFT":
        snake_direction = "LEFT"
    if change_to == "RIGHT":
        snake_direction = "RIGHT"

   
    if snake_direction == "UP":
        snake_pos[1] -= 10
    if snake_direction == "DOWN":
        snake_pos[1] += 10
    if snake_direction == "LEFT":
        snake_pos[0] -= 10
    if snake_direction == "RIGHT":
        snake_pos[0] += 10

    
    snake_body.insert(0, list(snake_pos))

    
    if snake_pos == food_pos:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()


    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
    food_spawn = True

    
    if (
        snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
        snake_pos[1] < 0 or snake_pos[1] >= HEIGHT
    ):
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    
    screen.fill(BLACK)  
    
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], 10, 10))
        pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(segment[0] + 2, segment[1] + 2, 6, 6))

    
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

   
    show_score()

    
    pygame.display.flip()

  
    clock.tick(speed)


pygame.quit()
sys.exit()
