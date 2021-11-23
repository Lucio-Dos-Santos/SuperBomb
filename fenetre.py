import pygame
import sys
import random
import time 

TILE_WIDTH = 40
TILE_HEIGHT = 40

WINDOW_WIDTH = 13*TILE_HEIGHT
WINDOW_HEIGHT = 13*TILE_WIDTH

BACKGROUND = (119, 160,244)

grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

herbe_img = None
bloc_img = None
box_img = None


terrain_images = []


def game_init():
     

    global s
    s= pygame.display.set_mode((13*TILE_WIDTH, 13*TILE_HEIGHT))
    pygame.display.set_caption('SuperBomb')
    
    
   
    global clock
    clock = pygame.time.Clock()
    
    global grass_img
    grass_img = pygame.image.load('assets/herbe.jpg')
    grass_img = pygame.transform.scale(grass_img, (TILE_WIDTH, TILE_HEIGHT))
    global block_img
    block_img = pygame.image.load('assets/bloc.jpg')
    block_img = pygame.transform.scale(block_img, (TILE_WIDTH, TILE_HEIGHT))
    global box_img
    box_img = pygame.image.load('assets/box.png')
    box_img = pygame.transform.scale(box_img, (TILE_WIDTH, TILE_HEIGHT))
    
    global terrain_images
    terrain_images = [grass_img, block_img, box_img, grass_img]
    
def draw():
    s.fill(BACKGROUND)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            s.blit(terrain_images[grid[i][j]], (i * TILE_WIDTH, j * TILE_HEIGHT, TILE_HEIGHT, TILE_WIDTH))

   
    pygame.display.update()


def generate_map():

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] != 0:
                continue
            elif (i < 3 or i > len(grid) - 4) and (j < 3 or j > len(grid[i]) - 4):
                continue
            if random.randint(0, 9) < 7:
                grid[i][j] = 2

    return


game_init()
draw()
generate_map()