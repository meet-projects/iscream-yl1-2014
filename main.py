import pygame
import blocks 
import lableclass 
def clear_screen():
	
	

if __name__=="__main__":
	pygame.init()
	main_screen=pygame.display.set_mode((600,600))
        main_screen.fill((175,238,238))
        
       	a=blocks.button([80,60],[100,200], (232,148,172))       
	a.create(main_screen)
        b=blocks.button([80,60],[250,200], (232,148,172))       
	b.create(main_screen)
        c=blocks.button([80,60],[400,200], (232,148,172))       
	c.create(main_screen)
        
	while True:
		ev = pygame.event.poll()
	
		pygame.display.flip()
