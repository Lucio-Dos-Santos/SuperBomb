import pygame
from pygame.locals import *
pygame.init()
taille_fenetre = (1250, 750)
fenetre_rect = pygame.Rect((0, 0), taille_fenetre)
screen_surface = pygame.display.set_mode(taille_fenetre)
 
BLEU_NUIT = (  5,   5,  30)
GRIS     = (  180, 182,   181)
JAUNE     = (255, 255,   0)

timer = pygame.time.Clock()
 
joueur = pygame.Surface((50, 50))
joueur.fill(JAUNE)
# Position du joueur
x, y = 25, 100
# Vitesse du joueur
vx, vy = 0, 0
# Gravité vers le bas donc positive
GRAVITE = 2
mur = pygame.Surface((50, 50))
mur.fill(GRIS)
 
niveau = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

def dessiner_niveau(surface, niveau):
    """Dessine le niveau sur la surface donnée.
 
    Utilise la surface `mur` pour dessiner les cases de valeur 1
    """
    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                surface.blit(mur, (i*50, j*50))
                
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type== KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = 0
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                vy = -20
    screen_surface.fill(BLEU_NUIT)
    dessiner_niveau(screen_surface, niveau)
    screen_surface.blit(joueur, (x, y))
    pygame.display.flip()
 
pygame.quit()

