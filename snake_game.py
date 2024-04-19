import pygame 
import random

# Initialize the pygame
pygame.init()

# set up display 
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# snake initial position and properties

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# food position and properties
food_pos = [random.randrange(1, screen_width//10)*10, random.randrange(1, screen_height//10)*10]
food_spawn = True

# score 
score = 0

# clock for controllong the speed of the game
clock = pygame.time.Clock()

def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

def draw_food():
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

def update_score(score):
    font = pygame.font.SysFont('arial', 20)
    score_surface = font.render('Score: {}'.format(score), True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (320, 10)
    screen.blit(score_surface, score_rect)

# Game over function

def game_over():
    font = pygame.font.SysFont('None', 25)
    game_over_surface = font.render("Game Over", True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width/2, screen_height/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(1000)
    quit()

# Main logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    
    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and not snake_direction == 'DOWN':
        snake_direction = 'UP'
    if change_to == 'DOWN' and not snake_direction == 'UP':
        snake_direction = 'DOWN'
    if change_to == 'LEFT' and not snake_direction == 'RIGHT':
        snake_direction = 'LEFT'
    if change_to == 'RIGHT' and not snake_direction == 'LEFT':
        snake_direction = 'RIGHT'

    # Moving the snake
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    if snake_direction == 'DOWN':
        snake_pos[1] += 10
    if snake_direction == 'LEFT':
        snake_pos[0] -= 10
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    # if the snake eats the food
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()
    
    if not food_spawn:
        food_pos = [random.randrange(1, screen_width//10)*10, random.randrange(1, screen_height//10)*10]
    
    food_spawn = True

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > screen_width-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > screen_height-10:
        game_over()
    
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()


    # Drawing the snake and food]
    screen.fill(black)
    draw_snake(snake_body)
    draw_food()
    update_score(score)

    pygame.display.update()

    clock.tick(15)