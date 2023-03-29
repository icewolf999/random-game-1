from mouvement import Player 

 
 

pygame.init()  

 
 

  

screen_dim = (1300,650)  

 
 

screen_color = (0,0,0)  

 
 

screen = pygame.display.set_mode(screen_dim)  

 
 

clock = pygame.time.Clock()  

 
 

running = True 

 
 
 
 

while running:  

 
 

    for event in pygame.event.get():  

 
 

        if event.type == pygame.QUIT:  

                running = False  

    

    keys = pygame.key.get_pressed() 

    if keys[pygame.K_LEFT]: 

         Player.left() 

    if keys[pygame.K_RIGHT]: 

         Player.right() 

    if keys[pygame.K_UP]: 

         Player.up() 

    if keys[pygame.K_DOWN]: 

         Player.down() 

 
 
 

    screen.fill(screen_color)  

 
 

    pygame.display.update()  

 
 
 

    clock.tick(60)

