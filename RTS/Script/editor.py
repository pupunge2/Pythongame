import var
import const
import pygame
import physics

class UI():
    title_text = [8, 8]

    class Start():
        rect = [160, 160, 960, 400]
        name = [240, 160, 800, 80]
        name_text = [248, 180]
        theme = []

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    if var.state == 'start':
        var.screen.blit(var.Font.title.render('New Map', True, const.Color.black), UI.title_text)
        pygame.draw.rect(var.screen, const.Color.black, UI.Start.rect, 2)
        pygame.draw.rect(var.screen, const.Color.black, UI.Start.name, 2)
        var.screen.blit(var.Font.title.render(str(var.Editor.map_name), True, const.Color.black), UI.Start.name_text)

    pygame.display.flip()

def mouse_left_up():
    mouse = pygame.mouse.get_pos()

    if var.state == 'start':
        if physics.point_inside_rect_list(mouse[0], mouse[1], UI.Start.name):
            if var.Editor.map_name_edit == True:
                var.Editor.map_name_edit = False
            else:
                var.Editor.map_name_edit = True

def key_down(key):
    if var.state == 'start':
        if var.Editor.map_name_edit == True:
            if key >= 97 and key <= 122:
                temp_char = chr(key)
                var.Editor.map_name += temp_char

            elif key == 32:
                var.Editor.map_name += ' '

            elif key == 8:
                if len(var.Editor.map_name) > 0:
                    var.Editor.map_name = var.Editor.map_name[:len(var.Editor.map_name) - 1]
