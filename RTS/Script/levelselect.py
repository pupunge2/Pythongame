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

    pygame.display.flip()

def mouse_left_up():
    pass
