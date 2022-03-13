import var
import const
import physics
import pygame

class UI():
    title_text = [8, 8]
    version_text = [8, 660]
    start_button = [160, 160, 960, 80]
    option_button = [160, 240, 960, 80]
    about_button = [160, 320, 960, 80]
    editor_button = [160, 400, 960, 80]
    custom_button = [160, 480, 960, 80]
    start_text = [168, 180]
    option_text = [168, 260]
    about_text = [168, 340]
    editor_text = [168, 420]
    custom_text = [168, 500]

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    var.screen.blit(var.Font.title.render('Desserterria Strawberry', True, const.Color.black), UI.title_text)

    pygame.draw.rect(var.screen, const.Color.black, UI.start_button, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.option_button, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.about_button, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.editor_button, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.custom_button, 2)

    var.screen.blit(var.Font.title.render('Start Game', True, const.Color.black), UI.start_text)
    var.screen.blit(var.Font.title.render('Option', True, const.Color.black), UI.option_text)
    var.screen.blit(var.Font.title.render('About', True, const.Color.black), UI.about_text)
    var.screen.blit(var.Font.title.render('Editor', True, const.Color.black), UI.editor_text)
    var.screen.blit(var.Font.title.render('Custom', True, const.Color.black), UI.custom_text)

    var.screen.blit(var.Font.title.render('v0.0.1', True, const.Color.black), UI.version_text)
    pygame.display.flip()

def mouse_left_up():
    mouse = pygame.mouse.get_pos()

    if var.state == '':
        if physics.point_inside_rect_list(mouse[0], mouse[1], UI.start_button):
            var.scene = 'save_select'

        elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.editor_button):
            var.scene = 'editor'
            var.Editor.selected_unit = -1
            var.Editor.team_mode = 1

        elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.custom_button):
            var.scene = 'custom'
            var.Custom.load_map_name = ''
            var.Custom.load_map_name_edit = False

