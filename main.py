
import pygame
import blocks 
import labelclass 


def clear_screen(r,g,b):
    button_rec = pygame.Rect(0,0 ,600 ,600 )
    button_sq = pygame.Surface([600, 600])
    button_sq.fill((r, g, b))
    main_screen.blit(button_sq, button_rec)


if __name__=="__main__":
    pygame.init()
    main_screen=pygame.display.set_mode((600,600))
    main_screen.fill((255,182,193))

    a1=blocks.button([80,60],[100,200], (232,148,172))   
    a1.create(main_screen)
    b1=blocks.button([80,60],[250,200], (232,148,172))       
    b1.create(main_screen)
    c1=blocks.button([80,60],[400,200], (232,148,172))       
    c1.create(main_screen)
    
    scoopnum = 0

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos
            if a1.button_rec.collidepoint(x, y):
                clear_screen(175,238,238)
                scoopnum = 1
            elif b1.button_rec.collidepoint(x, y):
                clear_screen(175,238,238)
                scoopnum = 2
            else :
                clear_screen(175,238,238)
                scoopnum = 3

        if scoopnum == 1:
            a2=blocks.button([80,60],[100,200], (218,109,128))   
            a2.create(main_screen)
            b2=blocks.button([80,60],[250,200], (218,109,128))       
            b2.create(main_screen)
        elif scoopnum == 2:
            a2=blocks.button([80,60],[100,200], (218,109,128))   
            a2.create(main_screen)
            b2=blocks.button([80,60],[250,200], (218,109,128))       
            b2.create(main_screen)
        else:
            a2=blocks.button([80,60],[100,200], (218,109,128))   
            a2.create(main_screen)
            b2=blocks.button([80,60],[250,200], (218,109,128))       
            b2.create(main_screen)
        #if ev.type == pygame.MOUSEBUTTONDOWN:
            #x, y == ev.pos





    
        pygame.display.flip()
