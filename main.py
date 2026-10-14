# Import any libraries that I may need
import pygame
import random

print("Hello World! From the developers of Snake!")

pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Snake! Eat em' apples")

player = pygame.Surface((100, 100))
player.fill((255, 255, 255))

player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

falling_object = pygame.Surface((50, 50))
falling_object.fill((255, 255, 255))
falling_object_x = 0
falling_object_y = 0
falling_object_vel_x = 0
falling_object_vel_y = 0.3


def collision_detection():
    return (
        player_x <= falling_object_x + falling_object.get_width()
        and player_x + player.get_width() >= falling_object_x
        and player_y <= falling_object_y + falling_object.get_height() + 5
        and player_y + player.get_height() >= falling_object_y
    )


while True:
    # Take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel_x = -0.2
            if event.key == pygame.K_RIGHT:
                player_vel_x = 0.2

    # Update positions
    player_x += player_vel_x
    player_y += player_vel_y

    falling_object_x += falling_object_vel_x
    falling_object_y += falling_object_vel_y

    # Output
    window.fill((255, 255, 255))
    window.blit(player, (player_x, player_y))
    window.blit(falling_object, (falling_object_x, falling_object_y))
    pygame.display.flip()