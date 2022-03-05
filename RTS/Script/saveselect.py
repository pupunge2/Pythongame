import var
import const
import physics
import pygame

class UI():
    title_text = [8, 8]
    rect = [160, 160, 960, 400]
    save_file = [[160, 160, 960, 80], [160, 240, 960, 80], [160, 320, 960, 80], [160, 400, 960, 80]]
    save_text_1 = [[168, 168], [168, 248], [168, 328], [168, 408]]
    save_text_2 = [[168, 208], [168, 288], [168, 368], [168, 408]]

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    var.screen.blit(var.Font.title.render('Select Save File', True, const.Color.black), UI.title_text)

    pygame.draw.rect(var.screen, const.Color.black, UI.rect, 2)
    
    for i in range(4):
        pygame.draw.rect(var.screen, const.Color.black, UI.save_file[i], 2)
        
        if var.Save.data[i]['new'] == True:
            var.screen.blit(var.Font.main_1.render('New', True, const.Color.black), UI.save_text_1[i])

    pygame.display.flip()

def mouse_left_up():
    mouse = pygame.mouse.get_pos()

    if var.state == '':
        for i in range(4):
            if physics.point_inside_rect_list(mouse[0], mouse[1], UI.save_file[i]):
                if var.Save.data[i]['new'] == True:
                    var.Player_Ready.level_unlock.append(1)
                    
                    for i in range(1, len(const.Level.level)):
                        var.Player_Ready.level_lock.append(i)

                    var.scene = 'level_select'
                    var.state = ''