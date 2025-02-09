import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    
    # Create clock
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # Create player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0
    # Game loop.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        # Render        
        screen.fill(color="black")

        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()

        # Limit FPS to 60.
        dt = clock.tick(120)/1000


if __name__ == "__main__":
    main()
