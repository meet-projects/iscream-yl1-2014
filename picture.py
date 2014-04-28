import pygame

class Picture (object):
	def __init__(self, x , y, size, image_to_set):
		self.x = x
		self.y = y
		self.xdim = size[0]
		self.ydim = size[1]
		self.image = image_to_set
		self.button_rec=pygame.Rect(x, y, size[0], size[1])
		self.buttonimg = pygame.image.load(image_to_set)


	def draw (self, main_screen):
		main_screen.blit(self.buttonimg, self.button_rec)
			

