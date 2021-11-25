#Import les librairies nécéssaires
import pygame
from pygame import mouse
from pygame import event
from pygame.constants import FULLSCREEN, RESIZABLE
from pygame.locals import *
import pygame.freetype
import time

pygame.freetype.init()

GAME_FONT_stats = pygame.freetype.Font('assets/MilkyNice-Clean.ttf', 16)

def button_quit(screen, lar, long):
	GAME_FONT_stats.render_to(screen, (lar * 0.75, long - 50), "Quitter", (255,255,255), size = 30)

def player1(screen, lar, long):
	GAME_FONT_stats.render_to(screen, (lar * 0.75, long * 0.1), "Joueur 1", (255, 213, 45), size = 35)

def moves_p1(screen, lar, long):
	GAME_FONT_stats.render_to(screen, (lar * 0.65, long * 0.15), "Poser la bombe - ESPACE", (23, 255, 10), size = 25)
	GAME_FONT_stats.render_to(screen, (lar * 0.65, long * 0.2), "Haut - FLECHE HAUT", (23, 255, 10), size = 25)
	GAME_FONT_stats.render_to(screen, (lar * 0.65, long * 0.25), "Bas - FLECHE BAS", (23, 255, 10), size = 25)
	GAME_FONT_stats.render_to(screen, (lar * 0.65, long * 0.3), "Droite - FLECHE DROITE", (23, 255, 10), size = 25)
	GAME_FONT_stats.render_to(screen, (lar * 0.65, long * 0.35), "Gauche - FLECHE GAUCHE", (23, 255, 10), size = 25)

def player2(screen, lar, long):
	GAME_FONT_stats.render_to(screen, (lar * 0.75, long * 0.45), "Joueur 2", (255, 41, 0), size = 35)

def moves_p2(screen, lar, long):
	GAME_FONT_stats.render_to(screen, (lar * 0.65, long * 0.5), "Poser la bombe - E", (23, 255, 10), size = 25)
	GAME_FONT_stats.render_to(screen, (lar * 0.65, long * 0.55), "Haut - Z", (23, 255, 10), size = 25)
	GAME_FONT_stats.render_to(screen, (lar * 0.65, long * 0.6), "Reculer - S", (23, 255, 10), size = 25)
	GAME_FONT_stats.render_to(screen, (lar * 0.65, long * 0.65), "Bas - D", (23, 255, 10), size = 25)
	GAME_FONT_stats.render_to(screen, (lar * 0.65, long * 0.7), "Gauche - Q", (23, 255, 10), size = 25)