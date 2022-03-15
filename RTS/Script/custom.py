import var
import img
import const
import pygame
import physics

class UI():
    title_text = [8, 8]
    rect = [160, 160, 960, 400]
    name = [240, 240, 800, 80]
    name_text = [248, 260]
    exit_button = [1080, 160, 40, 40]
    done_button = [1080, 520, 40, 40]

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    pygame.draw.rect(var.screen, const.Color.white, UI.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.rect, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.name, 2)

    var.screen.blit(var.Font.title.render(str(var.Custom.load_map_name), True, const.Color.black), UI.name_text)

    var.screen.blit(img.Button.exit, UI.exit_button[:2])
    var.screen.blit(img.Button.done, UI.done_button[:2])

    pygame.display.flip()

def mouse_left_up():
    mouse = pygame.mouse.get_pos()

    if physics.point_inside_rect_list(mouse[0], mouse[1], UI.name):
        if var.Custom.load_map_name_edit == True:
            var.Custom.load_map_name_edit = False
        else:
            var.Custom.load_map_name_edit = True
    
    elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.exit_button):
        var.scene = 'title'
        var.state = ''

    elif physics.point_inside_rect_list(mouse[0], mouse[1], UI.done_button):
        if len(var.Custom.load_map_name) > 0:
            success = load_map()
            if success == True:
                var.scene = 'field'
                var.state = ''

def load_map():
    var.Field.num_of_summoned_units = 0
    temp_dir = '../Map/' + var.Custom.load_map_name + '.desmap'

    f = open(temp_dir, 'a+')
    f.seek(0)

    mode = 'Terrain'

    file_contents = []

    while True:
        line = f.readline()
        
        if not line:
            break

        file_contents.append(line)

    if len(file_contents) == 0:
        return False

    var.Field.terrain = []
    var.Field.floor = []
    var.Field.unit = []

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

            var.Field.terrain.append(temp_list)

        if mode == 'Floor':
            temp_str = file_contents[i]
            length = len(temp_str)
            temp_str = temp_str[1:length - 2]
            temp_list = temp_str.split(',')

            for i in range(len(temp_list)):
                temp_list[i] = int(temp_list[i])

            var.Field.floor.append(temp_list)

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

            var.Field.num_of_summoned_units += 1
            var.Field.unit.append({'number' : var.Field.num_of_summoned_units,
                                   'ID' : temp_list[0],
                                   'name' : var.unit_list[temp_list[0]]['name'],
                                   'element' : var.unit_list[temp_list[0]]['element'],
                                   'type' : var.unit_list[temp_list[0]]['type'],
                                   'weapon' : var.unit_list[temp_list[0]]['weapon'],
                                   'attack' : var.unit_list[temp_list[0]]['attack'],
                                   'health' : var.unit_list[temp_list[0]]['health'],
                                   'speed' : var.unit_list[temp_list[0]]['speed'],
                                   'ability' : var.unit_list[temp_list[0]]['ability'],
                                   'position' : [temp_list[1], temp_list[2]],
                                   'size' : [temp_list[3], temp_list[4]],
                                   'move' : [False, [0, 0], [0, 0]],
                                   'team' : temp_list[5]})

    return True

def key_down(key):
    if var.state == '':
        if var.Custom.load_map_name_edit == True:
            if key >= 97 and key <= 122 or key >= 48 and key <= 57:
                temp_char = chr(key)
                var.Custom.load_map_name += temp_char

            elif key == 32:
                var.Custom.load_map_name += ' '

            elif key == 8:
                if len(var.Custom.load_map_name) > 0:
                    var.Custom.load_map_name = var.Custom.load_map_name[:len(var.Custom.load_map_name) - 1]