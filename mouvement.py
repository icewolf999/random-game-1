class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        velocity_x = 0
        velocity_y = 0
        anim_forward = []
        anim_backward = []
        anim_jump = []
        self.damage = 10
        self.health = 30
        self.level = 1
        self.xp = 0
    def left():
        velocity_x -= 1
    def right():
        velocity_x += 1
    def up():
        velocity_y += 1
    def down():
        velocity_y -= 1

    
    
        

