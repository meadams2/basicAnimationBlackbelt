"""Marianne Adams
CS120 Basic Animation Blackbelt
Wednesday's Adventure Pt. 2
User will be able to move Wednesday using the arrow keys"""
import pygame

def main():
    pygame.init()
    
    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Wednesday's Adventure! Move Wednesday using the arrow keys!")
    
    #Entities
    #Create the background
    background = pygame.image.load("BackgroundImage.png")
    background.convert()
    background = pygame.transform.scale(background, (640, 480))
    
    #Create character
    wednesday = pygame.image.load("Wednesday.png")
    wednesday.convert_alpha()
    wednesday = pygame.transform.scale(wednesday, (100, 100))
    wednesday_x = 320
    wednesday_y = 240
    
    #Action
    #Assign variables
    dy = 5
    dx = 5
    clock = pygame.time.Clock()
    keepGoing = True
    mode = "right"
    
    #Set up loop
    while keepGoing:
        #Time
        clock.tick(30)
        
        #Event-handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    #Want to go down--but if I say go in negative direction, character will go up.
                    #Check if position is within screen bounds
                    wednesday_y += dy
                    mode = "down"
                    
                elif event.key == pygame.K_UP:
                    #Want to go up--if I say go in negative direction, character will go up.
                    #Check if position is within screen bounds
                    wednesday_y -= dy
                    mode = "up"
                    
                elif event.key == pygame.K_LEFT:
                    #Want to go right. If i say go right, positive direction
                    wednesday_x -= dx
                    mode = "left"
                    
                else:
                    wednesday_x += dx
                    mode = "right"
#     w.rect = wednesday.get_rect()
#     w.rect.left = wednesday_x
#     w.rect.top = wednesday_y
        if mode == "up":
            if wednesday_y < 0:
                wednesday_y = screen.get_height()
            else:
                wednesday_y -= dy
            
        elif mode == "down":
            if wednesday_y > screen.get_height():
                wednesday_y = 0
            else:
                wednesday_y += dy
        elif mode == "left":
            if wednesday_x < 0:
                wednesday_x = screen.get_width()
            else:
                wednesday_x -= dx
        else:
            if wednesday_x > screen.get_width():
                wednesday_x = 0
            else:
                wednesday_x += dx
    
        #refresh
        screen.blit(background, (0, 0))
        screen.blit(wednesday, (wednesday_x, wednesday_y))
    
        pygame.display.flip()
        
    pygame.quit

if __name__ == "__main__":
    main()
        
                
        
    