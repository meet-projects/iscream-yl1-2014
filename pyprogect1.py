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

	#to_clear_a_picture
		if__name__=="__main__":

			pygame.init()
			main_screen = pygame.display.set_mode((600, 600))
			main_screen.fill((255,255,255))
			a=blocks.button([70, 50] , [50,50] , (232,148, 172))
			a.create(main_screen)
			button_rec = pygame.Rect (100, 200, 50, 20)
			button_sq = pygame.Surface([20, 20])
			main_screen.blit(button_sq, button_rec)

			while true:
				ev = pygame.event.poll()

				pygame.displpay.flip()
			
