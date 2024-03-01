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
        
        self.block_head = (6, 6)
        self.block_body = [(6,5), (6,4)]
        
        self.rects=[] #List for storing the body parts of the block

        self.rect = self.image.get_rect()

        self.rect.x = self.block_head[0]*TILE_WIDTH
        self.rect.y = self.block_head[1]*TILE_WIDTH

        for body_part in self.block_body:
            self.rects.append(pygame.Rect(body_part[0]*TILE_WIDTH, body_part[1]*TILE_WIDTH, TILE_WIDTH, TILE_WIDTH))