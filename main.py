import pygame
import blocks 
import labelclass 
<<<<<<< HEAD

def clear_screen(r,g,b):
	button_rec = pygame.Rect(0,0 ,600 ,600 )
	button_sq = pygame.Surface([20, 20])
	button_sq.fill((r, g, b))
	main_screen.blit(button_sq, button_rec)








=======
def clear_screen():
	
	
>>>>>>> 43dff2532c701c07701e0c5f95756d49642cd4ad
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
	d=blocks.button([80,60],[250,400], (232,148,172))       
	d.create(main_screen)

		


	while True:
		ev = pygame.event.poll()
	
		pygame.display.flip()
