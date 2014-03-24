import pygame
import blocks 
import lableclass 
def clear_screen():
	
	

if __name__=="__main__":
	pygame.init()
	main_screen=pygame.display.set_mode((600,600))
<<<<<<< HEAD
	main_screen.fill((175, 238, 238))
	a=blocks.button([70,50],[50,50], (232,148,172))       
=======
        main_screen.fill((175,238,238))
        
       	a=blocks.button([80,60],[100,200], (232,148,172))       
>>>>>>> a29e29df09f049a23d9cf66298bef56ae4867d31
	a.create(main_screen)
        b=blocks.button([80,60],[250,200], (232,148,172))       
	b.create(main_screen)
        c=blocks.button([80,60],[400,200], (232,148,172))       
	c.create(main_screen)
        
	while True:
		ev = pygame.event.poll()
	
		pygame.display.flip()
