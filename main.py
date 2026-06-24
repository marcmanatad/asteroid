import pygame, sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.Surface.fill(screen, color="black")
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    pygame.sprite.Sprite.kill(shot)
                    asteroid.split()
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
           


if __name__ == "__main__":
    main()
