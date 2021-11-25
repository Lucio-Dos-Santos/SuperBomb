import pygame
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.locals import *
import pygame.freetype


def menu_titre(screen, GAME_FONT, lar):
	GAME_FONT.render_to(screen, (lar * 0.5 - 270, 45), "Super Bomb", (245, 118, 39), size = 70)

def menu_solo(screen, GAME_FONT, lar, long):
	GAME_FONT.render_to(screen, (lar * 0.5 - 135, long * 0.25), "/!\Solo/!\ ", (218, 22, 22), size = 35)

def menu_multi_loc(screen, GAME_FONT, lar, long):
	GAME_FONT.render_to(screen, (lar * 0.375, long * 0.35), "Multijoueur", (218, 22, 22), size = 35)

def menu_multi_net(screen, GAME_FONT, lar, long):
	GAME_FONT.render_to(screen, (lar * 0.5 - 270, 45), "Multijoueur / Réseau", (218, 22, 22), size = 35)

def menu_quit(screen, GAME_FONT, lar, long):
	GAME_FONT.render_to(screen, (lar * 0.5 - 100, long - 75), "Quitter", (218, 22, 22), size = 32)
