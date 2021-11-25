#Import les librairies nécéssaires
import pygame
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.locals import *
import pygame.freetype
from datetime import datetime, timedelta


###### Def des variables
pix_lar = 1280
pix_long = 720
run = True
clock = pygame.time.Clock()

#Initialisation de la fenêtre graphique
pygame.init()
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
def init_screen(pix_lar, pix_long):
	screen = pygame.display.set_mode((pix_lar, pix_long))
	screen.fill((80 ,80 , 80))
	GAME_FONT_victory = pygame.freetype.Font('assets/Spongy.otf', 50)
	return(screen)


#Définition du titre de la fenêtre
pygame.display.set_caption("Super Bomb")



while run:

	screen = init_screen(pix_lar, pix_long)

	for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					run = False
			
			if event.type == QUIT:
				run = False
			
			#Détection click souris pour le menu
			mousePos = pygame.mouse.get_pos()
			if mousePos[0] > 533 and mousePos[0] < 708 and mousePos[1] > 644 and mousePos[1] < 679 :
				pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
				if event.type == MOUSEBUTTONDOWN:
					print("mdr")
			else:
				pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


			#Limite de FPS
			clock.tick(60)
			pygame.display.flip()