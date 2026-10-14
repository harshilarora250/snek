import pygame

print("Hello World! From the developers of Snake!")

pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Snake! Eat em' apples")

player = pygame.surface.Surface((100,100))
player.fill((255,255))

player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

falling_object = pygame. surface.Surface((50, 50))
falling_object.fill((255, 255, 255))
falling_object_x = 0
falling_object_y = O
falling_object_vel_x = O
falling_object_vel_y = 0.3

while True:
    # take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_vel_x = -0.2
        if event.key == pygame.K_RIGHT:
            player_vel_y = 0.2

    else: player_vel_x = 0
    player_vel_y = 0
    
    # output
    window.fill((255,255,255))
    window.blit(player, dist:(player_x, player_y))
    pygame.display.flip()