# Créé par PIERRE.PELLEROT, le 12/03/2023
"""Ce fichier contient différentes fonctions et constante utilisées fréquement"""
import pygame as pg
from random import randint

"""Constantes"""

"""couleur"""
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
ORANGE=(255,127,0)
CYAN=(0,255,255)




def ecrire(screen, texte, position=(0,0), color=(0,0,0), taille =30, police='calibri',simulation=False):
    font= pg.font.SysFont(police, int(taille), True)
    rendu=font.render(str(texte),1,color)
    dim=rendu.get_rect()
    if simulation:
        return dim[2],dim[3]
    screen.blit(rendu,position)

    return dim[2],dim[3]

def mouse_on(object, taille_object=[64,64]):
        position_souris=pg.mouse.get_pos()
        position_object=[object.x, object.y]
        try:
            taille_object=[object.taille_x, object.taille_y]
        except:
            pass

        for i in range(position_object[0],position_object[0]+taille_object[0]):
            for j in range(position_object[1],position_object[1]+taille_object[1]):

                if i==position_souris[0] and j==position_souris[1]:
                    return True

        return False

def point_in( coordonnees, objet, taille_objet=[64,64]):
    """Vérifie si les coordonnees rentrées appartiennent à l'objet"""

    if type(objet)==list or type(objet)==tuple:
        for i in range(int(objet[0]),int(objet[0])+int(taille_objet[0])):
            for j in range(int(objet[1]),int(objet[1])+int(taille_objet[1])):

                if i==coordonnees[0] and j==coordonnees[1]:
                    return True

    elif type(objet)!=int:



        objet_c=[objet.c_collision[0], objet.c_collision[1]]
        try:
           taille_objet=[objet.t_collision[0],objet.t_collision[1]]
        except:

            pass
        for i in range(objet_c[0],objet_c[0]+taille_objet[0]):
            for j in range(objet_c[1],objet_c[1]+taille_objet[1]):

                if i==coordonnees[0] and j==coordonnees[1]:
                    return True

    return False


def mouse_in( position_object, taille_object=[64,64]):

    position_souris=pg.mouse.get_pos()
    if point_in(position_souris,position_object,taille_object):
        return True
    return False

def click_in(click, position, taille_object=[64,64], pos=False):

    if click:
        if mouse_in(position,taille_object):
            return True
    return False


def ligne( screen , pos , long , color=(0,0,0) , larg=1):
    pg.draw.rect(screen, color, (pos[0],pos[1],long,larg))

def colonne(screen, pos, long,color=(0,0,0),larg=1):
    ligne(screen, pos, larg,color,long)

def button(screen, text, dim, button_color=(255,255,255), text_color=(0,0,0), border=0,border_color=(0,0,0),size_text=0):


    if size_text==0:

        size_text=dim[3]-2
        long_texte=ecrire(screen,text,(0),taille=size_text,simulation=True)

        if long_texte[0]>=dim[2]:
            long_texte=ecrire(screen,text,(0),taille=10,simulation=True)

            size_text=dim[2]*10//long_texte[0]-1
            long_texte=ecrire(screen,text,(0),taille=size_text,simulation=True)




    rect(screen,(dim[0],dim[1]),(dim[2],dim[3]),button_color,border,border_color)

    long_texte=ecrire(screen,text,color=text_color,taille=size_text,simulation=True)

    if long_texte[1]>=dim[3]:
        #print(long_texte,dim)

        size_text=dim[3]-2
        long_texte=ecrire(screen,text,(0),taille=size_text,simulation=True)

    if long_texte[0]>=dim[2]:
        long_texte=ecrire(screen,text,(0),taille=10,simulation=True)

        size_text=dim[2]*10//long_texte[0]-1
        long_texte=ecrire(screen,text,(0),taille=size_text,simulation=True)




    pos=( dim[0] + dim[2] / 2 - long_texte[0] / 2 + border  ,  dim[1] + dim[3] / 2 - long_texte[1] / 2 + border +1 )  #centrage du texte

    ecrire(screen,text,pos,text_color,size_text)

    return (dim[0],dim[1]) , (dim[2],dim[3])









def rect(screen,pos,dim,color,border=0,border_color=(0,0,0),full=-1):
    if full<=0:
        pg.draw.rect(screen,color,(pos[0]+border,pos[1]+border,dim[0]-border*2,dim[1]-border*2))
        if border>0:
            ligne(screen,pos,dim[0],border_color,border)
            ligne(screen,(pos[0],pos[1]+dim[1]-border),dim[0],border_color,border)
            colonne(screen,pos,dim[1]-border,border_color,border)
            colonne(screen,(pos[0]+dim[0]-border,pos[1]+border),dim[1]-border,border_color,border)
    else:
        pg.draw.rect(screen,color,(pos[0]+border,pos[1]+border,dim[0]-border*2,dim[1]-border*2),full)

def probabilité(prob=0.5):
        """Probabilité sur 1. Minimum 0.001"""
        nb=randint(0,1000)
        if nb>(prob*1000):
            return False
        else :
            return True

def in_liste(liste, value,indice=False):
    """
    Check if value is in the list and return True or False
     ---using dichotomie methode---
    """
    start=0
    end=len(liste)-1

    while start<=end:
        m=(start+end)//2
        if liste[m]<value:
            start=m+1
        elif liste[m]>value:
            end=m-1
        else:
            if indice:
                return m
            return True
    return False
