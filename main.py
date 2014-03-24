import pygame
import blocks  

if __name__=="__main__":
	pygame.init()
	main_screen=pygame.display.set_mode((600,600))
	main_screen.fill((175, 238, 238))
	a=blocks.button([70,50],[50,50], (232,148,172))       
	a.create(main_screen)
        
	while True:
		ev = pygame.event.poll()
	
		pygame.display.flip()