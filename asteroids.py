import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        ru = random.uniform(20, 50)
        new_asteroid_1_velocity = self.velocity.rotate(ru)
        new_asteroid_2_velocity = self.velocity.rotate(-ru)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position[0], self.position[1], new_radius)
        a2 = Asteroid(self.position[0], self.position[1], new_radius)
        a1.velocity = new_asteroid_1_velocity * 1.2
        a2.velocity = new_asteroid_2_velocity * 1.2

