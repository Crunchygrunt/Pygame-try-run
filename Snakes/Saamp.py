import pygame
import random
import os

pygame.mixer.init()

pygame.init()


gold=[184,134,11]    #Defining
red=[255,0,0]        #colours 
black=[0,0,0]        #for game window
green=[0,255,0]
purple=[0,0,139]
blue=[135,206,250]

width=900      #dimensions for window
height=600
gamewindow=pygame.display.set_mode((width,height))

bgimg= pygame.image.load("esnk.jpg")
sad= pygame.image.load("sad.jpg")
khu= pygame.image.load("khu.jfif")
bgimg= pygame.transform.scale(bgimg,(width,height)).convert_alpha()
sad= pygame.transform.scale(sad,(width,height)).convert_alpha()
khu= pygame.transform.scale(khu,(width,height)).convert_alpha()


#Title for game
pygame.display.set_caption("Hsssss")  
pygame.display.update()


init_velocity=3
clock=pygame.time.Clock()    #for updating framerate(fps)

font= pygame.font.SysFont('gabriola',40)
def text_screen(text,color,x,y):
    screen_text= font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snk(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
       pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill((233,200,210))
        gamewindow.blit(khu,(0,0))
        text_screen("Welcome to 'The Snake Game'",gold,290,250)
        text_screen("Press Space Bar to play",gold,330,300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('music.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)
#Game loop
def gameloop():
    exit_game=False
    game_over=False

    snake_x=45
    snake_y=55

    velocity_x=0
    velocity_y=0

    snk_list=[]
    snk_length=1

    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write(0)

    with open("highscore.txt","r") as f:
        highscore= f.read()
    
    food_x= random.randint(20,width/2)    #randint is for generating random numbers... 
    food_y= random.randint(40,height/1.5)   #for the food to appear
    score=0
    snake_size=20
    fps=60
    
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            gamewindow.fill(purple)
            gamewindow.blit(sad,(0,0))
            text_screen("      Press Enter To Play Again",red,175,50)
            text_screen("    Score: "+str(score),blue,300,100)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x+= init_velocity
                        velocity_y=0
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x-= init_velocity
                        velocity_y=0
                    
                    if event.key == pygame.K_UP:
                        velocity_y-= init_velocity
                        velocity_x=0
                    
                    if event.key == pygame.K_DOWN:
                        velocity_y+= init_velocity
                        velocity_x=0
                    

            snake_x+= velocity_x
            snake_y+= velocity_y

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=10

                food_x= random.randint(20,width/2)
                food_y= random.randint(20,height/2)
                snk_length+=5
                if score>int(highscore):
                    highscore=score

            gamewindow.fill(black)     #making window white
            gamewindow.blit(bgimg,(0,0))
            text_screen("Score: "+str(score) + "    Highscore: "+str(highscore),blue,5,5)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
            
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load('lost.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>width or snake_y<0 or snake_y>height:
                game_over=True
                pygame.mixer.music.load('lost.mp3')
                pygame.mixer.music.play()

            plot_snk(gamewindow,green,snk_list,snake_size)
        pygame.display.update()    #Updating the changes
        clock.tick(fps)

    pygame.quit()
    quit()
#gameloop()
welcome()