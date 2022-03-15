import img
import var
import const
import pygame
import physics

class UI():
    hand = [240, 560, 560, 160]

    minimap = [0, 480, 240, 240]

    action_rect = [1040, 480, 240, 240]
    action_buttons = [[1040, 480, 80, 80], [1120, 480, 80, 80], [1200, 480, 80, 80],
                      [1040, 560, 80, 80], [1120, 560, 80, 80], [1200, 560, 80, 80],
                      [1040, 640, 80, 80], [1120, 640, 80, 80], [1200, 640, 80, 80]]

def loop():
    unit_move()
    display()

def display():
    var.screen.fill(const.Color.white)

    # Field
    for i in range(len(var.Field.floor)):
        for j in range(len(var.Field.floor[0])):
            if j * 40 - var.Field.camera[0] > -20 and j * 40 - var.Field.camera[0] < 1300 and i * 40 - var.Field.camera[1] > -20 and i * 40 - var.Field.camera[1] < 740:
                var.screen.blit(img.Terrain.tile[var.Field.floor[i][j]], [j * 40 - var.Field.camera[0], i * 40 - var.Field.camera[1]])

    for i in range(len(var.Field.unit)):
        position = [var.Field.unit[i]['position'][0], var.Field.unit[i]['position'][1]]
        size = [var.Field.unit[i]['size'][0], var.Field.unit[i]['size'][1]]

        var.screen.blit(img.Unit.unit[var.Field.unit[i]['ID']], [position[0] - size[0] // 2 - var.Field.camera[0], position[1] - size[1] // 2 - var.Field.camera[1]])

        temp_color = ()
        if var.Field.unit[i]['team'] == 1:
            temp_color = (255, 0, 0)
        elif var.Field.unit[i]['team'] == 2:
            temp_color = (0, 255, 0)
        elif var.Field.unit[i]['team'] == 3:
            temp_color = (0, 0, 255)
        elif var.Field.unit[i]['team'] == 4:
            temp_color = (255, 0, 255)
        else:
            temp_color = (0, 0, 0)

        pygame.draw.rect(var.screen, temp_color, [position[0] - size[0] // 2, position[1] - size[1] // 2] + [8, 8])

    for i in range(len(var.Player.selected_unit)):
        temp_index = var.Player.selected_unit[i]
        pygame.draw.rect(var.screen, const.Color.green, [var.Field.unit[temp_index]['position'][0] - var.Field.unit[temp_index]['size'][0] // 2, var.Field.unit[temp_index]['position'][1] - var.Field.unit[temp_index]['size'][1] // 2] + var.Field.unit[temp_index]['size'], 2)

    if var.Player.mouse_press == True:
        top_left = [min(var.Player.mouse_left_down[0], var.Player.mouse_move_position[0]), min(var.Player.mouse_left_down[1], var.Player.mouse_move_position[1])]
        rect_size = [abs(var.Player.mouse_move_position[0] - var.Player.mouse_left_down[0]), abs(var.Player.mouse_move_position[1] - var.Player.mouse_left_down[1])]
        pygame.draw.rect(var.screen, const.Color.green, top_left + rect_size, 3)

    # Lower
    pygame.draw.rect(var.screen, const.Color.white, UI.minimap)
    pygame.draw.rect(var.screen, const.Color.black, UI.minimap, 4)
    pygame.draw.rect(var.screen, const.Color.white, UI.hand)
    pygame.draw.rect(var.screen, const.Color.black, UI.hand, 4)

    pygame.draw.rect(var.screen, const.Color.white, UI.action_rect)

    for i in range(9):
        pygame.draw.rect(var.screen, const.Color.black, UI.action_buttons[i], 6)

    pygame.display.flip()

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

def unit_select():
    var.Player.selected_unit = []

    for i in range(len(var.Field.unit)):
        if var.Field.unit[i]['team'] == 1:
            top_left = [min(var.Player.mouse_left_down[0], var.Player.mouse_left_up[0]), min(var.Player.mouse_left_down[1], var.Player.mouse_left_up[1])]
            rect_size = [abs(var.Player.mouse_left_up[0] - var.Player.mouse_left_down[0]), abs(var.Player.mouse_left_up[1] - var.Player.mouse_left_down[1])]
            print(top_left, rect_size)
            if physics.circle_rect_overlap(var.Field.unit[i]['position'][0], var.Field.unit[i]['position'][1], var.Field.unit[i]['size'][0], top_left[0], top_left[1], rect_size[0], rect_size[1]):
                var.Player.selected_unit.append(i)

def unit_move_set():
    for i in range(len(var.Player.selected_unit)):
        temp_index = var.Player.selected_unit[i]
        var.Field.unit[temp_index]['move'][0] = True
        temp_vector = [var.Player.mouse_right_up[0]- var.Field.unit[temp_index]['position'][0], var.Player.mouse_right_up[1] - var.Field.unit[temp_index]['position'][1]]
        temp_vector = physics.vector_normalize(temp_vector)
        temp_vector = physics.vector_multiple_scalar(temp_vector, var.Field.unit[temp_index]['speed'])
        var.Field.unit[temp_index]['move'][1] = [temp_vector[0], temp_vector[1]]
        var.Field.unit[temp_index]['move'][2] = [var.Player.mouse_right_up[0], var.Player.mouse_right_up[1]]

def unit_move():
    for i in range(len(var.Field.unit)):
        if var.Field.unit[i]['move'][0] == True:
            var.Field.unit[i]['position'][0] += var.Field.unit[i]['move'][1][0]
            var.Field.unit[i]['position'][1] += var.Field.unit[i]['move'][1][1]

    for i in range(len(var.Field.unit)):
        if physics.distance_between_two_point(var.Field.unit[i]['position'][0], var.Field.unit[i]['position'][1], var.Field.unit[i]['move'][2][0], var.Field.unit[i]['move'][2][1]) < 10:
            var.Field.unit[i]['move'][0] = False

def mouse_left_down():
    mouse = pygame.mouse.get_pos()
    var.Player.mouse_left_down = [mouse[0], mouse[1]]
    var.Player.mouse_press = True

def mouse_left_up():
    mouse = pygame.mouse.get_pos()
    var.Player.mouse_left_up = [mouse[0], mouse[1]]
    var.Player.mouse_press = False

    if var.state == '':
        unit_select()

def mouse_move():
    mouse = pygame.mouse.get_pos()
    var.Player.mouse_move_position = [mouse[0], mouse[1]]

def mouse_right_up():
    mouse = pygame.mouse.get_pos()
    var.Player.mouse_right_up = [mouse[0], mouse[1]]
    unit_move_set()

def key_down(key):
    if var.state == '':
        if key == 119:
            var.Editor.key_pressed[0] = True

        elif key == 97:
            var.Editor.key_pressed[1] = True

        elif key == 100:
            var.Editor.key_pressed[2] = True

        elif key == 115:
            var.Editor.key_pressed[3] = True

def key_up(key):
    if var.state == '':
        if key == 119:
            var.Editor.key_pressed[0] = False

        elif key == 97:
            var.Editor.key_pressed[1] = False

        elif key == 100:
            var.Editor.key_pressed[2] = False

        elif key == 115:
            var.Editor.key_pressed[3] = False
