import pygame
import time
import random

pygame.init()
display_height = 600
display_width = 800
display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Snake by MHRDp')

blue = (0, 0, 225)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

snake_speed = 15
snake_block = 10

font_style = pygame.font.SysFont('bahnschrift', 30)
score_style = pygame.font.SysFont('comicsansms', 25)
clock = pygame.time.Clock()

def message(msg, color):
    message = font_style.render(msg, True, color)
    display.blit(message, [display_width / 4, display_height / 2])

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

def score(num):
    value = score_style.render(f'Your score: {num}', True, black)
    display.blit(value, [0, 0])

def main_game():
    game_over = False
    game_close = False
    snake_length = 1
    snake_list = []

    x1 = display_width / 2
    y1 = display_width / 2
    x1_change = y1_change = 0

    food_x = round(random.randrange(0, display_width - snake_block) // 10) * 10
    food_y = round(random.randrange(0, display_height - snake_block) // 10) * 10
    
    trap_x = round(random.randrange(0, display_width - snake_block) // 10) * 10
    trap_y = round(random.randrange(0, display_height - snake_block) // 10) * 10

    if trap_x == food_x and trap_y == food_y:
        trap_x = trap_x
        trap_y = trap_y

    while not game_over:
        while game_close == True:
            display.fill(white)
            message("You Lost, Press Q to quit, or C to play again!", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        main_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10

        if x1 == display_width or x1 < 0:
            x1 = x1 % display_width
        if y1 == display_height or y1 < 0:
            y1 = y1 % display_height

        x1 += x1_change
        y1 += y1_change
        display.fill(white)

        pygame.draw.rect(display, blue, [food_x, food_y, snake_block, snake_block])
        pygame.draw.rect(display, red, [trap_x, trap_y, snake_block, snake_block])

        snake_head = []

        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        score(snake_length-1)
        
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, display_width - snake_block) // 10) * 10
            food_y = round(random.randrange(0, display_height - snake_block) // 10) * 10
            snake_length += 1
            print(f'snake_list: {snake_list}')
            print(f'snake_head: {snake_head}')

        if x1 == trap_x and y1 == trap_y:
            game_close = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main_game()
