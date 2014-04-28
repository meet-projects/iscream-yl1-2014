import pygame
import blocks
import labelclass
if __name__=="__main__":
	pygame.init()
	main_screen=pygame.display.set_mode((600,600))
    	main_screen.fill((196,255,255))





	a3 = blocks.button([100,100],[100,150],(58,255,255))
	a3.create(main_screen)
	la3 = labelclass.Label([100,250],[100,25],"Vanilla",20)
	la3.createlabel(main_screen)	
	b3 = blocks.button([100,100],[400,150],(58,255,255))
	b3.create(main_screen)
	lb3 = labelclass.Label([400,250],[100,25],"Chocolate",20)
	lb3.createlabel(main_screen)	
	c3 = blocks.button([100,100],[250,300],(58,255,255))
	c3.create(main_screen)
	lc3 = labelclass.Label([250,400],[100,25],"Strawberry",20)
	lc3.createlabel(main_screen)	
	d3 = blocks.button([120,50],[150,550],(58,255,255))
	d3.create(main_screen)
	ld3 = labelclass.Label([150,550],[120,50],"Previous", 30)
	ld3.createlabel(main_screen)
	e3 = blocks.button([120,50],[300,550],(58,255,255))
	e3.create(main_screen)
	le3 = labelclass.Label([300,550],[120,50],"Next", 30)
	le3.createlabel(main_screen)
	l3 = labelclass.Label([250,25],[150,75],"Flavors",50)
	l3.createlabel(main_screen)

	while True:
		ev = pygame.event.poll()
	

		pygame.display.flip()
