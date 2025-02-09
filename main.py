import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    
    # Create clock
    clock = pygame.time.Clock()
    dt = 0

    # Create player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Game loop.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        player.draw(screen)
        pygame.display.flip()

        # Limit FPS to 60.
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
