import img
import var
import const
import pygame
import physics

class UI():
    hand = [240, 560, 560, 160]

    minimap = [0, 480, 240, 240]

    action_buttons = [[1040, 480, 80, 80], [1120, 480, 80, 80], [1200, 480, 80, 80],
                      [1040, 560, 80, 80], [1120, 560, 80, 80], [1200, 560, 80, 80],
                      [1040, 640, 80, 80], [1120, 640, 80, 80], [1200, 640, 80, 80]]

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    
    # Lower
    pygame.draw.rect(var.screen, const.Color.black, UI.minimap, 4)
    pygame.draw.rect(var.screen, const.Color.black, UI.hand, 4)

    for i in range(9):
        pygame.draw.rect(var.screen, const.Color.black, UI.action_buttons[i], 6)

    pygame.display.flip()

def mouse_left_up():
    pass

def mouse_right_up():
    pass
