import pygments
from pyparsing import White
import pygame 
pygame.init()

running = True

class rat():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("rat1.zip")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = 500 - int(self.rect.width / 2)
        self.rect.y = 150 - int(self.rect.width / 2)
        self.x = x
        self.y = y
        hp = 40
        self.velocity_x = 5
        self.velocity_y = 5
        

    while running:
        anim_forward_ratn = []
        anim_backward_ratn = []
        anim_up_ratn = []
        anim_down_ratn = []



class ratb():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygments.Surface((50, 50))
        self.image.fill(White)
        self.x = x
        self.y = y
        hp = 40
        self.velocity_x = 5
        self.velocity_y = 5
        

    while running:
        anim_forward_ratb = []
        anim_backward_ratb = []
        anim_up_ratb = []
        anim_down_ratb = []


class monkey():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygments.Surface((50, 50))
        self.image.fill(White)
        self.x = x
        self.y = y
        hp = 40
        self.velocity_x = 5
        self.velocity_y = 5
        

    while running:
        anim_forward_monkey = []
        anim_backward_monkey = []
        anim_up_monkey = []
        anim_down_monkey = []

class dragon():
    def __init__(self, x, y):
         super().__init__()
         self.image = pygments.Surface((50, 50))
         self.image.fill(White)
         self.x = x
         self.y = y
         hp = 40
         self.velocity_x = 5
         self.velocity_y = 5




           
        
    
     
        

        