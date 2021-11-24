import pygame
from pygame.locals import *
from datetime import datetime, timedelta
import stats

pygame.init()

taille_fenetre = (1250, 750)
fenetre_rect = pygame.Rect((0, 0), taille_fenetre)
screen_surface = pygame.display.set_mode(taille_fenetre)
BLEU_NUIT = (  5,   5,  30)
GRIS     = (  80, 80,   80)
MARRON = (152, 75, 0)
timer = pygame.time.Clock()

joueur = pygame.image.load("assets/Pacman_d.png").convert_alpha()
    # Position du joueur
x, y = 100, 150

    # Vitesse du joueur
vx, vy = 0, 0
    # Gravité vers le bas donc positive

mur = pygame.image.load("assets/mur.jpg").convert_alpha()
bloc = pygame.image.load("assets/brique.png").convert_alpha()
box = pygame.image.load("assets/bloc.png").convert_alpha()

niveau = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,0],
    [0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0],
    [0, 1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1,0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0],
    [0, 1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1,0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0],
    [0, 1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1,0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0],
    [0, 1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1,0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    ]

  

class Bombe: 
    def init(self,bomb, joueur):
        """chargement des sprites"""
        self.bomb = pygame.image.load("assets/bomb.png").convert()
        """place la bombe a une position non visible par default"""
        self.x = 1300
        self.y = 800
        self.case_x = 255
        self.case_y = 255
        self.timer = datetime.now()
        self.niveau = niveau
        joueur = joueur
        self.explosion = 0
    

        
    def poser(self, x, y, bomb):
        """pose et arme la bombe"""
        self.bomb = pygame.image.load("assets/bomb").convert()
        self.bomb.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.case_x = int(x / 50)
        self.case_y = int(y / 50)
        self.timer = datetime.now()
        self.explosion = 0
        

    def exploser(self):
        
        """Explosion de la bombe"""
        image_explosion = pygame.image.load("assets/explodstart.png").convert_alpha()
        """condition explosion de la bombe 3 seconde apres"""
        if timedelta(seconds=3) <= datetime.now() - timer:
            """ change le sprite de la bombe en sprite d'explosion"""
            self.bomb = pygame.image.load(image_explosion).convert()
            self.bomb.set_colorkey((255, 255, 255))
            self.explosion = 1

            '''try:
                """ destruction des briques de tous les cotes"""
                """ mettre la condition dans niveau.detruire() pour simplifier"""
                if self.niveau[self.case_y][self.case_x+1] == 3:
                    self.niveau.detruire(self.case_y, self.case_x + 1)

                if self.niveau[from_coord_to_grid.case_y][from_coord_to_grid.case_x - 1] == 3:
                    niveau(from_coord_to_grid.case_y, from_coord_to_grid.case_x - 1)

                if self.niveau[from_coord_to_grid.case_y - 1][from_coord_to_grid.case_x] == 3:
                    niveau(from_coord_to_grid.case_y - 1, from_coord_to_grid.case_x)

                if self.niveau[from_coord_to_grid.case_y + 1][from_coord_to_grid.case_x] == 3:
                    niveau(from_coord_to_grid.case_y + 1, from_coord_to_grid.case_x)

            except IndexError:
                """ au cas ou la bombe est / detruit un bloc en dehors du terrain"""
                pass'''

        if timedelta(milliseconds=3500) <= datetime.now() - self.timer:
            """place la bombe a une position non visible apres l'explosion"""
            self.x = 640
            self.y = 640
            self.case_x = 255
            self.case_y = 255
            self.explosion = 0

class flamme:
    
    def __init__(self, fflamme_d, fflamme_g, fflamme_h, fflamme_b):
        """ chargement des sprites de flammes"""
        self.fflamme_d = pygame.image.load("assets/fflamme_d").convert()
        self.fflamme_d.set_colorkey((255, 255, 255))
        self.fflamme_g = pygame.image.load("assets/fflamme_g").convert()
        self.fflamme_g.set_colorkey((255, 255, 255))
        self.fflamme_h = pygame.image.load("assets/fflamme_h").convert()
        self.fflamme_h.set_colorkey((255, 255, 255))
        self.fflamme_b = pygame.image.load("assets/fflamme_b").convert()
        self.fflamme_b.set_colorkey((255, 255, 255))
        

def dessiner_niveau(surface, niveau):
    """Dessine le niveau sur la surface donnée.
    
    Utilise la surface `mur` pour dessiner les cases de valeur 1
    """
    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                screen_surface.blit(mur, (i*50, j*50))
            if case == 2:
                screen_surface.blit(bloc, (i*50, j*50))
            if case == 3:
                screen_surface.blit(box,(i*50, j*50))


def from_coord_to_grid(pos):
    """Retourne la position dans le niveau en indice (i, j)
    
        `pos` est un tuple contenant la position (x, y) du coin supérieur gauche.
        On limite i et j à être positif.
        """
    x, y = pos
    i = max(0, int(x // 50))
    j = max(0, int(y // 50))
    return i, j
                    
def get_neighbour_blocks(niveau, i_start, j_start):
    """Retourne la liste des rectangles autour de la position (i_start, j_start).
    
        Vu que le personnage est dans le carré (i_start, j_start), il ne peut
        entrer en collision qu'avec des blocks dans sa case, la case en-dessous,
        la case à droite ou celle en bas et à droite. On ne prend en compte que
        les cases du niveau avec une valeur de 1.
        """
    blocks = list()
    for j in range(j_start, j_start+2):
        for i in range(i_start, i_start+2):
            if niveau[j][i] == 1 :
                topleft = i*50, j*50
                blocks.append(pygame.Rect((topleft), (50, 50)))
            if niveau[j][i] == 2:
                topleft = i*50, j*50
                blocks.append(pygame.Rect((topleft), (50, 50)))
            if niveau[j][i] == 3:
                topleft = i*50, j*50
                blocks.append(pygame.Rect((topleft), (50, 50)))
    return blocks
    
def bloque_sur_collision(niveau, old_pos, new_pos, vx, vy):
    """Tente de déplacer old_pos vers new_pos dans le niveau.
    
        S'il y a collision avec les éléments du niveau, new_pos sera ajusté pour
        être adjacents aux éléments avec lesquels il entre en collision.
        On passe également en argument les vitesses `vx` et `vy`.
    
        La fonction retourne la position modifiée pour new_pos ainsi que les
        vitesses modifiées selon les éventuelles collisions.
        """
    old_rect = pygame.Rect(old_pos, (50, 50))
    new_rect = pygame.Rect(new_pos, (50, 50))
    i, j = from_coord_to_grid(new_pos)
    collide_later = list()
    blocks = get_neighbour_blocks(niveau, i, j)
    for block in blocks:
        if not new_rect.colliderect(block):
            continue
    
        dx_correction, dy_correction = compute_penetration(block, old_rect, new_rect)
            # Dans cette première phase, on n'ajuste que les pénétrations sur un
            # seul axe.
        if dx_correction == 0.0:
            new_rect.top += dy_correction
            vy = 0.0
        elif dy_correction == 0.0:
            new_rect.left += dx_correction
            vx = 0.0
        else:
            collide_later.append(block)
    
        # Deuxième phase. On teste à présent les distances de pénétrations pour
        # les blocks qui en possédaient sur les 2 axes.
    for block in collide_later:
        dx_correction, dy_correction = compute_penetration(block, old_rect, new_rect)
        if dx_correction == dy_correction == 0.0:
                # Finalement plus de pénétration. Le new_rect a bougé précédemment
                # lors d'une résolution de collision
            continue
        if abs(dx_correction) < abs(dy_correction):
                # Faire la correction que sur l'axe X (plus bas)
            dy_correction = 0.0
        elif abs(dy_correction) < abs(dx_correction):
                # Faire la correction que sur l'axe Y (plus bas)
            dx_correction = 0.0
        if dy_correction != 0.0:
            new_rect.top += dy_correction
            vy = 0.0
        elif dx_correction != 0.0:
            new_rect.left += dx_correction
            vx = 0.0
    
    x, y = new_rect.topleft
    return x, y, vx, vy
    
def compute_penetration(block, old_rect, new_rect):
    """Calcul la distance de pénétration du `new_rect` dans le `block` donné.
    
        `block`, `old_rect` et `new_rect` sont des pygame.Rect.
        Retourne les distances `dx_correction` et `dy_correction`.
        """
    dx_correction = dy_correction = 0.0
    if old_rect.bottom <= block.top < new_rect.bottom:
        dy_correction = block.top  - new_rect.bottom
    elif old_rect.top >= block.bottom > new_rect.top:
        dy_correction = block.bottom - new_rect.top
    if old_rect.right <= block.left < new_rect.right:
        dx_correction = block.left - new_rect.right
    elif old_rect.left >= block.right > new_rect.left:
        dx_correction = block.right - new_rect.left
    return dx_correction, dy_correction               
                    
continuer = True
while continuer:
    pygame.time.Clock().tick(60)
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type== KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = False
        if  event.type == KEYDOWN:
            if event.key == K_RIGHT:
                joueur = pygame.image.load("assets/Pacman_d.png").convert_alpha()
        if  event.type == KEYDOWN:
            if event.key == K_LEFT:
                joueur = pygame.image.load("assets/Pacman_g.png").convert_alpha()
        if  event.type == KEYDOWN:
            if event.key == K_UP:
                joueur = pygame.image.load("assets/Pacman_h.png").convert_alpha() 
        if  event.type == KEYDOWN:
            if event.key == K_DOWN:
                joueur = pygame.image.load("assets/Pacman_b.png").convert_alpha()    
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                image_bombe=pygame.image.load("assets/bomb").convert()
                Bombe.poser(joueur.x, joueur.y,image_bombe)
        if event.type == MOUSEBUTTONDOWN:
            if mousePos[0] > 559 and mousePos[0] < 674 and mousePos[1] > 711 and mousePos[1] < 739:
                stats.click_quit()

    '''if Bombe.explosion == 1:
        screen_surface.blit(flamme.fflamme_b, (bombe.x, bombe.y + 50))
        screen_surface.blit(flamme.fflamme_h, (poser.bomb.x, poser.bomb.y - 50))
        screen_surface.blit(flamme.fflamme_g, (poser.bomb.x - 50, poser.bomb.y))
        screen_surface.blit(flamme.fflamme_d, (poser.bomb.x + 50, poser.bomb.y))'''      
    
    #pygame.display.flip()
    
    keys_pressed = pygame.key.get_pressed()
        # Sauvegarde de l'ancienne position
    old_x, old_y = x, y
    vx = (keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) * 1.5
        
    vy = (keys_pressed[K_DOWN] - keys_pressed[K_UP]) * 1.5
    x += vx
    y += vy
    x, y, vx, vy = bloque_sur_collision(niveau, (old_x, old_y), (x, y), vx, vy)
                
    screen_surface.fill(GRIS)
    dessiner_niveau(screen_surface, niveau)
    screen_surface.blit(joueur, (x, y))

    ############################Luca
    stats.button_quit(screen_surface, taille_fenetre[0], taille_fenetre[1])
    
    
    ############################
    pygame.display.flip()

pygame.quit()

