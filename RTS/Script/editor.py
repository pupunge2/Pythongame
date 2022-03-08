import var
import img
import const
import pygame
import physics

class UI():
    title_text = [8, 8]

    class Upper_Bar():
        new_button = [0, 0, 40, 40]
        save_button = [40, 0, 40, 40]
        exit_button = [1240, 0, 40, 40]

    class Start():
        title_text = [168, 168]
        rect = [160, 160, 960, 400]
        name = [240, 240, 800, 80]
        name_text = [248, 260]
        theme = []
        map_dir_button = [480, 160, 80, 80]
        campaign_dir_button = [560, 160, 80, 80]
        exit_button = [1080, 160, 40, 40]
        done_button = [1080, 520, 40, 40]

    class Main_Editor():
        minimap = [0, 40, 240, 240]
        left_bar = [0, 280, 240, 400]

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    var.screen.blit(img.Button.new_map, UI.Upper_Bar.new_button[:2])
    var.screen.blit(img.Button.save, UI.Upper_Bar.save_button[:2])
    var.screen.blit(img.Button.exit, UI.Upper_Bar.exit_button[:2])

    if var.state == 'start':
        var.screen.blit(var.Font.title.render('New Map', True, const.Color.black), UI.Start.title_text)
        pygame.draw.rect(var.screen, const.Color.black, UI.Start.rect, 2)
        pygame.draw.rect(var.screen, const.Color.black, UI.Start.name, 2)
        var.screen.blit(var.Font.title.render(str(var.Editor.map_name), True, const.Color.black), UI.Start.name_text)
        
        var.screen.blit(img.Button.exit, UI.Start.exit_button)
        var.screen.blit(img.Button.done, UI.Start.done_button)

    if var.state == 'edit':
        for i in range(var.Editor.map_size):
            for j in range(var.Editor.map_size):
                var.screen.blit(img.Terrain.tile[var.Editor.floor[i][j]], [240 + 40 * j, 40 + 40 * i])

        pygame.draw.rect(var.screen, const.Color.white, UI.Main_Editor.minimap)
        pygame.draw.rect(var.screen, const.Color.white, UI.Main_Editor.left_bar)
        pygame.draw.rect(var.screen, const.Color.black, UI.Main_Editor.minimap, 2)
        pygame.draw.rect(var.screen, const.Color.black, UI.Main_Editor.left_bar, 2)

    pygame.display.flip()

def mouse_left_up():
    mouse = pygame.mouse.get_pos()

    if physics.point_inside_rect_list(mouse[0], mouse[1], UI.Upper_Bar.exit_button):
        var.state = ''
        var.scene = 'title'
        var.Editor.temp_data = []

    elif var.state == '':
        if physics.point_inside_rect_list(mouse[0], mouse[1], UI.Upper_Bar.new_button):
            var.state = 'start'
            var.Editor.map_name = 'New Map'
            var.Editor.map_name_edit = True

    elif var.state == 'start':
        if physics.point_inside_rect_list(mouse[0], mouse[1], UI.Start.name):
            if var.Editor.map_name_edit == True:
                var.Editor.map_name_edit = False
            else:
                var.Editor.map_name_edit = True

        elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.Start.exit_button):
            var.state = ''

        elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.Start.done_button):
            var.state = 'edit'
            map_generate()

    elif var.state == 'edit':
        if physics.point_inside_rect_list(mouse[0], mouse[1], UI.Upper_Bar.save_button):
            save_map()

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

def map_generate():
    var.Editor.terrain = []
    var.Editor.floor = []

    for i in range(var.Editor.map_size):
        temp = []

        for j in range(var.Editor.map_size):
            temp.append(101)

        var.Editor.floor.append(temp)

    for i in range(var.Editor.map_size):
        temp = []

        for j in range(var.Editor.map_size):
            temp.append(0)

        var.Editor.terrain.append(temp)

def save_map():
    file_directory = '../Map/' + str(var.Editor.map_name) + '.desmap'
    f = open(file_directory, 'w')

    f.write('Terrain\n')

    for i in range(len(var.Editor.terrain)):
        f.write(str(var.Editor.terrain[i]) + '\n')

    f.write('Floor\n')

    for i in range(len(var.Editor.floor)):
        f.write(str(var.Editor.floor[i]) + '\n')

    f.write('Unit\n')

    for i in range(len(var.Editor.unit)):
        f.write(str(var.Editor.unit[i] + '\n'))

    f.write('End\n')