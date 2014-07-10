import pygame
class Label(object):
	def __init__(self, location_ts , size_ts, color_ts , font_ts, sizelabels_ts):
		self.location = location_ts
		self.size = size_ts
		self.color = color_ts
		self.font = font_ts	



	def createlabel(self):
		label_rec = pygame.Rect(self.location_ts[0], self.location_ts[1], self.size_ts[0], self.size_ts[1]) 
		orderlabel = pygame.font.Font(self.font_ts,self.sizelabels_ts, color_ts)
		label = orderlabel.render()
		main_screen.blit(label, label_rec)
		
