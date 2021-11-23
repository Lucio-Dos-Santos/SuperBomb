import pygame
from pygame.locals import *


def fenetre_jeu():
    
    pygame.init()

#Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((1280, 720))

#Chargement et collage du fond
    fond = pygame.image.load("assets/fond.jpg").convert()
    fenetre.blit(fond,(110,20))


#Chargement et collage du personnage
    perso = pygame.image.load("assets/perso.png").convert_alpha()
    perso.set_colorkey((255,255,255))
    position_perso = [240,100]
    size = perso.get_size()[0]

#bord du cadre de jeu
    i = 0
    x = 30
    while i<5:
        x = x+80
        bloc = pygame.image.load("assets/bloc.jpg").convert_alpha()
        fenetre.blit(bloc, (x,20))
        i += 1

    i = 0
    x = 670
    while i<5:
        x = x+80
        bloc = pygame.image.load("assets/bloc.jpg").convert_alpha()
        fenetre.blit(bloc, (x,20))
        i += 1

    i = 0
    y = 20
    while i<7:
        y = y + 80
        bloc = pygame.image.load("assets/bloc.jpg").convert_alpha()
        fenetre.blit(bloc, (1070,y))
        i += 1
    
    i = 0
    y = 20
    while i<7:
        y = y + 80
        bloc = pygame.image.load("assets/bloc.jpg").convert_alpha()
        fenetre.blit(bloc, (110,y))
        i += 1

    i = 0
    x = 110
    while i<11:
        x = x+80
        bloc = pygame.image.load("assets/bloc.jpg").convert_alpha()
        fenetre.blit(bloc, (x,580))
        i += 1

    #bloc
    i = 0
    x = 50
    while i<4:
        x = x + 200
        bloc = pygame.image.load("assets/bloc_bleu.jpg").convert_alpha()
        fenetre.blit(bloc, (x,150))
        i += 1
    
    i = 0
    x = 150
    while i<4:
        x = x + 200
        bloc = pygame.image.load("assets/bloc_marron.jpg").convert_alpha()
        fenetre.blit(bloc, (x,150))
        i += 1
    
    i = 0
    x = 50
    while i<4:
        x = x + 200
        bloc = pygame.image.load("assets/bloc_marron.jpg").convert_alpha()
        fenetre.blit(bloc, (x,260))
        i += 1
    
    i = 0
    x = 150
    while i<4:
        x = x + 200
        bloc = pygame.image.load("assets/bloc_bleu.jpg").convert_alpha()
        fenetre.blit(bloc, (x,260))
        i += 1
    
    i = 0
    x = 50
    while i<4:
        x = x + 200
        bloc = pygame.image.load("assets/bloc_bleu.jpg").convert_alpha()
        fenetre.blit(bloc, (x,370))
        i += 1
    
    i = 0
    x = 150
    while i<4:
        x = x + 200
        bloc = pygame.image.load("assets/bloc_marron.jpg").convert_alpha()
        fenetre.blit(bloc, (x,370))
        i += 1
    
    i = 0
    x = 50
    while i<4:
        x = x + 200
        bloc = pygame.image.load("assets/bloc_marron.jpg").convert_alpha()
        fenetre.blit(bloc, (x,480))
        i += 1
    
    i = 0
    x = 150
    while i<4:
        x = x + 200
        bloc = pygame.image.load("assets/bloc_bleu.jpg").convert_alpha()
        fenetre.blit(bloc, (x,480))
        i += 1
    
#Rafraîchissement de l'écran
    pygame.display.flip()

#BOUCLE INFINIE
    pygame.key.set_repeat(400, 30)
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:	#Si "flèche escape"
                    continuer = 0
                if event.type == QUIT:
                    continuer = 0
                if event.key == K_DOWN:	#Si "flèche bas"
                #On descend le perso
                    position_perso[-1] += size
                
                if event.key == K_LEFT:	#Si "flèche gauche"
                    position_perso[-1] += size
                
                if event.key == K_RIGHT:	#Si "flèche droite"
                    position_perso[1] += size
                    
                if event.key == K_UP:	#Si "flèche haut"
                    position_perso[1] += size
    #Re-collage	
        pygame.display.flip()      
        fenetre.blit(perso,tuple(position_perso))
	#Rafraichissement
        pygame.display.flip()
        
fenetre_jeu()
pygame.quit()