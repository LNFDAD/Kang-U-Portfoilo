import pygame
import random

WHITE = (255,255,255) # 흰색의 값 ( 배경 색깔 )
pad_width = 740 # 게임판의 폭
pad_height = 370 # 게임판의 높이
background_width = 740

def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))

def back(background , x, y):
    global gamepad
    gamepad.blit(background, (x, y))

def airplane(x,y): # 비행기를 내가 원하는 x,y 좌표에 놓는 함수
    global gamepad, aircraft
    gamepad.blit(aircraft, (x,y))

def runGame():
    global gamepad , aircraft , clock , background1 , background2 , bat , fires# 변수선언

    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0 # y좌표의 변화량

    background1_x = 0
    background2_x = background_width

    bat_x = pad_width
    bat_y = random.randrange(0,pad_height)

    fire_x = pad_width
    fire_y = random.randrange(0,pad_height)
    random.shuffle(fires)
    fire = fires[0]

    crashed = False # 나중에 게임 졸료를 위한 변수 ( 게임 종료 플래그 )
    while not crashed:
        for event in pygame.event.get(): # 게임에서 발생하는 이벤트들을 갖고옴
            if event.type == pygame.QUIT: # 만약 창을 닫는다면
                crashed = True # crashed를 True로 설정한후 종료.
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  #만약 위키가 눌리면 5픽셀 위로 (y_change = -5)
                    y_change = -5
                
                elif event.key == pygame.K_DOWN: # 만약 아래키가 눌리면 5픽셀 아래로 (y_change = 5)
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        y += y_change # 키보드 입력에 따라 값변경

        gamepad.fill(WHITE) # 반대로 창을 닫지 않는다면 게임판의 색깔을 설정

        background1_x -= 2
        background2_x -= 2

        bat_x -= 7
        if bat_x <= 0:
            bat_x = pad_width
            bat_y = random.randrange(0,pad_height)
        if fire == None:
            fire_x -= 30
        else:
            fire_x -= 15

        if fire_x <= 0:
            fire_x = pad_width
            fire_y = random.randrange(0,pad_height)
            random.shuffle(fires)
            fire = fires[0]      
             
        if background1_x == -background_width:
            background1_x = background_width

        if background2_x == -background_width:
            background2_x = background_width

        drawObject(background1 , background1_x,0)
        drawObject(background2 , background2_x,0)
        drawObject(bat,bat_x,bat_y)
        if fire != None:
            drawObject(fire,fire_x,fire_y)
        drawObject(aircraft,x,y)
        back(background1, background1_x , 0)
        back(background2, background2_x , 0)

        airplane(x,y) # 호출
        pygame.display.update() 
        clock.tick(60) # FPS 값을 60으로 설정.

    pygame.quit() # 종료.



def initGame():
    global gamepad , clock , aircraft , background1 , background2 , bat, fires

    fires = []
 
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height)) # 게임판의 크기를 pad_width x pad_height 로 정함.
    pygame.display.set_caption('test') # 타이틀 설정
    aircraft = pygame.image.load('images/plane.png')
    background1 = pygame.image.load('images/background.png')
    background2 = background1.copy()
    bat = pygame.image.load('images/bat.png')
    fires.append(pygame.image.load('images/fireball.png'))
    fires.append(pygame.image.load('images/fireball2.png'))

    for i in range(5):
        fires.append(None)

    clock = pygame.time.Clock() # 게임의 프레임 수
    runGame()# runGame 호출

if __name__ == '__main__':
    initGame()
