import pygame
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.locals import *
import pygame.freetype


def menu_titre(screen, GAME_FONT, lar, long):
	GAME_FONT.render_to(screen, (lar * 0.5 - 270, 45), "Super Bomb", (180, 255, 0), size = 70)
	