import pygame
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.locals import *
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((1280, 720))
GAME_FONT = pygame.freetype.Font(None, 50)

def menu_titre():
	GAME_FONT.render_to(screen, (1280 / 2.6, 10), "SuperBomb", (0, 255, 0))
	
	