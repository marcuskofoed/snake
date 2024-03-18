import pygame
import random
from constants import *

class Block(pygame.sprite.Sprite):
    def __init__(self, screen, color):
        super().__init__()
        self.screen = screen
        self.color = color
        self.image = pygame.Surface((TILE_WIDTH, TILE_WIDTH))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.random_position()
    def draw(self, surface):
        surface.blit(self.image, self.rect)    
           
    def random_position(self):
        rand_x = random.randint(0,BOARD[0])*TILE_WIDTH
        rand_y = random.randint(0,BOARD[1])*TILE_WIDTH
        return (rand_x, rand_y)

    """
    TODO:
    Random position ala point
    Tegn denne block på samme måde som point --> self.draw()
    add to all_sprites
    lav en colission ved at loope gennem block_sprites og tjekke colissions 
    """