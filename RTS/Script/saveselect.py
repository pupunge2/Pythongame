import var
import const
import physics
import pygame

class UI():
    title_text = [8, 8]
    rect = [160, 160, 960, 400]
    save_file = [[160, 160, 960, 80], [160, 240, 960, 80], [160, 320, 960, 80], [160, 400, 960, 80]]

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    var.screen.blit(var.Font.title.render('Save File Select', True, const.Color.black), UI.title_text)

    pygame.draw.rect(var.screen, const.Color.black, UI.rect, 2)
    
    for i in range(4):
        pygame.draw.rect(var.screen, const.Color.black, UI.save_file[i], 2)

    pygame.display.flip()

def mouse_left_up():
    mouse = pygame.mouse.get_pos()

    if var.state == '':
        for i in range(4):
            if physics.point_inside_rect_list(mouse[0], mouse[1], UI.save_file[i]):
                pass
