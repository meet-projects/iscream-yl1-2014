import pygame
import blocks
import labelclass
if __name__=="__main__":
	pygame.init()
	main_screen=pygame.display.set_mode((600,600))
    	main_screen.fill((196,255,255))





	a4 = blocks.button([100,100],[100,150],(58,255,255))
	a4.create(main_screen)
	la4 = labelclass.Label([100,250],[100,25],"Vanilla",20)
	la4.createlabel(main_screen)	
	b4 = blocks.button([100,100],[400,150],(58,255,255))
	b4.create(main_screen)
	lb4 = labelclass.Label([400,250],[100,25],"Chocolate",20)
	lb4.createlabel(main_screen)	
	c4 = blocks.button([100,100],[250,300],(58,255,255))
	c4.create(main_screen)
	lc4 = labelclass.Label([250,400],[100,25],"Strawberry",20)
	lc4.createlabel(main_screen)	
	d4 = blocks.button([120,50],[150,550],(58,255,255))
	d4.create(main_screen)
	ld4 = labelclass.Label([150,550],[120,50],"Previous", 30)
	ld4.createlabel(main_screen)
	e4 = blocks.button([120,50],[300,550],(58,255,255))
	e4.create(main_screen)
	le4 = labelclass.Label([300,550],[120,50],"Next", 30)
	le4.createlabel(main_screen)
	l4 = labelclass.Label([250,25],[150,75],"Flavors",50)
	l4.createlabel(main_screen)

	while True:
		ev = pygame.event.poll()
	
		pygame.display.flip()
