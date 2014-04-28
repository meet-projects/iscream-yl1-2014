import pygame

if __name__=="__main__":
    pygame.init()
    main_screen=pygame.display.set_mode((600,600))
    main_screen.fill((255,102,102))

    a1=blocks.button([80,60],[250,500], (232,148,172))   
    a1.create(main_screen)

    while True:
    	ev = pygame.event.poll()
    	pygame.display.flip()