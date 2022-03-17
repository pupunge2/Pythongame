from pydoc import cli
import var
import img
import const
import pygame
import physics

class UI():
    title_text = [8, 8]

    class Upper_Bar():
        rect = [0, 0, 1280, 40]
        new_button = [0, 0, 40, 40]
        load_button = [40, 0, 40, 40]
        save_button = [80, 0, 40, 40]
        team_button = [[120, 0, 40, 40], [160, 0, 40, 40], [200, 0, 40, 40], [240, 0, 40, 40]]
        delete_button = [280, 0, 40, 40]
        close_button = [320, 0, 40, 40]
        team_text = [[132, 12], [172, 12], [212, 12], [252, 12]]
        exit_button = [1240, 0, 40, 40]

    class Lower_Bar():
        rect = [0, 680, 1280, 40]

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

    class Load():
        title_text = [168, 168]
        rect = [160, 160, 960, 400]
        name = [240, 240, 800, 80]
        name_text = [248, 260]
        exit_button = [1080, 160, 40, 40]
        done_button = [1080, 520, 40, 40]

    class Main_Editor():
        minimap = [0, 40, 240, 240]
        left_bar = [0, 280, 240, 400]
        field_area = [240, 40, 1040, 680]

    class Misc():
        team_rect = [0, 0, 20, 20]

def loop():
    camera_move()
    display()

def display():
    var.screen.fill(const.Color.white)

    # Start & Load
    if var.state == 'start':
        var.screen.blit(var.Font.title.render('New Map', True, const.Color.black), UI.Start.title_text)
        pygame.draw.rect(var.screen, const.Color.black, UI.Start.rect, 2)
        pygame.draw.rect(var.screen, const.Color.black, UI.Start.name, 2)
        var.screen.blit(var.Font.title.render(str(var.Editor.map_name), True, const.Color.black), UI.Start.name_text)
        
        var.screen.blit(img.Button.exit, UI.Start.exit_button)
        var.screen.blit(img.Button.done, UI.Start.done_button)

    if var.state == 'load':
        var.screen.blit(var.Font.title.render('Open', True, const.Color.black), UI.Start.title_text)
        pygame.draw.rect(var.screen, const.Color.black, UI.Start.rect, 2)
        pygame.draw.rect(var.screen, const.Color.black, UI.Start.name, 2)
        var.screen.blit(var.Font.title.render(str(var.Editor.map_name), True, const.Color.black), UI.Start.name_text)
        
        var.screen.blit(img.Button.exit, UI.Start.exit_button)
        var.screen.blit(img.Button.done, UI.Start.done_button)

    # Edit
    if var.state == 'edit':
        # Field
        for i in range(var.Editor.map_size):
            for j in range(var.Editor.map_size):
                var.screen.blit(img.Terrain.tile[var.Editor.floor[i][j]], [UI.Main_Editor.field_area[0] + 40 * j - var.Editor.camera[0], UI.Main_Editor.field_area[1] + 40 * i - var.Editor.camera[1]])

        for i in range(len(var.Editor.unit)):
            var.screen.blit(img.Unit.unit[var.Editor.unit[i][0]], [var.Editor.unit[i][1][0] - var.Editor.unit[i][2][0] // 2 - var.Editor.camera[0] + UI.Main_Editor.field_area[0], var.Editor.unit[i][1][1]- var.Editor.unit[i][2][1] // 2- var.Editor.camera[1] + UI.Main_Editor.field_area[1]])
            temp_rect = [var.Editor.unit[i][1][0] - var.Editor.camera[0] + UI.Main_Editor.field_area[0] - var.Editor.unit[i][2][0] // 2, var.Editor.unit[i][1][1] - var.Editor.camera[1] + UI.Main_Editor.field_area[1] - var.Editor.unit[i][2][1] // 2, 8, 8]
            temp_color = ()

            if var.Editor.unit[i][3] == 1:
                temp_color = (255, 0, 0)
            elif var.Editor.unit[i][3] == 2:
                temp_color = (0, 255, 0)
            elif var.Editor.unit[i][3] == 3:
                temp_color = (0, 0, 255)
            elif var.Editor.unit[i][3] == 4:
                temp_color = (255, 0, 255)
            else:
                temp_color = (0, 0, 0)

            pygame.draw.rect(var.screen, temp_color, temp_rect)

        pygame.draw.rect(var.screen, const.Color.white, UI.Main_Editor.minimap)
        pygame.draw.rect(var.screen, const.Color.white, UI.Main_Editor.left_bar)
        pygame.draw.rect(var.screen, const.Color.black, UI.Main_Editor.minimap, 2)
        pygame.draw.rect(var.screen, const.Color.black, UI.Main_Editor.left_bar, 2)

        # Left bar
        for i in range(len(const.Editor.unit_list)):
            var.screen.blit(img.Unit.unit[const.Editor.unit_list[i]], [UI.Main_Editor.left_bar[0] + 40 * (i % 6), UI.Main_Editor.left_bar[1] + 40 * (i // 6)])

            if const.Editor.unit_list[i] == var.Editor.selected_unit:
                pygame.draw.rect(var.screen, const.Color.black, [UI.Main_Editor.left_bar[0] + 40 * (i % 6), UI.Main_Editor.left_bar[1] + 40 * (i // 6), 40, 40], 2)

    # Upper bar
    pygame.draw.rect(var.screen, const.Color.white, UI.Upper_Bar.rect)
    var.screen.blit(img.Button.new_map, UI.Upper_Bar.new_button[:2])
    var.screen.blit(img.Button.save, UI.Upper_Bar.save_button[:2])
    var.screen.blit(img.Button.load, UI.Upper_Bar.load_button[:2])
    var.screen.blit(img.Button.delete, UI.Upper_Bar.delete_button[:2])
    var.screen.blit(img.Button.exit, UI.Upper_Bar.close_button[:2])
    var.screen.blit(img.Button.exit, UI.Upper_Bar.exit_button[:2])

    if var.Editor.unit_delete_mode == True:
        pygame.draw.rect(var.screen, const.Color.green, UI.Upper_Bar.delete_button, 5)

    for i in range(4):
        pygame.draw.rect(var.screen, const.Color.black, UI.Upper_Bar.team_button[i], 4)
        var.screen.blit(var.Font.main_1.render(str(i + 1), True, const.Color.black), UI.Upper_Bar.team_text[i])
    
    pygame.draw.rect(var.screen, const.Color.blue, UI.Upper_Bar.team_button[var.Editor.team_mode - 1], 4)

    # Lower bar
    pygame.draw.rect(var.screen, const.Color.white, UI.Lower_Bar.rect)

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
            var.Editor.map_name = 'new map'
        elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.Upper_Bar.load_button):
            var.state = 'load'
            var.Editor.map_name = ''

    elif var.state == 'start':
        if physics.point_inside_rect_list(mouse[0], mouse[1], UI.Start.name):
            if var.Editor.map_name_edit == True:
                var.Editor.map_name_edit = False
            else:
                var.Editor.map_name_edit = True

        elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.Start.exit_button):
            var.state = ''

        elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.Start.done_button):
            if len(var.Editor.map_name) > 0:
                map_generate()
                var.state = 'edit'

    elif var.state == 'load':
        if physics.point_inside_rect_list(mouse[0], mouse[1], UI.Start.name):
            if var.Editor.map_name_edit == True:
                var.Editor.map_name_edit = False
            else:
                var.Editor.map_name_edit = True

        elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.Start.exit_button):
            var.state = ''

        elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.Start.done_button):
            if len(var.Editor.map_name) > 0:
                load_map(var.Editor.map_name)
                var.state = 'edit'

    elif var.state == 'edit':
        if physics.point_inside_rect_list(mouse[0], mouse[1], UI.Upper_Bar.save_button):
            save_map()

        elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.Upper_Bar.close_button):
            var.state = ''
            var.Editor.map_name = ''
            var.Editor.map_name_edit = False
            var.Editor.terrain = []
            var.Editor.floor = []
            var.Editor.unit = []
            var.Editor.camera = [0, 0]
            var.Editor.map_theme = 'grass'
            var.Editor.map_size = 64

        elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.Upper_Bar.delete_button):
            if var.Editor.unit_delete_mode == True:
                var.Editor.unit_delete_mode = False
            else:
                var.Editor.unit_delete_mode = True

        for i in range(4):
            if physics.point_inside_rect_list(mouse[0], mouse[1], UI.Upper_Bar.team_button[i]):
                var.Editor.team_mode = i + 1

        for i in range(len(const.Editor.unit_list)):
            temp_rect = [UI.Main_Editor.left_bar[0] + 40 * (i % 6), UI.Main_Editor.left_bar[1] + 40 * (i // 6), 40, 40]
            
            if physics.point_inside_rect_list(mouse[0], mouse[1], temp_rect):
                var.Editor.selected_unit = const.Editor.unit_list[i]

        if physics.point_inside_rect_list(mouse[0], mouse[1], UI.Main_Editor.field_area):
            click_field_pos = [mouse[0] - UI.Main_Editor.field_area[0] + var.Editor.camera[0], mouse[1] - UI.Main_Editor.field_area[1] + var.Editor.camera[1]]

            if var.Editor.selected_unit != -1 and var.Editor.unit_delete_mode == False:
                size = [const.Unit.size[var.Editor.selected_unit][0], const.Unit.size[var.Editor.selected_unit][1]]
                unit_add = True

                for i in range(len(var.Editor.unit)):
                    unit_position = [var.Editor.unit[i][1][0], var.Editor.unit[i][1][1]]
                    unit_size = [var.Editor.unit[i][2][0], var.Editor.unit[i][2][1]]

                    if physics.two_circle_overlap(click_field_pos[0], click_field_pos[1], unit_position[0], unit_position[1], const.Unit.size[var.Editor.selected_unit][0] // 2, unit_size[0] // 2):
                        unit_add = False
                        break
                
                if unit_add == True:
                    var.Editor.unit.append([var.Editor.selected_unit, [click_field_pos[0], click_field_pos[1]], [size[0], size[1]], var.Editor.team_mode])

            elif var.Editor.unit_delete_mode == True:
                for i in range(len(var.Editor.unit)):
                    top_left = [var.Editor.unit[i][1][0] - var.Editor.unit[i][2][0] // 2, var.Editor.unit[i][1][1] - var.Editor.unit[i][2][1] // 2]
                    rect = [var.Editor.unit[i][2][0], var.Editor.unit[i][2][1]]
                    
                    if physics.point_inside_rect(click_field_pos[0], click_field_pos[1], top_left[0], top_left[1], rect[0], rect[1]):
                        var.Editor.unit.pop(i)
                        break

def key_down(key):
    if var.state == 'start' or var.state == 'load':
        if var.Editor.map_name_edit == True:
            if key >= 97 and key <= 122 or key >= 48 and key <= 57:
                temp_char = chr(key)
                var.Editor.map_name += temp_char

            elif key == 32:
                var.Editor.map_name += ' '

            elif key == 8:
                if len(var.Editor.map_name) > 0:
                    var.Editor.map_name = var.Editor.map_name[:len(var.Editor.map_name) - 1]

    elif var.state == 'edit':
        if key == 119:
            var.Editor.key_pressed[0] = True

        elif key == 97:
            var.Editor.key_pressed[1] = True

        elif key == 100:
            var.Editor.key_pressed[2] = True

        elif key == 115:
            var.Editor.key_pressed[3] = True

def key_up(key):
    if var.state == 'edit':
        if key == 119:
            var.Editor.key_pressed[0] = False

        elif key == 97:
            var.Editor.key_pressed[1] = False

        elif key == 100:
            var.Editor.key_pressed[2] = False

        elif key == 115:
            var.Editor.key_pressed[3] = False

def camera_move():
    if var.Editor.key_pressed[0] == True:
        if var.Editor.camera[1] > 0:
            var.Editor.camera[1] -= 3

    if var.Editor.key_pressed[1] == True:
        if var.Editor.camera[0] > 0:
            var.Editor.camera[0] -= 3

    if var.Editor.key_pressed[2] == True:
        if var.Editor.camera[0] < 40 * 64 - 1280:
            var.Editor.camera[0] += 3

    if var.Editor.key_pressed[3] == True:
        if var.Editor.camera[1] < 40 * 64 - 720:
            var.Editor.camera[1] += 3

def map_generate():
    var.Editor.terrain = []
    var.Editor.floor = []
    var.Editor.unit = []

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
        f.write(str(var.Editor.unit[i]) + '\n')

    f.write('End\n')

def load_map(name):
    file_directory = '../Map/' + name + '.desmap'
    f = open(file_directory, 'a+')
    f.seek(0)
    
    mode = 'Terrain'

    file_contents = []

    while True:
        line = f.readline()
        
        if not line:
            break

        file_contents.append(line)

    if len(file_contents) == 0:
        var.Editor.map_theme = 'grass'
        var.Editor.map_size = 64
        map_generate()
        return

    var.Editor.terrain = []
    var.Editor.floor = []
    var.Editor.unit = []

    for i in range(len(file_contents)):
        if file_contents[i] == 'Terrain\n':
            mode = 'Terrain'
            continue
        elif file_contents[i] == 'Floor\n':
            mode = 'Floor'
            continue
        elif file_contents[i] == 'Unit\n':
            mode = 'Unit'
            continue
        elif file_contents[i] == 'End\n':
            break

        if mode == 'Terrain':
            temp_str = file_contents[i]
            length = len(temp_str)
            temp_str = temp_str[1:length - 2]
            temp_list = temp_str.split(',')

            for i in range(len(temp_list)):
                temp_list[i] = int(temp_list[i])

            var.Editor.terrain.append(temp_list)

        if mode == 'Floor':
            temp_str = file_contents[i]
            length = len(temp_str)
            temp_str = temp_str[1:length - 2]
            temp_list = temp_str.split(',')

            for i in range(len(temp_list)):
                temp_list[i] = int(temp_list[i])

            var.Editor.floor.append(temp_list)

        if mode == 'Unit':
            temp_str = file_contents[i]
            length = len(temp_str)
            temp_str = temp_str[1:length - 2]
            temp_list = temp_str.split(',')

            temp_list[0] = int(temp_list[0])
            temp_list[1] = temp_list[1][2:len(temp_list[1])]
            temp_list[1] = int(temp_list[1])
            temp_list[2] = temp_list[2][1:len(temp_list[2]) - 1]
            temp_list[2] = int(temp_list[2])
            temp_list[3] = temp_list[3][2:len(temp_list[3])]
            temp_list[3] = int(temp_list[3])
            temp_list[4] = temp_list[4][1:len(temp_list[4]) - 1]
            temp_list[4] = int(temp_list[4])
            temp_list[5] = temp_list[5][1:len(temp_list[5])]
            temp_list[5] = int(temp_list[5])

            var.Editor.unit.append([temp_list[0], [temp_list[1], temp_list[2]], [temp_list[3], temp_list[4]], temp_list[5]])
