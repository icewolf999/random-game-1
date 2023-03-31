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



 
 
 

    screen.fill(screen_color)  

 
 

    pygame.display.update()  

 
 
 

    clock.tick(60)

