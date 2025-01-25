import pygame
import sys

#Initialiser pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jeu du serpent")
screen.blit(pygame.image.load("welcome.png"), [400, 300])
pygame.display.flip()
pygame.time.wait(3000)
