import pygame
from pygame.locals import *
from new_constant import *
from datetime import datetime, timedelta


class Niveau:
    """class de l'ffichage du terrain"""
    def __init__(self, fichier):
        """initialisation des variables de la class"""
        self.fichier = fichier
        self.structure = [[]]

    def generer(self):
        """lecture du fichier du niveau"""
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                    if sprite != "\n":
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau

    def afficher(self, fenetre):
        """définition des images du niveau"""
        brick = pygame.image.load(image_brick)
        pillar = pygame.image.load(image_pillier)
        sol = pygame.image.load(image_sol)
        box = pygame.image.load(image_box)
        num_ligne = 0
        # parcours de la double liste du terrain
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite

                if sprite == "p":
                    fenetre.blit(pillar, (x, y))
                elif sprite == "s":
                    fenetre.blit(sol, (x, y))
                elif sprite == "b":
                    fenetre.blit(brick, (x, y))
                elif sprite == 'a':
                    fenetre.blit(box,(x,y))
                num_case += 1
            num_ligne += 1

    def detruire(self, case_x, case_y):
        """destruction d'un bloc du terrain"""
        self.structure[int(case_x)][int(case_y)] = "s"


class Perso:
    """Classe permettant de créer un personage"""

    def __init__(self, droite, gauche, haut, bas, niveau):
        # initialisation des images et gestion de la transparance
        self.droite = pygame.image.load(p1_droite).convert()
        self.droite.set_colorkey((255, 255, 255))
        self.gauche = pygame.image.load(p1_gauche).convert()
        self.gauche.set_colorkey((255, 255, 255))
        self.haut = pygame.image.load(p1_haut).convert()
        self.haut.set_colorkey((255, 255, 255))
        self.bas = pygame.image.load(p1_bas).convert()
        self.bas.set_colorkey((255, 255, 255))
        # position de base du perso
        self.case_x = 1
        self.case_y = 1
        self.x = taille_sprite * self.case_x
        self.y = taille_sprite * self.case_y

        self.direction = self.droite
        self.niveau = niveau

    def deplacer(self, direction):
        """Methode de déplacement du personnage"""

        if direction == "droite":
            # dépassement de l'écran ?
            if self.case_x < (nombre_sprite_cote - 1):
                # destination le sol ?
                if self.niveau.structure[self.case_y][self.case_x + 1] == "s":
                    # déplacement d"une case
                    self.case_x += 1
                    # calcul de la position en px
                    self.x = self.case_x * taille_sprite
            # image de la direction (a simplifier avec pygame.image.rotate())
            self.direction = self.droite

        if direction == "gauche":
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x - 1] == "s":
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite
            self.direction = self.gauche

        if direction == "haut":
            if self.case_y > 0:
                if self.niveau.structure[self.case_y - 1][self.case_x] == "s":
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.haut

        if direction == "bas":
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y + 1][self.case_x] == "s":
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.bas


class Perso2:
    """Classe permettant de créer le second perso à simplifier pour en utiliser qu'une"""

    def __init__(self, droite, gauche, haut, bas, niveau):
        # initialisation des images et gestion de la transparance
        self.droite = pygame.image.load(droite).convert()
        self.droite.set_colorkey((255, 255, 255))
        self.gauche = pygame.image.load(gauche).convert()
        self.gauche.set_colorkey((255, 255, 255))
        self.haut = pygame.image.load(haut).convert()
        self.haut.set_colorkey((255, 255, 255))
        self.bas = pygame.image.load(bas).convert()
        self.bas.set_colorkey((255, 255, 255))
        # position de base
        self.case_x = 13
        self.case_y = 13
        self.x = taille_sprite * self.case_x
        self.y = taille_sprite * self.case_y
        self.direction = self.haut
        self.niveau = niveau

    def deplacer(self, direction):
        """Methode de déplacement du personnage"""

        if direction == "droite":
            # dépassement de l'écran ?
            if self.case_x < (nombre_sprite_cote - 1):
                # destination le sol ?
                if self.niveau.structure[self.case_y][self.case_x + 1] == "s":
                    # déplacement d"une case
                    self.case_x += 1
                    # calcul de la position en px
                    self.x = self.case_x * taille_sprite
            # image dans la bonne direction
            self.direction = self.droite

        if direction == "gauche":
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x - 1] == "s":
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite
            self.direction = self.gauche

        if direction == "haut":
            if self.case_y > 0:
                if self.niveau.structure[self.case_y - 1][self.case_x] == "s":
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.haut

        if direction == "bas":
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y + 1][self.case_x] == "s":
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.bas


class Bomb:
    """Classe controllant la bombe"""

    def __init__(self, bomb, niveau, perso1, perso2):
        # chargement des sprites
        self.bomb = pygame.image.load(bomb).convert()
        # place la bombe a une position non visible par default
        self.x = 1300
        self.y = 800
        self.case_x = 500
        self.case_y = 500
        self._time_created = datetime.now()
        # déclaration des variables de la classe
        self.niveau = niveau
        self.perso1 = perso1
        self.perso2 = perso2
        self.explosion = 0

    def poser(self, x, y, bomb):
        """pose et arme la bombe"""
        self.bomb = pygame.image.load(bomb).convert()
        self.bomb.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.case_x = int(x / taille_sprite)
        self.case_y = int(y / taille_sprite)
        self._time_created = datetime.now()
        self.explosion = 0

    def exploser(self):
        """Explosion de la bombe"""

        # condition explosion de la bombe 3 seconde apres
        if timedelta(seconds=3) <= datetime.now() - self._time_created:
            # change le sprite de la bombe en sprite d'explosion
            self.bomb = pygame.image.load(image_explosion).convert()
            self.bomb.set_colorkey((255, 255, 255))
            self.explosion = 1

            # try / except vrmt hard codé à supprimer
            try:
                # destruction des briques de tous les cotes
                # mettre la condition dans niveau.detruire() pour simplifier
                if self.niveau.structure[self.case_y][self.case_x + 1] == "a":
                    self.niveau.detruire(self.case_y, self.case_x + 1)

                if self.niveau.structure[self.case_y][self.case_x - 1] == "a":
                    self.niveau.detruire(self.case_y, self.case_x - 1)

                if self.niveau.structure[self.case_y - 1][self.case_x] == "a":
                    self.niveau.detruire(self.case_y - 1, self.case_x)

                if self.niveau.structure[self.case_y + 1][self.case_x] == "a":
                    self.niveau.detruire(self.case_y + 1, self.case_x)

                # conditions de victoire (a simplifier)
                if self.case_x == self.perso1.case_x and self.case_y - 1 <= self.perso1.case_y <= self.case_y + 1:
                    return 1
                elif self.case_x - 1 <= self.perso1.case_x <= self.case_x + 1 and self.case_y == self.perso1.case_y:
                    return 1

                if self.case_x == self.perso2.case_x and self.case_y - 1 <= self.perso2.case_y <= self.case_y + 1:
                    return 1
                elif self.case_x - 1 <= self.perso2.case_x <= self.case_x + 1 and self.case_y == self.perso2.case_y:
                    return 1

            except IndexError:
                # au cas ou la bombe est / detruit un bloc en dehors du terrain
                pass

        if timedelta(milliseconds=3500) <= datetime.now() - self._time_created:
            # place la bombe a une position non visible apres l'explosion
            self.x = 640
            self.y = 640
            self.case_x = 255
            self.case_y = 255
            self.explosion = 0


class Bomb2:
    """Classe controllant la bombe du perso2"""

    def __init__(self, bomb, niveau, perso1, perso2):
        # chargement des sprites
        self.bomb = pygame.image.load(bomb).convert()
        # place la bombe a une position non visible par default
        self.x = 640
        self.y = 640
        self.case_x = 255
        self.case_y = 255
        self._time_created = datetime.now()
        # déclaration des variables de la classe
        self.niveau = niveau
        self.perso1 = perso1
        self.perso2 = perso2
        self.explosion = 0

    def poser(self, x, y, bomb):
        """pose et arme la bombe"""
        self.bomb = pygame.image.load(bomb).convert()
        self.bomb.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.case_x = int(x / taille_sprite)
        self.case_y = int(y / taille_sprite)
        self._time_created = datetime.now()
        self.explosion = 0

    def exploser(self):
        """Explosion de la bombe"""

        if timedelta(seconds=3) <= datetime.now() - self._time_created:
            self.bomb = pygame.image.load(image_explosion).convert()
            self.bomb.set_colorkey((255, 255, 255))
            self.explosion = 1

            # try / except vrmt hard codé à supprimer
            try:
                # destruction des briques de tous les cotes
                if self.niveau.structure[self.case_y][self.case_x + 1] == "b":
                    self.niveau.detruire(self.case_y, self.case_x + 1)

                if self.niveau.structure[self.case_y][self.case_x - 1] == "b":
                    self.niveau.detruire(self.case_y, self.case_x - 1)

                if self.niveau.structure[self.case_y - 1][self.case_x] == "b":
                    self.niveau.detruire(self.case_y - 1, self.case_x)

                if self.niveau.structure[self.case_y + 1][self.case_x] == "b":
                    self.niveau.detruire(self.case_y + 1, self.case_x)

                # conditions de victoire (a simplifier)
                if self.case_x == self.perso1.case_x and self.case_y - 1 <= self.perso1.case_y <= self.case_y + 1:
                    return 1
                elif self.case_x - 1 <= self.perso1.case_x <= self.case_x + 1 and self.case_y == self.perso1.case_y:
                    return 1

                if self.case_x == self.perso2.case_x and self.case_y - 1 <= self.perso2.case_y <= self.case_y + 1:
                    return 1
                elif self.case_x - 1 <= self.perso2.case_x <= self.case_x + 1 and self.case_y == self.perso2.case_y:
                    return 1
            except IndexError:
                pass

        if timedelta(milliseconds=3500) <= datetime.now() - self._time_created:
            # place la bombe a une position non visible
            self.x = 640
            self.y = 640
            self.case_x = 255
            self.case_y = 255
            self.explosion = 0


class Flammes:
    def __init__(self, fflamme_d, fflamme_g, fflamme_h, fflamme_b):
        # chargement des sprites de flammes
        self.fflamme_d = pygame.image.load(fflamme_d).convert()
        self.fflamme_d.set_colorkey((255, 255, 255))
        self.fflamme_g = pygame.image.load(fflamme_g).convert()
        self.fflamme_g.set_colorkey((255, 255, 255))
        self.fflamme_h = pygame.image.load(fflamme_h).convert()
        self.fflamme_h.set_colorkey((255, 255, 255))
        self.fflamme_b = pygame.image.load(fflamme_b).convert()
        self.fflamme_b.set_colorkey((255, 255, 255))
