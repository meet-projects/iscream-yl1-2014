import pygame
import blocks
import labelclass
import welcomscreen
import picture


def clear_screen(r, g, b):
    button_rec = pygame.Rect(0, 0, 600, 600)
    button_sq = pygame.Surface([600, 600])
    button_sq.fill((r, g, b))
    main_screen.blit(button_sq, button_rec)


if __name__ == "__main__":
    pygame.init()
    main_screen = pygame.display.set_mode((600, 600))

    welcomscreen.draw_screen(main_screen)

    scoopnum = 0
    vanilla = True
    update = True
    stepNum = 0
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = ev.pos

            if welcomscreen.p1.button_rec.collidepoint(x, y):
                clear_screen(255, 255, 255)
                main_screen.fill((255, 182, 193))

                lp1 = labelclass.Label([200, 45], [200, 40], "Choose Size", 50)
                lp1.createlabel(main_screen)

                a1 = blocks.button([80, 60], [100, 200], (232, 148, 172))
                a1.create(main_screen)
                aimage = picture.Picture(100, 280, [60, 100], "cups.png")
                aimage.draw(main_screen)

                b1 = blocks.button([80, 60], [250, 200], (232, 148, 172))
                b1.create(main_screen)
                bimage = picture.Picture(250, 280, [60, 100], "mediumcone.jpg")
                bimage.draw(main_screen)

                c1 = blocks.button([80, 60], [400, 200], (232, 148, 172))
                c1.create(main_screen)
                cimage = picture.Picture(400, 280, [60, 100], "cone.png")
                cimage.draw(main_screen)
                stepNum = 1
            if stepNum == 1 and update == True:
                if a1.button_rec.collidepoint(x, y) and scoopnum == 0:
                    clear_screen(175, 238, 238)
                    scoopnum = 1
                    stepNum = 2
                    update = False
                elif b1.button_rec.collidepoint(x, y) and scoopnum == 0:
                    clear_screen(175, 238, 238)
                    scoopnum = 2
                    stepNum = 2
                    update = False

                elif c1.button_rec.collidepoint(x, y) and scoopnum == 0:
                    clear_screen(175, 238, 238)
                    scoopnum = 3
                    stepNum = 2
                    update = False

            if stepNum == 2:
                if scoopnum == 1:
                    vanillaLabel = labelclass.Label([100, 150], [200, 40], "Vanilla", 30)
                    vanillaLabel.createlabel(main_screen)
                    a2 = blocks.button([80, 60], [100, 200], (218, 109, 128))
                    a2.create(main_screen)

                    chocLabel = labelclass.Label([250, 150], [200, 40], "Chocolate", 30)
                    chocLabel.createlabel(main_screen)
                    b2 = blocks.button([80, 60], [250, 200], (218, 109, 128))
                    b2.create(main_screen)
                    stepNum = 3
                    update = False

                elif scoopnum == 2:
                    vanillaLabel = labelclass.Label([100, 150], [200, 40], "Vanilla", 30)
                    vanillaLabel.createlabel(main_screen)
                    a2 = blocks.button([80, 60], [100, 200], (218, 109, 128))
                    a2.create(main_screen)

                    chocLabel = labelclass.Label([250, 150], [200, 40], "Chocolate", 30)
                    chocLabel.createlabel(main_screen)

                    b2 = blocks.button([80, 60], [250, 200], (218, 109, 128))
                    b2.create(main_screen)
                    stepNum = 3
                    update = False

                elif scoopnum == 3:
                    vanillaLabel = labelclass.Label([100, 150], [200, 40], "Vanilla", 30)
                    vanillaLabel.createlabel(main_screen)
                    a2 = blocks.button([80, 60], [100, 200], (218, 109, 128))
                    a2.create(main_screen)

                    chocLabel = labelclass.Label([250, 150], [200, 40], "Chocolate", 30)
                    chocLabel.createlabel(main_screen)
                    b2 = blocks.button([80, 60], [250, 200], (218, 109, 128))
                    b2.create(main_screen)
                    stepNum = 3
                    update = False

            if stepNum == 3 and update == True:
                if a2.button_rec.collidepoint(x, y):
                    clear_screen(175, 238, 238)
                    vanilla = True
                    didSetVanilla = True

                    l4_2 = labelclass.Label([200, 50], [100, 50], "Syrups", 35)
                    l4_2.createlabel(main_screen)

                    la4 = labelclass.Label([100, 150], [100, 50], "Chocolate Syrup", 35)
                    la4.createlabel(main_screen)

                    b4 = blocks.button([100, 100], [100, 180], (255, 122, 103))
                    b4.create(main_screen)

                    lb4 = labelclass.Label([400, 150], [100, 50], "Maple Syrup", 35)
                    lb4.createlabel(main_screen)

                    c4 = blocks.button([100, 100], [400, 180], (255, 122, 103))
                    c4.create(main_screen)
                    stepNum = 4
                    update = False

                elif b2.button_rec.collidepoint(x, y):
                    clear_screen(175, 238, 238)
                    vanilla = False
                    didSetVanilla = True

                    l4_2 = labelclass.Label([200, 50], [100, 50], "Syrups", 35)
                    l4_2.createlabel(main_screen)

                    la4 = labelclass.Label([100, 150], [100, 50], "Chocolate Syrup", 35)
                    la4.createlabel(main_screen)

                    b4 = blocks.button([100, 100], [100, 180], (255, 122, 103))
                    b4.create(main_screen)

                    lb4 = labelclass.Label([400, 150], [100, 50], "Maple Syrup", 35)
                    lb4.createlabel(main_screen)

                    c4 = blocks.button([100, 100], [400, 180], (255, 122, 103))
                    c4.create(main_screen)
                    stepNum = 4
                    update = False
            if stepNum == 4 and update == True:

                if b4.button_rec.collidepoint(x, y):

                    x = str(scoopnum)
                    if vanilla:
                        x = x + " " + "vanilla scoops with chocolate syrup"
                    else:
                        x = x + " " + "chocolate scoops with chocolate syrup"

                    clear_screen(175, 238, 238)
                    l4_3 = labelclass.Label([50, 100], [200, 50], x, 27)
                    l4_3.createlabel(main_screen)

                    l4_4 = labelclass.Label([50, 140], [200, 50], "$" + str(scoopnum * 3), 35)
                    l4_4.createlabel(main_screen)
                    bimage = picture.Picture(100, 150, [600, 600], "moneytakingcream.jpg")
                    bimage.draw(main_screen)
                elif c4.button_rec.collidepoint(x, y):
                    x = str(scoopnum)
                    if vanilla:
                        x = x + " " + "vanilla scoops with maple syrup"
                    else:
                        x = x + " " + "chocolate scoops with maple syrup"

                    clear_screen(175, 238, 238)

                    l4_3 = labelclass.Label([50, 100], [200, 50], x, 27)
                    l4_3.createlabel(main_screen)

                    l4_4 = labelclass.Label([50, 140], [200, 50], "$" + str(scoopnum * 3), 35)
                    l4_4.createlabel(main_screen)
                    bimage = picture.Picture(100, 150, [600, 600], "moneytakingcream.jpg")
                    bimage.draw(main_screen)
            update = True


            # if ev.type == pygame.MOUSEBUTTONDOWN:
            #x, y == ev.pos

        pygame.display.flip()