#Import les librairies nécéssaires
import pygame
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.locals import *
import pygame.freetype
from datetime import datetime, timedelta
import time
import main
#from multijoueur import winner
#from multijoueur import fenetre

###### Def des variables
pix_lar = 1250
pix_long = 750
'''
run = True
clock = pygame.time.Clock()
'''


#Initialisation de la fenêtre graphique
pygame.init()
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


GAME_FONT_victory = pygame.freetype.Font('assets/MilkyNice-Clean.ttf', 50)




def victoire(screen, winner, pix_lar, pix_long):
	screen = pygame.display.set_mode((pix_lar, pix_long))
	screen.fill((80 ,80 , 80))
	pygame.display.set_caption("Super Bomb")
	pygame.display.set_icon(pygame.image.load("icon.ico"))
	GAME_FONT_victory.render_to(screen, (pix_lar * 0.25, pix_long * 0.4), "Le gagnant de la partie est : ", (255, 255,255), size = 40)
	GAME_FONT_victory.render_to(screen, (pix_lar * 0.40, pix_long * 0.5), winner, (255, 255, 255), size = 40)
	pygame.display.flip()
	time.sleep(4)
	pygame.display.quit()
	pygame.quit()
	main.boucle_main()
	#exec(open("main.py").read())




'''
#Limite de FPS
clock.tick(60)
pygame.display.flip()
'''







'''
		def init_screen(pix_lar, pix_long):
			screen = pygame.display.set_mode((pix_lar, pix_long))
			screen.fill((80 ,80 , 80))
			return(screen)


		#Définition du titre de la fenêtre
		pygame.display.set_caption("Super Bomb")





		screen = init_screen(pix_lar, pix_long)


###########################################################################


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

'''