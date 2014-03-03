class Picture (object):
	def __init__(self, x , y, size, image_to_set):
		self.x = x
		self.y = y
		self.xdim = size[0]
		self.ydim = size[1]
		self.image = image_to_set

		

		button_rec=pygame.Rect(x, y, size)
		button_sq=pygame.Surface([y, size])
		main_screen.blit(button_sq, button_rec)
		button_sq.fill((0, 255, 0))

		buttonimg = pygame.image.load(image_to_set)

		def clear_picture(self):
			
			
