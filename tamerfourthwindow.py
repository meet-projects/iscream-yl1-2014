import pygame
import blocks
import labelclass

def draw_second(main_screen):
	main_screen.fill((200,116,76))





	a4 = blocks.button([100,100],[100,150],(130,122,255))
	a4.create(main_screen)
	la4 = labelclass.Label([130,250],[100,25],"Cone",20)
	la4.createlabel(main_screen)	
	b4 = blocks.button([100,100],[400,150],(130,112,255))
	b4.create(main_screen)
	lb4 = labelclass.Label([440,250],[100,25],"Cup",20)
	lb4.createlabel(main_screen)	
	c4 = blocks.button([460,70],[100,25],(130,112,255))
	c4.create(main_screen)
	lc4 = labelclass.Label([100,25],[100,25],"choose your icecream container",40)
	lc4.createlabel(main_screen)	
	d4 = blocks.button([120,50],[150,550],(130,112,255))
	d4.create(main_screen)
	ld4 = labelclass.Label([175,580],[120,50],"Back", 30)
	ld4.createlabel(main_screen)
	e4 = blocks.button([120,50],[300,550],(130,112,255))
	e4.create(main_screen)
	le4 = labelclass.Label([325,580],[120,50],"Next", 30)
	le4.createlabel(main_screen)


if __name__=="__main__":
	pygame.init()
	main_screen=pygame.display.set_mode((600,600))

	draw_second(main_screen)

	while True:
		ev = pygame.event.poll()
	
		pygame.display.flip()
