#Import les librairies nécéssaires
import pygame
from pygame import mouse
from pygame import event
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.locals import *
import pygame.freetype

import main

pygame.freetype.init()

GAME_FONT_stats = pygame.freetype.Font('assets/Spongy.otf', 16)

def button_quit(screen, lar, long):
	GAME_FONT_stats.render_to(screen, (lar * 0.45, long - 38), "Quitter", (255,255,255), size = 25)

def click_quit():
	for event in pygame.event.get():
		mousePos = pygame.mouse.get_pos()
		if mousePos[0] > 559 and mousePos[0] < 674 and mousePos[1] > 711 and mousePos[1] < 739:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
			if event.type == MOUSEBUTTONDOWN:
				main.boucle_main()

		else:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
	