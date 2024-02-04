#import libraries
import pygame
import random
import sys
from pygame import mixer
import random
import math
# from terrain import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (0,255,255)
GREY = (100,100,100)

pygame.init()
 
size = (1600, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Gradius')

clock = pygame.time.Clock()

class Button(pygame.sprite.Sprite):
    
    def __init__(self,colour,text,position,size,font_name):

        super().__init__()
        #define variables
        self.colour = colour
        self.rect = 0
        self.text = text
        self.position = position
        self.size = size
        self.font_name = font_name
        #wider letters for hitbox
        if 'M' in self.text: 
            self.hitbox = pygame.Rect((position), ((len(self.text) * 75) + 50,self.size * 0.8666))
        elif 'O' in self.text:
            self.hitbox = pygame.Rect((position), ((len(self.text) * 75) + 25,self.size * 0.8666))
        else:
            self.hitbox = pygame.Rect((position), (len(self.text) * 75,self.size * 0.8666))
        
        #sets font
        self.font = pygame.font.SysFont('Barcade',self.size)
    
    #draw the text on the desired screen
    def draw(self,screen):
        screen.blit(self.font.render(str(self.text), 1, self.colour), (self.position))
    
    #Returns true if the mouse is over the text
    def colliding_with_mouse(self):
        return self.hitbox.collidepoint(pygame.mouse.get_pos())