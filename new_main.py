import pygame
from pygame.locals import *
from datetime import datetime, timedelta

from new_constant import *
from new_classes import *

###### SOUS PROGRAMMES
import time
import stats
import victory

winner = ""

__name__ = "bomberman luncher"


# initialisation de pygame
pygame.display.init()

# initialisation de la fenetre
screesize = (1250, 750)
fenetre = pygame.display.set_mode(screesize)
pygame.display.set_caption("Super Bomb")

# variable de debut/fin de la boucle infinie
continuer = 1

# boucle d'actualisation de la fenetre
while continuer:

    # chargement de l'accueil
    #accueil = pygame.image.load(image_accueil).convert()
    #fenetre.blit(accueil, (0, 0))

    # rafraichissement
    pygame.display.flip()

    continuer_jeu = 1
    continuer_accueil = 0
    choix = "n1"

    # boucle d'accueil
    while continuer_accueil:

        # limitation de vittesse de la boucle
        pygame.time.Clock().tick(60)

        choix = 0
        # evemements clavier du menu
        for event in pygame.event.get():
            # quitter le jeu
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
            # démarer la jeu
            elif event.type == KEYDOWN and event.key == K_SPACE:
                continuer_accueil = 0
                choix = "n1"

    # Vérification du choix du niveau pour ne pas charger si il quitte ;)
    if choix != 0:
        # chargement du fond
        # fond = pygame.image.load(image_fond).convert()

        # generation du niveau à partir du fichier
        niveau = Niveau("level1.txt")
        niveau.generer()
        niveau.afficher(fenetre)

        # création des deux avatars
        perso = Perso(p1_droite, p1_gauche, p1_haut, p1_bas, niveau)
        perso2 = Perso2(p2_droite, p2_gauche, p2_haut, p2_bas, niveau)
        # création des deux bombes
        bombe = Bomb(image_bombe, niveau, perso, perso2)
        bombe2 = Bomb(image_bombe, niveau, perso, perso2)
        # création des flammes
        flamme = Flammes(flamme_d, flamme_g, flamme_h, flamme_b)

    # boucle de jeu
    while continuer_jeu:

        ##############################LUCA
        mousePos = pygame.mouse.get_pos()
        ##############################

        # debugfps = datetime.now()

        # limitation de la vitesse de la boucle infinie
        pygame.time.Clock().tick(30)
        # print(pygame.time.get_ticks())

        # boucle des evenements de pygame
        for event in pygame.event.get():

            ################################## LUCA
            if event.type == MOUSEBUTTONDOWN:
                if mousePos[0] > 932 and mousePos[0] < 1051 and mousePos[1] > 699 and mousePos[1] < 727:
                    continuer_jeu = 0
                    pygame.display.quit()
                    pygame.quit()
                    exec(open("main.py").read())
                    break
            ##################################
           
           
            # quitter le jeu [X][-][□]
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0

            elif event.type == KEYDOWN:
                # retour au menu
                if event.key == K_ESCAPE:
                    continuer_jeu = 0
                if event.key == K_SPACE:
                    bombe.poser(perso.x, perso.y, image_bombe)
                    #bombe += 1
                    #if bombe < 2:
                        #continue
                    
                # touches de déplacement perso
                elif event.key == K_RIGHT:
                    perso.deplacer("droite")
                elif event.key == K_LEFT:
                    perso.deplacer("gauche")
                elif event.key == K_DOWN:
                    perso.deplacer("bas")
                elif event.key == K_UP:
                    perso.deplacer("haut")

                # touches de perso2

                if event.key == K_e:
                    bombe2.poser(perso2.x, perso2.y, image_bombe)
                elif event.key == K_d:
                    perso2.deplacer("droite")
                elif event.key == K_q:
                    perso2.deplacer("gauche")
                elif event.key == K_s:
                    perso2.deplacer("bas")
                elif event.key == K_z:
                    perso2.deplacer("haut")

        # définition des affichages au nouvelles positions
        # A faire => actualiser seulement ce qui a changer pour ameliorer fps
        # ≈15fps --> Intel(R) Atom(TM) x5-Z8350  CPU @ 1.44GHz (Ubuntu 16.04.4 LTS)
        #fenetre.blit(fond, (0, 0))
        niveau.afficher(fenetre)
        fenetre.blit(perso.direction, (perso.x, perso.y))
        fenetre.blit(perso2.direction, (perso2.x, perso2.y))
        fenetre.blit(bombe.bomb, (bombe.x, bombe.y))
        fenetre.blit(bombe2.bomb, (bombe2.x, bombe2.y))

        # affichage des flammes de l'explosion (à simplifier avec la class flamme)
        # A integrer la classe flamme dans la class bombe pour simplifier
        if bombe.explosion == 1:
            fenetre.blit(flamme.fflamme_b, (bombe.x, bombe.y + taille_sprite))
            fenetre.blit(flamme.fflamme_h, (bombe.x, bombe.y - taille_sprite))
            fenetre.blit(flamme.fflamme_g, (bombe.x - taille_sprite, bombe.y))
            fenetre.blit(flamme.fflamme_d, (bombe.x + taille_sprite, bombe.y))

        if bombe2.explosion == 1:
            fenetre.blit(flamme.fflamme_b, (bombe2.x, bombe2.y + taille_sprite))
            fenetre.blit(flamme.fflamme_h, (bombe2.x, bombe2.y - taille_sprite))
            fenetre.blit(flamme.fflamme_g, (bombe2.x - taille_sprite, bombe2.y))
            fenetre.blit(flamme.fflamme_d, (bombe2.x + taille_sprite, bombe2.y))

        

        ######################## LUCA
        stats.button_quit(fenetre, screesize[0], screesize[1])
        stats.player1(fenetre, screesize[0], screesize[1])
        stats.moves_p1(fenetre, screesize[0], screesize[1])
        stats.player2(fenetre, screesize[0], screesize[1])
        stats.moves_p2(fenetre, screesize[0], screesize[1])

        ########################

        # affichage de la frame
        pygame.display.flip()


        # verification des conditions de victoire
        game_over = bombe.exploser()
        if game_over == 1:
            winner = "Joueur 1"
            continuer = 0
            continuer_accueil = 0
            continuer_jeu = 0
            
        game_over = bombe2.exploser()
        if game_over == 1:
            winner = "Joueur 2"
            continuer = 0
            continuer_accueil = 0
            continuer_jeu = 0
           

        # print(datetime.now() - debugfps)

fenetre.fill(255,255,255)
pygame.display.flip()
victory.victoire(fenetre, winner, screesize[0], screesize[1])
time.sleep(10)
pygame.display.quit()
pygame.quit()


'''
pygame.display.quit()
pygame.quit()
exec(open("victory.py").read())
'''