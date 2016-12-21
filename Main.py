""" A game made using pygame to play snake. """

import pygame
from random import randint
from Character import SnakeBody
from Food import FoodBlock

#sets colours as variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#game window
SCREENWIDTH = 800
SCREENHEIGHT = 800
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snek Game")

#sprite lists
spritesList = pygame.sprite.Group()
foodList = pygame.sprite.Group()

#sprites size
width = 10
height = 10

#snake sprite
snake = SnakeBody(WHITE, width, height)
snake.rect.x = 100
snake.rect.y = 700
#add snake to sprite list
spritesList.add(snake)

#running variables
running = True
clock = pygame.time.Clock()

direction = "up"
speed = 10
foodCount = 0
foodCheck = False


#main running loop
while running:

    #frames per second
    clock.tick(30)

    for event in pygame.event.get():

        #quits game
        if event.type == pygame.QUIT:
            running = False

        ### snake movement ###
        #arrow key pressed
        elif event.type == pygame.KEYDOWN:

            #up arrow
            if event.key == pygame.K_UP:
                direction = "up"

            #down arrow
            elif event.key == pygame.K_DOWN:
                direction = "down"

            #left arrow
            elif event.key == pygame.K_LEFT:
                direction = "left"

            #right arrow
            elif event.key == pygame.K_RIGHT:
                direction = "right"

    #move snake
    if direction == "up":
        snake.moveUp(speed)

    elif direction == "down":
        snake.moveDown(speed)

    elif direction == "left":
        snake.moveLeft(speed)

    elif direction == "right":
        snake.moveRight(speed)

    ### snake collisions ###    
    #end game if snake body
##    snakeCollisionList = pygame.sprite.spritecollide(snake, bodyParts_x, bodyParts_y, False)
##    for i in snakeCollisionList:
##        running = False

    #end game if hit wall
    snakeCoord = snake.rect.center
    snakeCoord_x, snakeCoord_y = snakeCoord

    if (snakeCoord_x - (width/2)) <= 0:
        running = False

        
    elif (snakeCoord_x + (width/2)) >= SCREENWIDTH:
        running = False


    elif (snakeCoord_y - (height/2)) <= 0:
        running = False


    elif (snakeCoord_y + (height/2)) >= SCREENHEIGHT:
        running = False

    ### food ###
    if foodCheck == False:
        x = randint(0,((SCREENWIDTH - width)/10))
        y = randint(0,((SCREENHEIGHT - height)/10))

        food = FoodBlock(WHITE, width, height)
        food.rect.x = x*10
        food.rect.y = y*10

        foodList.add(food)
        
        foodCheck = True

        #add another body section every 3 foods eaten
        #if foodCount %3 == 0:
            

    foodCollisionList = pygame.sprite.spritecollide(snake, foodList, False)
    for i in foodCollisionList:
        foodCount += 1
        foodList.remove(food)
        foodCheck = False


        
    #update sprite list
    spritesList.update()
    foodList.update()

    #remove sprite trails
    screen.fill(BLACK)

    #draw sprites
    spritesList.draw(screen)
    foodList.draw(screen)
    
    #refresh screen
    pygame.display.update()


#quit game
pygame.quit()


