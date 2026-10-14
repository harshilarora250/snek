import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Snake! Eat em' apples")

while True:
    # take input

    # output
    window.fill((255,255,255))
    pygame.display.flip()