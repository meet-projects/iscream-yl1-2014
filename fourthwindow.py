import pygame
import blocks
import labelclass

def draw4(main_screen):
	main_screen.fill((255,255,103))

	l4_1 = labelclass.Label([200,25],[150,75],"Toppings",50)
	l4_1.createlabel(main_screen)
	l4_2 = labelclass.Label([50,100],[200,50],"Syrups",35)
	l4_2.createlabel(main_screen)
	l4_3 = labelclass.Label([400,100],[200,50],"Other",35)
	l4_3.createlabel(main_screen)
	
	a4 = blocks.button([100,50],[50,150],(255,122,103))
	a4.create(main_screen)
	la4 = labelclass.Label([50,200],[100,25],"Chocolate Syrup",20)
	la4.createlabel(main_screen)	
	
	b4 = blocks.button([100,50],[50,250],(255,122,103))
	b4.create(main_screen)
	lb4 = labelclass.Label([50,300],[100,25],"Maple Syrup",20)
	lb4.createlabel(main_screen)	
	

	c4 = blocks.button([100,50],[400,150],(255,122,103))
	c4.create(main_screen)
	lc4 = labelclass.Label([400,200],[100,25],"Chocolate Chips",20)
	lc4.createlabel(main_screen)	
	d4 = blocks.button([100,50],[400,250],(255,122,103))
	d4.create(main_screen)
	ld4 = labelclass.Label([400,300],[100,25],"cherry",20)
	ld4.createlabel(main_screen)
	e4 = blocks.button([100,50],[400,350],(255,122,103))
	e4.create(main_screen)
	le4 = labelclass.Label([400,400],[100,25],"Sprinkles",20)
	le4.createlabel(main_screen)


	f4 = blocks.button([120,50],[150,550],(255,122,103))
	f4.create(main_screen)
	lf4 = labelclass.Label([150,550],[120,50],"Previous", 30)
	lf4.createlabel(main_screen)
	g4 = blocks.button([120,50],[300,550],(255,122,103))
	g4.create(main_screen)
	lg4 = labelclass.Label([300,550],[120,50],"Next", 30)
	lg4.createlabel(main_screen)
	


if __name__=="__main__":
	pygame.init()
	main_screen=pygame.display.set_mode((600,600))

	draw4(main_screen)

	while True:
		ev = pygame.event.poll()
	
		pygame.display.flip()
