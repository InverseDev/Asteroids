import pygame
import sys
from player import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shootable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shootable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
