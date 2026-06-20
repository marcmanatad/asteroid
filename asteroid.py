import pygame, random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            first_asteroid_velocity = self.velocity.rotate(random.uniform(20,50))
            second_asteroid_velocity = self.velocity.rotate(-(random.uniform(20,50)))
            smaller_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position.x, self.position.y, smaller_radius)
            second_asteroid = Asteroid(self.position.x, self.position.y, smaller_radius)
            first_asteroid.velocity = first_asteroid_velocity * 1.2
            second_asteroid.velocity = second_asteroid_velocity * 1.2
