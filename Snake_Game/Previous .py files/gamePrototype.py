################################################################################
# THis is the first prototype of the snake game i'll be creating.
# This has controls and displays the user score.
# after the game is over we can either continue to play or exit the window
################################################################################
import pygame
import random
import time
pygame.init()

green = (0,255,0)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

clock = pygame.time.Clock()

display_width = 800
display_height = 400
snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont('sahadeva', display_width//20)
score_font = pygame.font.SysFont('nakula',display_width//20)

d = pygame.display.set_mode((display_width,display_height))		# for a layout of 400*200
pygame.display.set_caption('SNAKE GAME')	# sets the tile of the project

score_pos = [0,0]
def Your_score(score):
    value = score_font.render(f'Your score:{score}', True, blue)
    d.blit(value, score_pos)


def message(txt,color):
    mesg = font_style.render(txt,True, color)
    d.blit(mesg, [50,50])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(d, red, [x[0],x[1], snake_block,snake_block])

def game_loop():
    game_over = False
    game_close = False

    x1 = display_width/2
    y1 = display_height/2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1


    foodx = round(random.randrange(0,display_width - snake_block) /10.0 )* 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0 ) *10.0

    while not game_over:						#While loop for the screen to get displayed

        pygame.display.update()

        while game_close == True:
            d.fill(black)
            message('You lost, Press p-play again or q-quit', green)

            Your_score(length_of_snake -1)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = False
                        game_over = True

                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():		# until quit button is pressed


        	if event.type == pygame.QUIT:
        		game_over = True                # if event is quit / if exit button is pressed it exits from the screen
        	if event.type == pygame.KEYDOWN:
        		if event.key == pygame.K_LEFT:
        			x_change = -snake_block
        			y_change = 0
        		elif event.key == pygame.K_RIGHT:
        			x_change = snake_block
        			y_change = 0
        		elif event.key == pygame.K_UP:
        			x_change = 0
        			y_change = -snake_block
        		elif event.key == pygame.K_DOWN:
        			x_change = 0
        			y_change = snake_block

        x1 += x_change
        y1 += y_change
     # IF YOU DONT WANT END THE GAME IF SNAKE TOUCHES THE BORDER REMOVE THE BELOW COMMENTS
     #   if x1 > display_width:
     #       x1 = 0
     #   elif x1 < 0:
     #       x1 = display_width
     #   elif y1 > display_height:
     #      y1 = 0
     #   elif y1 < 0:
     #       y1 = display_height
        if x1 >= display_width or x1 <= 0 or y1 >= display_height or y1<=0:
            game_close = True

        d.fill(black)
        pygame.draw.circle(d,green, [int(foodx), int(foody)], 5)
        snake_head =[]
        snake_head.append(x1)
        snake_head.append(y1)

        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block,snake_list)
        Your_score(length_of_snake -1)

        pygame.display.update()


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1


        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
