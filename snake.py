import pygame
import random

pygame.init()

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (243, 44, 16)
green = (51, 135, 58)

# Размер окна
dis_width = 800
dis_height = 600

# Инициализация окна игры
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Big python')

# Музыка
pygame.mixer.music.load('8bit_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)


clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont('Arial', 25)
score_font = pygame.font.SysFont('Arial', 35)


def your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, black)
    dis.blit(value, [dis_width//2 - value.get_width()//2, dis_height - 50 - value.get_height()])


def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])



def gameloop():
    game_over = False
    game_close = False
    pygame.mixer.init()

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(green)
            game_over_font = font_style.render("Игра окончена, нажмите Z для выхода или X для продолжения", True, black)
            text_rect = game_over_font.get_rect(center=(dis_width // 2, dis_height // 2))
            dis.blit(game_over_font, text_rect)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_x:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(green)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        our_snake(snake_block, snake_list)

        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameloop()
