import pygame
from methode import *

pygame.init()
screen=pygame.display.set_mode()
running=True
compteur=0
color=(0,0,0)

statue_green=False
statue_red=False
statue_blue=False
r,g,b=0,0,0


while running:
    click=False
    for event in pygame.event.get():
        if event.type==pg.MOUSEBUTTONDOWN:
            click=True
        if event.type==pg.QUIT:
            running=False




    screen.fill(color)
    green=button(screen, "Green",[0,0,200,100],border=5)

    red=button(screen,"Red",[200,0,200,100],border=5)
    blue=button(screen,"Blue",[400,0,200,100],border=5)


    if statue_green:
        text_green="ON"
        g=255
        color=(r,g,b)
    else:
        text_green='OFF'


    if statue_red:
        text_red="ON"
        r=255
        color=(r,g,b)
    else:
        text_red="OFF"
        r=0
    if statue_blue:
        text_blue="ON"
        b=255
        color=(r,g,b)
    else:
        text_blue="OFF"
        b=0

    button_statue_green=button(screen,text_green,[0,100,200,100],border=5)
    button_statue_red=button(screen,text_red,[200,100,200,100],border=5)
    button_statue_blue=button(screen,text_blue,[400,100,200,100],border=5)



    if click_in(click,button_statue_green[0],button_statue_green[1]):
        statue_green=not statue_green
        if statue_green:
            text_green="ON"
            g=255
        else:
            text_green="OFF"
            g=0
            color=(r,g,b)

    if click_in(click,button_statue_red[0],button_statue_red[1]):
        statue_red=not statue_red
        if statue_red:
            text_red="ON"
            r=255
        else:
            text_red="OFF"
            r=0
            color=(r,g,b)

    if click_in(click,button_statue_blue[0],button_statue_blue[1]):
        statue_blue=not statue_blue
        if statue_blue:
            text_blue="ON"
            b=255
        else:
            text_blue="OFF"
            b=0
            color=(r,g,b)



    if click_in(click,green[0],green[1]):
         color=GREEN
         statue_green=False
         statue_red=False
         statue_blue=False

         print(color)
    if click_in(click,red[0],red[1]):
         color=RED
         statue_green=False
         statue_red=False
         statue_blue=False
         print(color)
    if click_in(click,blue[0],blue[1]):
         color=BLUE
         print(color)
         statue_green=False
         statue_red=False
         statue_blue=False


    pygame.display.flip()

pygame.quit()
