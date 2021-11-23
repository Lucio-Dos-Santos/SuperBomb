import pygame
from pygame.locals import *
from fenetre1 import fenetre_jeu

class Player:
    joueur = pygame.image.load("assets/perso.png")
    def __init__(self):
        self.x = 0
        self.y = 0
        
        