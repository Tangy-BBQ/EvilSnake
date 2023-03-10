import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 1200
dis_height = 800

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Steve')

clock = pygame.time.Clock()


font_style = pygame.font.SysFont("bahnschrift", 45)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 4, dis_height / 2])


def gameLoop():
    game_over = False
    game_close = False

    snake_block = 20
    snake_speed = 10

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) /
                  snake_block) * snake_block
    foody = round(random.randrange(0, dis_height -
                  snake_block) / snake_block) * snake_block

    enemyx = round(random.randrange(
        0, dis_width - snake_block) / snake_block) * snake_block
    enemyy = round(random.randrange(0, dis_height -
                   snake_block) / snake_block) * snake_block
    enemyxs = []
    enemyys = []
    enemyxs.append(enemyx)
    enemyys.append(enemyy)

    direction = -1

    inc = False

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 1:
                    direction = 0
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and direction != 0:
                    direction = 1
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and direction != 3:
                    direction = 2
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and direction != 2:
                    direction = 3
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        for x in range(len(enemyxs)):
            pygame.draw.rect(
                dis, red, [enemyxs[x], enemyys[x], snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(
                0, dis_height - snake_block) / snake_block) * snake_block

            enemyx = round(random.randrange(
                0, dis_width - snake_block) / snake_block) * snake_block
            enemyy = round(random.randrange(
                0, dis_height - snake_block) / snake_block) * snake_block

            enemyxs.append(enemyx)
            enemyys.append(enemyy)

            Length_of_snake += 1

        for x in range(len(enemyxs)):
            if x1 == enemyxs[x] and y1 == enemyys[x]:
                game_close = True

        if Length_of_snake % 2 == 0:
            if inc:
                inc = False
                snake_speed = snake_speed + 5
                # snake_block = snake_block - (snake_block / 10)

                for x in range(len(enemyxs)):
                    enemyxs[x] = round(random.randrange(
                        0, dis_width - snake_block) / snake_block) * snake_block
                    enemyys[x] = round(random.randrange(
                        0, dis_width - snake_block) / snake_block) * snake_block
        else:
            inc = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
