import pygame
class Label(object):
	def __init__(self, location , size, text, fontsize):
		self.location = location
		self.fontsize = fontsize
		self.size = size
		self.text = text
		self.label_rec = pygame.Rect(self.location[0], self.location[1], self.size[0], self.size[1]) 
		orderlabel = pygame.font.Font(None, self.fontsize)
		self.label = orderlabel.render(self.text, 1, (0,0,0))	



	def createlabel(self, main_screen):
		main_screen.blit(self.label, self.label_rec)
		
if  __name__ == "__main__":
	pygame.init()
	main_screen=pygame.display.set_mode((600,600))
	main_screen.fill((175,238,238))
	A = Label([100,100], [50,50], "sdfhgjkdfh", 200)
	A.createlabel(main_screen)


	while True:
		ev = pygame.event.poll()
	
		pygame.display.flip()
