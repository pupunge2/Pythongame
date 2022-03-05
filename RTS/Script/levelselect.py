import img
import var
import const
import pygame
import physics

class UI():
    title_text = [8, 8]

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    var.screen.blit(var.Font.title.render('Select Scenario', True, const.Color.black), UI.title_text)

    for i in range(1, len(const.Level.level)):
        start = [const.Level.level[i][1] + 40, const.Level.level[i][2] + 40]
        endpoint = const.Level.level[i][4]
        end = [const.Level.level[endpoint][1] + 40, const.Level.level[endpoint][2] + 40]
        pygame.draw.line(var.screen, const.Color.black, start, end, 6)

        text_pos = [const.Level.level[i][1], const.Level.level[i][2] + 80]
        var.screen.blit(var.Font.main_1.render(str(const.Level.level[i][3]), True, const.Color.black), text_pos)

    for i in range(len(var.Player_Ready.level_lock)):
        level = var.Player_Ready.level_lock[i]
        var.screen.blit(img.Level.lock, const.Level.level[level][1:3])

    for i in range(len(var.Player_Ready.level_cleared)):
        level = var.Player_Ready.level_cleared[i]
        var.screen.blit(img.Level.cleared, const.Level.level[level][1:3])

    for i in range(len(var.Player_Ready.level_unlock)):
        level = var.Player_Ready.level_unlock[i]
        var.screen.blit(img.Level.unlock, const.Level.level[level][1:3])

    pygame.display.flip()

def mouse_left_up():
    mouse = pygame.mouse.get_pos()

    if var.state == '':
        for i in range(len(var.Player_Ready.level_cleared)):
            level = var.Player_Ready.level_cleared[i]
            level_rect = const.Level.level[level][1:3] + [80, 80]
            
            if physics.point_inside_rect_list(mouse[0], mouse[1], level_rect):
                var.scene = 'field'
                var.state = ''

        for i in range(len(var.Player_Ready.level_unlock)):
            level = var.Player_Ready.level_unlock[i]
            level_rect = const.Level.level[level][1:3] + [80, 80]
            
            if physics.point_inside_rect_list(mouse[0], mouse[1], level_rect):
                var.scene = 'field'
                var.state = ''
