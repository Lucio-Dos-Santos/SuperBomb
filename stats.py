#Import les librairies nécéssaires
import pygame
from pygame import mouse
from pygame import event
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.locals import *
import pygame.freetype

pygame.freetype.init()

GAME_FONT_stats = pygame.freetype.Font('assets/Spongy.otf', 16)

def button_quit(screen, lar, long):
	GAME_FONT_stats.render_to(screen, (lar * 0.45, long - 38), "Quitter", (255,255,255), size = 25)
