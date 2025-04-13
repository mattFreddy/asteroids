from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        ang_a = self.velocity.rotate(random_angle)
        ang_b = self.velocity.rotate(-random_angle)

        asteroid_a = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        asteroid_a.velocity = ang_a * 1.2

        asteroid_b = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        asteroid_b.velocity = ang_b * 1.2