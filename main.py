import pygame 
import blocks
if __name__=="__main__":
	pygame.init()
	main_screen=pygame.display.set_mode((600,600))
    main_screen.fill((175,238,238))
    while True:
		pygame.display.flip()
	a = blocks.Button([10,10], [10,10], [255,0,0])