#Import les librairies nécéssaires
import pygame
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.locals import *
import pygame.freetype

#Import les sous programmes
import menu

#Réglage de la résolution de la fenêtre
pix_lar = 1280
pix_long = 720

#Définitions de certaines variables
run = True
clock = pygame.time.Clock()

#Initialisation de la fenêtre graphique
pygame.init()
screen = pygame.display.set_mode((pix_lar, pix_long))
screen.fill((19 ,80 , 13))

#Définition de la police d'écriture
GAME_FONT = pygame.freetype.Font('assets/BD_Cartoon_Shout.ttf', 16)


#Boucle néccéssaire pour le bon fonctionnement de la partie graphique
while run:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				run = False
		
		if event.type == QUIT:
			run = False
	
	#Détection click souris pour le menu
	mousePos = pygame.mouse.get_pos()
	if event.type == MOUSEBUTTONDOWN:
		if mousePos[0] > 533 and mousePos[0] < 708 and mousePos[1] > 644 and mousePos[1] < 679 :
			run = False
		if mousePos[0] > 500 and mousePos[0] < 757 and mousePos[1] > 177 and mousePos[1] < 220 : 
			print("Mode Solo")
		if mousePos[0] > 476 and mousePos[0] < 774 and mousePos[1] > 249 and mousePos[1] < 288 : 
			print("Mode multijoueur")
		

	#Récupère les infos de la fenêtre (La résolution)
	ecran = pygame.display.Info()

	#Affichage du menu
	menu.menu_titre(screen, GAME_FONT, ecran.current_w)
	menu.menu_solo(screen, GAME_FONT, ecran.current_w, ecran.current_h)
	menu.menu_multi_loc(screen, GAME_FONT, ecran.current_w, ecran.current_h)
	menu.menu_quit(screen, GAME_FONT, ecran.current_w, ecran.current_h)
	
	#Limite de FPS
	clock.tick(60)
	pygame.display.flip()
