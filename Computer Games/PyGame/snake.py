import pygame
import time
import random

pygame.init()

white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)

disWidth = 800
disHeight = 600

dis = pygame.display.set_mode((disWidth, disHeight))
pygame.display.set_caption('Snake Game by Glen')

clock = pygame.time.Clock()

snakeBlock = 10
snakeSpeed = 30

fontStyle = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = fontStyle.render(msg, True, color)
    dis.blit(mesg, [disWidth/2, disHeight/2])

def gameLoop():
    gameOver = False
    gameClose = False

    x1 = disWidth / 2
    y1 = disHeight / 2

    x1Change = 0
    y1Change = 0

    foodx = round(random.randrange(0, disWidth - snakeBlock) / 10.0)
    foody = round(random.randrange(0, disWidth - snakeBlock) / 10.0)

    while not gameOver:

        while gameClose == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_Q:
                        gameOver = True
                        gameClose = False
                    if event.type == pygame.K_C:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1Change = -snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_RIGHT:
                    x1Change = snakeBlock
                    y1Change = 0
                elif event.key == pygame.K_UP:
                    x1Change = 0
                    y1Change = -snakeBlock
                elif event.key == pygame.K_DOWN:
                    x1Change = 0
                    y1Change = snakeBlock

        if x1 >= disWidth or x1 < 0 or y1 >+ disHeight or y1 < 0:
            gameClose = True
    
        x1 += x1Change
        y1 += y1Change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snakeBlock, snakeBlock])
        pygame.draw.rect(dis, black, [x1,y1, snakeBlock, snakeBlock])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Yummy!!")

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()

gameLoop()

# https://www.edureka.co/blog/snake-game-with-pygame/