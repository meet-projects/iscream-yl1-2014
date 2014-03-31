import pygame
class Label(object):
	def __init__(self, location , size, color , font, sizelabels):
		self.location = location
		self.size = size
		self.color = color
		self.font = font	



	def createlabel(self, main_screen):
		label_rec = pygame.Rect(self.location[0], self.location[1], self.size[0], self.size[1]) 
		orderlabel = pygame.font.Font(self.font, self.color)
		label = orderlabel.render()
		main_screen.blit(label, label_rec)
		
