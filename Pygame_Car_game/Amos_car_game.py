import pygame
import random
import time
pygame.mixer.init()

pygame.init()
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Car Crash Game")

#music
pygame.mixer.music.load("%5BFREE%5D_Acoustic_Guitar_Type_Beat__Upbeat___Country___Rap_Instrumental_2020_(256k).mp3")
pygame.mixer.music.play()
#colors
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
gray=(119,118,113)
green=(0,255,0)
#Image Loads
intro_image=pygame.image.load("introo.jpg")
intro_image=pygame.transform.scale(intro_image,(screen_width,screen_height))
creator=pygame.image.load("amos.jpg")
creator=pygame.transform.scale(creator,(70,70))
User_car=pygame.image.load("User_car.png")
User_car=pygame.transform.scale(User_car,(80,80))
footpath=pygame.image.load("download.jpg")
footpath=pygame.transform.scale(footpath,(150,1000))
enemy=pygame.image.load("enemy.jpg")
enemy=pygame.transform.scale(enemy,(80,80))


#Font Initialization

def Texts_func(message,size,text_pos_x,text_pos_y,color):
    font=pygame.font.SysFont(None,size)
    render=font.render(message,True,color)
    screen.blit(render,(text_pos_x,text_pos_y))
def Button(btn_pos_x,btn_pos_y,btn_sizex,btn_sizey,mess_b):
    pygame.draw.rect(screen,red,[btn_pos_x,btn_pos_y,btn_sizex,btn_sizey])
    Texts_func(mess_b,40,btn_pos_x+10,btn_pos_y+10,white)

    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if btn_pos_x<mouse[0]<btn_pos_x+100 and btn_pos_y<mouse[1]<btn_pos_y+37:
        pygame.draw.rect(screen,white,[btn_pos_x,btn_pos_y,btn_sizex,btn_sizey])       
        Texts_func(mess_b,40,btn_pos_x+10,btn_pos_y+10,red)
        if click==(1,0,0) and mess_b=="PLAY":
            pygame.mixer.music.load("Click_-_Sound_Effect_(HD)(256k).mp3")
            pygame.mixer.music.play()
            time.sleep(0.5)
            Game_Loop()
        elif click==(1,0,0) and mess_b=="QUIT":
            pygame.mixer.music.load("Click_-_Sound_Effect_(HD)(256k).mp3")
            pygame.mixer.music.play()
            time.sleep(0.5)
            pygame.quit()
            quit()


def Intro():
    exit_game=False
    pygame.mixer.music.load("%5BFREE%5D_Acoustic_Guitar_Type_Beat__Upbeat___Country___Rap_Instrumental_2020_(256k).mp3")
    pygame.mixer.music.play()
    while exit_game==False:
       
        screen.blit(intro_image,(0,0))
        screen.blit(creator,(500,280))
        Texts_func("Car Crashing 2D",60,250,100,red)
        Texts_func("Content Created By ",30,300,300,blue)
        Button(150,380,110,45,"PLAY")
        Button(550,380,95,45,"QUIT")

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
        pygame.display.update()


def OurCar(car_pos_x,car_pos_y):
    screen.blit(User_car,(car_pos_x,car_pos_y))



def Enemy_Car(enemy_x,enemy_y):
    screen.blit(enemy,(enemy_x,enemy_y))

def Crashed():
    game_over=False
    pygame.mixer.music.load("Car_Crash_Sound_Effect(256k) Trim.mp3")
    pygame.mixer.music.play()
    while not game_over:
        Texts_func("Game Over!",50,310,200,red)
        Texts_func("Press Enter To Start Again",40,250,300,white)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    Intro()
            if event.type==pygame.QUIT:
                game_over=True
            
        pygame.display.update()


def Game_Loop():
    score=0
    exit_game=False
    #Clock
    clock=pygame.time.Clock()
    fps=60
    #User Car
    car_pos_x=350
    car_pos_y=500
    car_size=30
    initial_car_pos=5
    car_vel_x=0
    enemy_car_x=random.randint(180,540)
    enemy_car_y=0
    pygame.mixer.music.load('24kGoldn_-_Mood_(Lyrics)_ft._Iann_Dior__Why_you_always_in_a_mood(256k).mp3')
    pygame.mixer.music.play()

    while exit_game==False:
        screen.fill(black)        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    car_vel_x=initial_car_pos
                elif event.key==pygame.K_LEFT:
                    car_vel_x=-initial_car_pos
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    car_vel_x=0
        car_pos_x+=car_vel_x
        
        screen.fill(gray)
        screen.blit(footpath,(0,0))
        screen.blit(footpath,(screen_width-150,0))
        OurCar(car_pos_x,car_pos_y)
        Enemy_Car(enemy_car_x,enemy_car_y)
        enemy_car_y+=5
        if enemy_car_y==600:
            score+=5
            enemy_car_x=random.randint(180,540)
            enemy_car_y=0
        Texts_func("Score: "+ str(score),50,150,0,blue)        

        if enemy_car_x<car_pos_x<enemy_car_x+90 and enemy_car_y<car_pos_y<enemy_car_y+90 or enemy_car_x<car_pos_x+98<enemy_car_x+90 and enemy_car_y<car_pos_y<enemy_car_y+90:
            Crashed()
            exit_game=True
                
        if car_pos_x<160 or car_pos_x>570:
            exit_game=True
            Crashed()       
        pygame.display.update()

        clock.tick(fps)      

    pygame.quit()
    quit()

Intro()