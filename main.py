#Import les librairies nécéssaires
import pygame
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.locals import *
import pygame.freetype
from datetime import datetime, timedelta

#Import les sous programmes
import menu
import stats
import main

#Initialisation de la fenêtre graphique
pygame.init()
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
def init_screen(pix_lar, pix_long):
	screen = pygame.display.set_mode((pix_lar, pix_long))
	screen.fill((80 ,80 , 80))
	return(screen)

#Définition de la police d'écriture
def font_menu():
	GAME_FONT_menu = pygame.freetype.Font('assets/BD_Cartoon_Shout.ttf', 16)
	return(GAME_FONT_menu)

def font_stats():
	GAME_FONT_stats = pygame.freetype.Font('assets/Spongy.otf', 16)
	return(GAME_FONT_stats)

GAME_FONT_menu = font_menu()
GAME_FONT_stats = font_stats()

def boucle_main():
	#Réglage de la résolution de la fenêtre
	pix_lar = 1280
	pix_long = 720

	screen = init_screen(pix_lar, pix_long)

	#Définitions de certaines variables
	run = True
	clock = pygame.time.Clock()

	#Définition du titre de la fenêtre
	pygame.display.set_caption("Super Bomb")

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
		if mousePos[0] > 533 and mousePos[0] < 708 and mousePos[1] > 644 and mousePos[1] < 679 :
			#pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
			if event.type == MOUSEBUTTONDOWN:
				pygame.display.quit()
				pygame.quit()
				quit()
			
		'''if mousePos[0] > 500 and mousePos[0] < 757 and mousePos[1] > 177 and mousePos[1] < 220 : 
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
			if event.type == MOUSEBUTTONDOWN:
				print("Mode Solo")
		'''
		
		if mousePos[0] > 476 and mousePos[0] < 774 and mousePos[1] > 249 and mousePos[1] < 288 : 
			#pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
			if event.type == MOUSEBUTTONDOWN:
				pygame.display.quit()
				exec(open("new_main.py").read())
				run = False
				break

		if not mousePos[0] > 533 and mousePos[0] < 708 and mousePos[1] > 644 and mousePos[1] < 679 :
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
		
		if not mousePos[0] > 476 and mousePos[0] < 774 and mousePos[1] > 249 and mousePos[1] < 288 :
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

		#Récupère les infos de la fenêtre (La résolution)
		ecran = pygame.display.Info()

		#Affichage du menu
		menu.menu_titre(screen, GAME_FONT_menu, ecran.current_w)
		menu.menu_solo(screen, GAME_FONT_menu, ecran.current_w, ecran.current_h)
		menu.menu_multi_loc(screen, GAME_FONT_menu, ecran.current_w, ecran.current_h)
		menu.menu_quit(screen, GAME_FONT_menu, ecran.current_w, ecran.current_h)
		
		#Limite de FPS
		clock.tick(60)
		pygame.display.flip()

boucle_main()


#################################################### TRUC DE BLEDAR
'''
#Réglage de la résolution de la fenêtre
pix_lar = 1280
pix_long = 720

screen = init_screen(pix_lar, pix_long)

#Définitions de certaines variables
run = True
clock = pygame.time.Clock()

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
	if mousePos[0] > 533 and mousePos[0] < 708 and mousePos[1] > 644 and mousePos[1] < 679 :
		#pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
		if event.type == MOUSEBUTTONDOWN:
			run = False
		
	if mousePos[0] > 500 and mousePos[0] < 757 and mousePos[1] > 177 and mousePos[1] < 220 : 
		pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
		if event.type == MOUSEBUTTONDOWN:
			print("Mode Solo")
	

	if mousePos[0] > 476 and mousePos[0] < 774 and mousePos[1] > 249 and mousePos[1] < 288 : 
		#pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
		if event.type == MOUSEBUTTONDOWN:
			pygame.quit()

	if not mousePos[0] > 533 and mousePos[0] < 708 and mousePos[1] > 644 and mousePos[1] < 679 :
		pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

	if not mousePos[0] > 476 and mousePos[0] < 774 and mousePos[1] > 249 and mousePos[1] < 288 :
		pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

	#Récupère les infos de la fenêtre (La résolution)
	ecran = pygame.display.Info()

	#Affichage du menu
	menu.menu_titre(screen, GAME_FONT_menu, ecran.current_w)
	menu.menu_solo(screen, GAME_FONT_menu, ecran.current_w, ecran.current_h)
	menu.menu_multi_loc(screen, GAME_FONT_menu, ecran.current_w, ecran.current_h)
	menu.menu_quit(screen, GAME_FONT_menu, ecran.current_w, ecran.current_h)

	#Limite de FPS
	clock.tick(60)
	pygame.display.flip()

'''