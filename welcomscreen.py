import pygame
import picture 
import blocks
import labelclass

def draw_screen(main_screen):
    main_screen.fill((0,0,0))

   # picture1= picture.Picture(105,15,[250,270],"finallogo.jpg")
   # picture1.draw(main_screen)
    bimage = picture.Picture(0, 0, [600, 600], "icecream.jpeg")
    bimage.draw(main_screen)
    global p1
    p1=blocks.button([60,40],[510,550], (255,255,255))
    p1.create(main_screen)
    lp1=labelclass.Label([510,550],[60,40],"Order",25)
    lp1.createlabel(main_screen)



if __name__=="__main__":
    pygame.init()
    main_screen=pygame.display.set_mode((600,600))
    draw_screen(main_screen)


    while True:
        ev = pygame.event.poll()
        pygame.display.flip()