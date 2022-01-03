#Main Screen


import pygame
from random import randint
pygame.init()  
WIDTH = 800
HEIGHT = 800
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,104,17)

game = True
menu = True
gamePlay = False
instructions = False
restartScreen = False

timeDelay = 0

life = 1

vertexAX = 705
vertexAY = 250
vertexBX = 740
vertexBY = 300
vertexCX = 740
vertexCY = 200

cometX1 = randint(100, 1155)
cometY1 = -50
cometX2 = randint(100, 1155)
cometY2 = -150
cometX3 = randint(100, 1155)
cometY3 = -250
cometX4 = randint(100, 1155)
cometY4 = -350
cometX5 = randint(100, 1155)
cometY5 = -450
cometX6 = randint(100, 1155)
cometY6 = -550

starX = randint(100, 1155)
starY = randint(-400, -35)

timer = pygame.time.Clock()
moveSpeed = 3
frameTimer = 0
gameScore = 0
highscore = 0

font1 = pygame.font.SysFont("bankgothic",70)
font2 = pygame.font.SysFont("MV Boli",50)
font3 = pygame.font.SysFont("MV Boli",150)
graphicGAMENAME = font1.render("SPACE DODGE IV" , 0 , WHITE)
graphicPLAY = font1.render("PLAY" , 0 , WHITE)
graphicINSTRUCTIONS = font1.render("INSTRUCTIONS" , 0 , WHITE)
graphicHIGHSCORE = font1.render("HIGHSCORE" , 0 , WHITE)
graphicEXIT = font1.render("EXIT" , 0 , WHITE)
graphicSCORE = font2.render("Score: " +str(gameScore),0,WHITE)
graphicRESTART = font3.render("YOU LOST!",0,WHITE)

spaceBG = pygame.image.load("space.jpg").convert_alpha()
spaceBG = pygame.transform.scale(spaceBG, (WIDTH, HEIGHT))

cometPic = pygame.image.load("comet.png").convert_alpha()
cometPic = pygame.transform.scale(cometPic, (60, 150))

starPic = pygame.image.load("star.png").convert_alpha()
starPic = pygame.transform.scale(starPic, (100, 100))

playerRocket = pygame.image.load("rocket.png").convert_alpha()
playerRocket = pygame.transform.scale(playerRocket, (100,180))

#colour collision initialization
        
while game == True:
    pygame.event.clear()
    pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    if menu == True:
        timeDelay = 75
        gameWindow.fill(BLACK)
        gameWindow.blit(spaceBG,(0,0))
        pygame.draw.rect(gameWindow, WHITE, (4,50 , +792, +100),3)
        gameWindow.blit(graphicGAMENAME, (75,60))

        pygame.draw.rect(gameWindow, WHITE, (100,200 , +600, +100),3)
        gameWindow.blit(graphicPLAY, (300, 210))
                
        pygame.draw.rect(gameWindow, WHITE, (100,325 , +600, +100),3)
        gameWindow.blit(graphicINSTRUCTIONS, (110, 335))

        pygame.draw.rect(gameWindow, WHITE, (100,450 , +600, +100),3)
        gameWindow.blit(graphicHIGHSCORE, (170,460))

        pygame.draw.rect(gameWindow, WHITE, (100,575 , +600, +100),3)
        gameWindow.blit(graphicEXIT, (300,585))

        pygame.draw.polygon(gameWindow, WHITE,((vertexAX,vertexAY), (vertexBX,vertexBY),(vertexCX,vertexCY)),4)


        if keys[pygame.K_DOWN] and vertexAY != 625: 
            vertexAY += 125
            vertexBY += 125
            vertexCY += 125
        if keys[pygame.K_UP] and vertexAY != 250: 
            vertexAY -= 125
            vertexBY -= 125
            vertexCY -= 125
        if vertexAY == 250 and keys[pygame.K_RETURN]:
            menu = False
            gamePlay = True  
            playerX = 700
            playerY = 650
            countSetup = 0
        if vertexAY == 625 and keys[pygame.K_RETURN]:
            break
    #end while
            
        if vertexAY == 375 and keys[pygame.K_RETURN]:
            menu = False
            instructions = True
            if instructions == True:
                instructionsBG = pygame.image.load("instructions.png").convert_alpha()
                instructionsBG = pygame.transform.scale(instructionsBG, (WIDTH, HEIGHT))
                gameWindow.blit(instructionsBG,(0,0))
                pygame.display.update()
                pygame.time.delay(1)

    while gamePlay == True:
        timeDelay = 10
        if countSetup == 0:
            gameWindow = pygame.display.set_mode((WIDTH+400, HEIGHT))
            spaceBG = pygame.image.load("space.jpg").convert_alpha()
            spaceBG = pygame.transform.scale(spaceBG, (WIDTH+400, HEIGHT))
            countSetup = 1
        #endif 
        gameWindow.blit(spaceBG,(0,0))
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if life == 1:
            gameWindow.blit(cometPic,(cometX1,cometY1))
            cometY1 += 1
            if cometY1 > 800:
                cometY1 = randint(-400, -35)
                cometX1 = randint(100, 1040)
                cometY1 += 1
            
            gameWindow.blit(cometPic,(cometX2,cometY2))
            cometY2 += 1
            if cometY2 > 800:
                cometY2 = randint(-400, -35)
                cometX2 = randint(100,1040)
                cometY2 += 1

            gameWindow.blit(cometPic,(cometX3,cometY3))
            cometY3 += 1
            if cometY3 > 800:
                cometX3 = randint(100, 1040)
                cometY3 = randint(-400, -35)
                cometY3 += 1

            gameWindow.blit(cometPic,(cometX4,cometY4))
            cometY4 += 1
            if cometY4 > 800:
                cometX4 = randint(100, 1040)
                cometY4 = randint(-400, -35)
                cometY4 += 1
            
            gameWindow.blit(cometPic,(cometX5,cometY5))
            cometY5 += 1
            if cometY5 > 800:
                cometX5 = randint(100, 1040)
                cometY5 = randint(-400, -35)
                cometY5 += 1

            gameWindow.blit(cometPic,(cometX6,cometY6))
            cometY6 += 1
            if cometY6 > 800:
                cometX6 = randint(100, 1040)
                cometY6 = randint(-400, -35)
                cometY6 += 1
            
            gameWindow.blit(starPic,(starX,starY))
            starY += 1
            if starY > 800:
                starX = randint(100,1040)
                starY = randint(-400, -35)
                starY += 1

            #collision
            #rocket tip
            if cometX1 <= playerX+40 <= cometX1+60 and cometX1<= playerX+60 <= cometX1+60 and cometY1 <= playerY+15 <= cometY1+150:
                gamePlay = False
                restartScreen = True
            if cometX2 <= playerX+40 <= cometX2+60 and cometX2<= playerX+60 <= cometX2+60 and cometY2 <= playerY+15 <= cometY2+150:
                gamePlay = False
                restartScreen = True
            if cometX3 <= playerX+40 <= cometX3+60 and cometX3<= playerX+60 <= cometX3+60 and cometY3 <= playerY+15 <= cometY3+150:
                gamePlay = False
                restartScreen = True
            if cometX4 <= playerX+40 <= cometX4+60 and cometX4<= playerX+60 <= cometX4+60 and cometY4 <= playerY+15 <= cometY4+150:
                gamePlay = False
                restartScreen = True
            if cometX5 <= playerX+40 <= cometX5+60 and cometX5<= playerX+60 <= cometX5+60 and cometY5 <= playerY+15 <= cometY5+150:
                gamePlay = False
                restartScreen = True
            if cometX6 <= playerX+40 <= cometX6+60 and cometX6<= playerX+60 <= cometX6+60 and cometY6 <= playerY+15 <= cometY6+150:
                gamePlay = False
                restartScreen = True
            if starX <= playerX+50 <= starX+100 and starY <= playerY <= starY+100:
                gameScore += 100
                starX = randint(100,1040)
                starY = randint(-400, -35)

            #rocket left side
            if cometX1 <= playerX+20 <= cometX1+60 and cometY1 <= playerY+50 <= cometY1+150:
                gamePlay = False
                restartScreen = True
            if cometX2 <= playerX+20 <= cometX2+60 and cometY2 <= playerY+50 <= cometY2+150:
                gamePlay = False
                restartScreen = True
            if cometX3 <= playerX+20 <= cometX3+60 and cometY3 <= playerY+50 <= cometY3+150:
                gamePlay = False
                restartScreen = True
            if cometX4 <= playerX+20 <= cometX4+60 and cometY4 <= playerY+50 <= cometY4+150:
                gamePlay = False
                restartScreen = True
            if cometX5 <= playerX+20 <= cometX5+60 and cometY5 <= playerY+50 <= cometY5+150:
                gamePlay = False
                restartScreen = True
            if cometX6 <= playerX+20 <= cometX6+60 and cometY6 <= playerY+50 <= cometY6+150:
                gamePlay = False
                restartScreen = True
            if starX <= playerX <= starX+100 and starY <= playerY <= starY+100:
                gameScore += 100
                starX = randint(100,1040)
                starY = randint(-400, -35)

            #rocket right side
            if cometX1 <= playerX+80 <= cometX1+60 and cometY1 <= playerY+50 <= cometY1+150:
                gamePlay = False
                restartScreen = True
            if cometX2 <= playerX+80 <= cometX2+60 and cometY2 <= playerY+50 <= cometY2+150:
                gamePlay = False
                restartScreen = True
            if cometX3 <= playerX+80 <= cometX3+60 and cometY3 <= playerY+50 <= cometY3+150:
                gamePlay = False
                restartScreen = True
            if cometX4 <= playerX+80 <= cometX4+60 and cometY4 <= playerY+50 <= cometY4+150:
                gamePlay = False
                restartScreen = True
            if cometX5 <= playerX+80 <= cometX5+60 and cometY5 <= playerY+50 <= cometY5+150:
                gamePlay = False
                restartScreen = True
            if cometX6 <= playerX+80 <= cometX6+60 and cometY6 <= playerY+50 <= cometY6+150:
                gamePlay = False
                restartScreen = True
            if starX <= playerX+100 <= starX+100 and starY <= playerY <= starY+100:
                gameScore += 100
                starX = randint(100,1040)
                starY = randint(-400, -35)
                


            #comet: 60 x 150
            #player: 100 x 180

            gameWindow.blit(playerRocket,(playerX,playerY))
            if keys[pygame.K_RIGHT] and playerX <= 1090:
                playerX += moveSpeed
            elif keys[pygame.K_LEFT] and playerX >= -40:
                playerX -= moveSpeed

            frameTimer += 1
            if frameTimer % 100 == 0:
                gameScore += 1

            if gameScore > highscore:
                highscore = gameScore

            graphicSCORE = font2.render("Score: " +str(gameScore),1,WHITE)
            gameWindow.blit(graphicSCORE, (20,20))

        if restartScreen == True:
            gameWindow.blit(graphicRESTART, (200,100))
        pygame.display.update()
        timer.tick(250)
        

        #if vertexAY == 500:
    
    
   

    pygame.display.update()
    pygame.time.delay(timeDelay)
#end while    

pygame.display.update()
pygame.quit()

   
