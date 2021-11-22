import pygame
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.locals import *
import pygame.freetype
import menu

pix_lar = 1280
pix_long = 720

run = True
pygame.init()
screen = pygame.display.set_mode((pix_lar, pix_long))

GAME_FONT = pygame.freetype.Font(None, 50)

while run:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				run = False
		
		if event.type == QUIT:
			run = False
	
	menu.menu_titre()
	
	
	
	pygame.display.flip()
