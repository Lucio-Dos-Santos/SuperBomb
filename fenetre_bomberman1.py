import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1280, 720))

#Chargement et collage du fond
fond = pygame.image.load("assets/fond.jpg").convert()
fenetre.blit(fond,(140,150))


#Chargement et collage du personnage
perso = pygame.image.load("assets/perso.png").convert_alpha()
perso.set_colorkey((255,255,255))
position_perso = perso.get_rect()
fenetre.blit(perso,(480,480),position_perso)

#bord du cadre de jeu
i = 0
x = 280
while i<5:
    x = x+80
    bloc = pygame.image.load("assets/bloc_gris.jpg").convert_alpha()
    fenetre.blit(bloc, (x,150))
    i += 1

i = 0
x = 1080
while i<5:
    x = x+80
    bloc = pygame.image.load("assets/bloc_gris.jpg").convert_alpha()
    fenetre.blit(bloc, (x,150))
    i += 1

i = 0
y = 150
while i<12:
    y = y + 80
    bloc = pygame.image.load("assets/bloc_gris.jpg").convert_alpha()
    fenetre.blit(bloc, (1480,y))
    i += 1
    
i = 0
y = 150
while i<12:
    y = y + 80
    bloc = pygame.image.load("assets/bloc_gris.jpg").convert_alpha()
    fenetre.blit(bloc, (360,y))
    i += 1

i = 0
x = 360
while i<13:
    x = x+80
    bloc = pygame.image.load("assets/bloc_gris.jpg").convert_alpha()
    fenetre.blit(bloc, (x,1110))
    i += 1

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:	#Si "flèche escape"
                continuer = 0
            if event.key == K_DOWN:	#Si "flèche bas"
                #On descend le perso
                position_perso = position_perso.move(0,-3)
                
            if event.key == K_LEFT:	#Si "flèche gauche"
                position_perso = position_perso.move(3,0)
                
            if event.key == K_RIGHT:	#Si "flèche droite"
                
                position_perso = position_perso.move(-3,0)
            if event.key == K_UP:	#Si "flèche haut"
                
                position_perso = position_perso.move(0,3)
    #Re-collage	
    fenetre.blit(perso, (480,480),position_perso)
	#Rafraichissement
    pygame.display.flip()
