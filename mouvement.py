from typing import Self
import pygments
from pyparsing import White


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygments.Surface((50, 50))
        self.image.fill(White)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.velocity_x = 5
        self.velocity_y = 5
        anim_forward = []
        anim_backward = []
        anim_jump = []
        self.damage = 10
        self.health = 30
        self.level = 1
        self.xp = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_left]:
            self.rect.x -= self.velocity_x
        keys = pygame.key.get_pressed()
        if keys[pygame.k_right]:
            self.rect.x += self.velocity_x
        keys = pygame.key.get_pressed()
        if keys[pygame.K_up]:
            self.rect.y += self.velocity_y

    def left():
        velocity_x -= 1
    def right():
        velocity_x += 1
    def up():
        velocity_y += 1
    def down():
        velocity_y -= 1
    
        

    
    
        

