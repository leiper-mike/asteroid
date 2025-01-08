from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random
class Asteroid(CircleShape):
     def __init__(self,x,y,radius):
          super().__init__(x,y,radius)
     def draw(self, screen):
          pygame.draw.circle(screen, "white", self.position,self.radius, 2)
     def update(self,dt):
          self.position += self.velocity * dt
     def split(self):
          self.kill()
          if self.radius <= ASTEROID_MIN_RADIUS:
               return
          split_angle = random.uniform(20,50)
          v1 = self.velocity.rotate(split_angle)
          v2 = self.velocity.rotate(-split_angle)
          Asteroid(self.position[0],self.position[1],self.radius - ASTEROID_MIN_RADIUS).velocity = v1 * 1.2
          Asteroid(self.position[0],self.position[1],self.radius - ASTEROID_MIN_RADIUS).velocity = v2 * 1.2