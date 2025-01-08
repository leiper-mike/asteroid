import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from AsteroidField import AsteroidField
from shot import Shot
def main():
     print("Starting asteroids!")
     print(f"Screen width: {SCREEN_WIDTH}" )
     print(f"Screen height: {SCREEN_HEIGHT}" )
     pygame.init()
     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
     clock = pygame.time.Clock()
     dt = 0
     updatable = pygame.sprite.Group()
     drawable = pygame.sprite.Group()
     asteroids = pygame.sprite.Group()
     shots = pygame.sprite.Group()
     AsteroidField.containers = (updatable)
     Asteroid.containers = (asteroids, updatable, drawable)
     Player.containers = (updatable, drawable)
     Shot.containers = (updatable, drawable, shots)
     asteroid_field = AsteroidField()
     player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
     while True:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    return
          screen.fill("black")
          dt = clock.tick(60) / 1000
          for u in updatable:
               u.update(dt)
          for a in asteroids:
               if a.collides(player):
                    print("Game over")
                    return
               for s in shots:
                    if a.collides(s):
                         a.split()
                         s.kill()
          for d in drawable:
               d.draw(screen)


          pygame.display.flip()
          
if __name__ == "__main__":
    main()