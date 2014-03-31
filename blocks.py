import pygame

class button(object):
	def __init__(self, size, location, color):
		self.size = size
		self.location = location
		self.color = color
		self.button_rec = pygame.Rect(self.location[0], self.location[1], self.size[0], self.size[1])
		self.button_sq = pygame.Surface([self.size[0], self.size[1]])
		self.button_sq.fill(self.color)

	def create(self, main_screen):
		main_screen.blit(self.button_sq, self.button_rec) 
	


